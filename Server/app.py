import os
import requests
import json
from flask import Flask, jsonify, request, Response

import time
import random
import shutil
from blockchain import Blockchain
from block import Block
from wallet import Wallet
from transaction import Transaction
from transaction_pool import TransactionPool
from pubsub import PubSub
from crypto_hash import crypto_hash
from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend  

import subprocess

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

shutil.copy('balances.json', 'balances_sec.json')

############## Carga del monedero ##############



blockchain = Blockchain()
with open("blockchain.json", "r+") as file:
    sec_blockchain_json = json.load(file)
    sec_blockchain = Blockchain()
    sec_blockchain = sec_blockchain.from_json(sec_blockchain_json)

# url_rasp = ["https://158.49.247.152:443/","https://158.49.247.162:443/"]
url_rasp = ["https://192.168.0.23:443/","https://192.168.0.24:443/"]

#test_1 = subprocess.call(['ping', '-c', '2', "192.168.0.22"]) == 1
#test_2 = subprocess.call(['ping', '-c', '2', "192.168.0.23"]) == 1

# print(test_1)
# print(test_2)

#if (test_1 and test_2):
#    blockchain = sec_blockchain

#else:
counter = 0
for url in url_rasp:
    try:
        result_blockchain = Blockchain.from_json(requests.get(url+str(crypto_hash("A vuestra puta casa")), verify=False, timeout=1).json())
        try:
            blockchain.replace_chain(result_blockchain.chain)
            print('\n -- Successfully synchronized the local chain')
            break
        except Exception as e:
            print(f'\n -- Error synchronizing: {e}')  
            
    
    except:
        print("No ha sido posible contactar con el servidor con url "+url)
        counter += 1
# print(counter)
if counter == 2:
    if len(blockchain.chain) < len(sec_blockchain.chain):
        print("cargando blockchain")
        blockchain = sec_blockchain

############## Carga o creación de monedero ##############

try:
    with open("server_wallet.json", "r+") as file:
        data = json.load(file)
    wallet = Wallet(blockchain)
    wallet.address = data["address"]
    wallet.public_key = data["public_key"]
    wallet.private_key = data["private_key"] = serialization.load_pem_private_key(data["private_key"].encode('utf-8') , password=None, backend=default_backend())
except:
    wallet = Wallet(blockchain)
    wallet_data = {
        "address":wallet.address,
        "public_key":wallet.public_key,
        "private_key":wallet.private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()).decode('utf-8'),
    }
    with open("server_wallet.json", "w+") as file:
        json.dump(wallet_data, file)

transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)

############## Funciones de mantenimiento y test ##############

@app.route("/prueba_funcionamiento")
def index():
    return Response("El servidor está activo", status=200)

@app.route('/'+str(crypto_hash("A vuestra puta casa")))
def route_blockchain():
    actualizar_datos()
    return jsonify(blockchain.to_json())

############## Transacciones y minado ##############

@app.route('/'+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Información sobre la cartera")))
def route_wallet_info():
    return jsonify({ 'address': wallet.address, 'balance': wallet.balance })

def actualiza_user_balances():
    lista_balance_users = []
    with open("users.json", "r+") as user_list:
        lista_users = json.load(user_list)
    for usuario in lista_users:
        balance_data = {
            "user" : usuario["nombre"],
            "balance" : Wallet.calculate_balance(blockchain, usuario["address"], False)
        }
        lista_balance_users.append(balance_data)

    balances_ordenados = sorted(lista_balance_users, key=lambda lista : lista["balance"],reverse=True)
    with open("balances.json", "w+") as fichero_balances:
        json.dump(balances_ordenados, fichero_balances)
    return balances_ordenados

@app.route('/'+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Restaurar dinero monederos")))
def restaurar_dinero():
    with open("balances_sec.json", "r+") as user_balances:
        lista = json.load(user_balances)
    return {"data": lista}  


@app.route('/'+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Muestra monederos usuarios")))
def user_balances():

    return {"data" : actualiza_user_balances()}

@app.route('/'+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Devuelve dinero cartera")))
def devolver_dinero_cartera():
    receiver = request.args.get("user")
    with open("users.json", "r+") as user_list:
        lista_users = json.load(user_list)
    for usuario in lista_users:
        if usuario["nombre"] == receiver:
            # print(Wallet.calculate_balance(blockchain, usuario["address"], False))
            return {"balance" : Wallet.calculate_balance(blockchain, usuario["address"], False)}
    return "El user no existe"

def actualizar_balances_cursos(): 
    lista_balances_cursos = []
    cursos = []
    with open("users.json", "r+") as user_list:
        lista_users = json.load(user_list)
    for usuario in lista_users:
        if not usuario["curso"] in cursos:
            curso_balance_data = {
                "curso" : usuario["curso"],
                "balance" : Wallet.calculate_balance(blockchain, usuario["address"], False)
            }
            lista_balances_cursos.append(curso_balance_data)
            cursos.append(usuario["curso"])
        else:
            for balances in lista_balances_cursos:
                if balances["curso"] == usuario["curso"]:
                    balances["balance"] += Wallet.calculate_balance(blockchain, usuario["address"], False)
                    break
    balances_ordenados = sorted(lista_balances_cursos, key=lambda lista : lista["balance"],reverse=True)
    with open("balance_cursos.json", "w+") as fichero_balances:
        json.dump(balances_ordenados, fichero_balances)
    return balances_ordenados

@app.route('/'+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Muestra balance por curso")))
def balances_cursos(): 
    return {"data":actualizar_balances_cursos()}
  
@app.route('/'+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Ahora vas y minas")))
def route_blockchain_mine():
    transaction_data = transaction_pool.transaction_data()
    transaction_data.append(Transaction.reward_transaction(wallet).to_json())
    blockchain.add_block(transaction_data)
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)
    transaction_pool.clear_blockchain_transactions(blockchain)

    return jsonify(block.to_json())

@app.route('/'+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Hacer transacción")), methods=['POST'])
def route_wallet_transact():
    transaction_data = request.get_json()
    transaction = transaction_pool.existing_transaction(wallet.address)

    if transaction:
        transaction.update(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )
    else:
        transaction = Transaction(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )

    pubsub.broadcast_transaction(transaction)

    return jsonify(transaction.to_json())

@app.route('/'+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Prueba sin pool")), methods=['POST'])
def realizar_transaccion_prueba():
    
    transaction_data = request.get_json()
    print(transaction_data)

    transaction = transaction_pool.existing_transaction(wallet.address)

    if transaction:
        transaction.update(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )
    else:
        transaction = Transaction(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )

    # print(transaction.to_json())
    # pubsub.broadcast_transaction(transaction)
    # return jsonify(transaction_pool.transaction_data())

    # transaction_data = transaction_pool.transaction_data()
    transaction_data = [transaction.to_json()]
    block = Block.mine_block(blockchain.chain[-1], transaction_data)
    pubsub.broadcast_block(block)







############## Información sobre los usuarios ##############
        
@app.route('/'+str(crypto_hash("info de user"))+'/'+str(crypto_hash("Deme la informaçao")), methods=['POST']) # Utilizado al crear un nuevo usuario, con el objetivo de almacenar su información en el servidor
def route_add_wallet_info():
    wallet_data = request.get_json()
    with open("users_queue.json", "r+") as file:
         data = json.load(file)
    data["usuarios"].append(wallet_data)
    with open("users_queue.json", "w+") as file:
         json.dump(data, file)
    # if wallet_data["propagar"] == 1:
    #     wallet_data["propagar"] = 0
    #     for server in url_rasp:
    #         requests.post(server+str(crypto_hash("info de user"))+'/'+str(crypto_hash("Deme la informaçao")), verify=False,json = wallet_data)
    bot_send_text()
    return "añadido"
    
@app.route('/'+str(crypto_hash("info de user"))+'/'+str(crypto_hash("Solicitar cantidad"))) # Utilizado al crear un nuevo usuario, con el objetivo de almacenar su información en el servidor
def devolver_dinero(): 
    
    with open("balances.json", "r+") as file:
         data = json.load(file)
    for user_data in data:
        if(user_data["user"] == request.args.get('user')):
            return {"data":user_data["balance"]}

@app.route('/'+str(crypto_hash("info de user"))+'/'+str(crypto_hash("Tome informaçao"))) # Utilizado para que un usuario pueda acceder a la aplicación
def get_wallet_info():
    print("currando")
    with open("users.json", "r") as file:
        data = json.load(file)
    for user_data in data:
        if(user_data["nombre"] == request.args.get('user') and user_data["contrasena"] == request.args.get('key')):
            return jsonify(user_data)
    return "no_existe"

@app.route('/'+str(crypto_hash("info de user"))+'/'+str(crypto_hash("Existe el usuario?"))) # Utilizado para relacionar a un nombre de usuario con una dirección.
def existe_el_user():
    print("currando")
    with open("users.json", "r") as file:
        data = json.load(file)
    for user_data in data:
        if(user_data["nombre"] == request.args.get('user')):
            return "existe"
    return "no_existe"

@app.route('/'+str(crypto_hash("info de user"))+'/'+str(crypto_hash("comprobando existencia user")))
def comprobando_user():
    print("currando")
    with open("users.json", "r") as file:
        data = json.load(file)
    for user_data in data:
        if(user_data["nombre"] == request.args.get('user')):
            return user_data["address"]	
    return "no_existe"

@app.route('/'+str(crypto_hash("info de user"))+'/'+str(crypto_hash("nombre from address")))
def buscar_nombre():
    print("currando")
    with open("users.json", "r") as file:
        data = json.load(file)
    for user_data in data:
        if(user_data["nombre"] == request.args.get('user')):
            return user_data["address"]	
    return "no_existe"    

@app.route('/'+str(crypto_hash("info de user"))+ '/'+ str(crypto_hash("entrega usuarios pendientes")))
def confirmacion_usuarios():
    print("currando")
    with open ("users_queue.json", "r") as fichero_pendientes:
        users_pendientes = json.load(fichero_pendientes)
    return users_pendientes

@app.route('/'+str(crypto_hash("info de user"))+ '/'+ str(crypto_hash("confirmación user")))
def confirmar_user():
    print("currando")
    confirmacion = request.args.get("conf")

    with open("users_queue.json", "r") as fichero_pendientes:
        users_pendientes = json.load(fichero_pendientes)
   
    nombre = request.args.get("nombre")
    # print(nombre)
    for user in users_pendientes["usuarios"]:
        if user["nombre"] == nombre:
            if confirmacion == "1":
                with open ("users.json", "r") as fichero_admitidos:
                    users_admitidos = json.load(fichero_admitidos)
                users_admitidos.append(user)
                with open("users.json", "w+") as file:
                    json.dump(users_admitidos, file)
                users_pendientes["usuarios"].remove(user)
                enviar_correo(user["correo"], user["nombre"])
            else:
                users_pendientes["usuarios"].remove(user)
                
    with open("users_queue.json", "w+") as file:
        json.dump(users_pendientes, file)
    # if request.args.get("propagar") == 1:
    #     for server in url_rasp:
    #         requests.post(server+str(crypto_hash("info de user"))+'/'+str(crypto_hash("confirmación user")), verify=False,params={'nombre': request.args.get("nombre"), "conf": request.args.get("conf"), "propagar" : 0})
    actualizar_datos()
    return "Ok"

def enviar_correo(correo_receptor, nombre_receptor):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.message import EmailMessage

    message = EmailMessage()

    sender = "zelletwallet@gmail.com"
    recipient = correo_receptor
    body_of_email = "Hola "+nombre_receptor+". Tu monedero de Zellets ha sido confirmado."
    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = 'Se ha confirmado tu cuenta de Zellet Wallet'

    message.set_content(body_of_email)

    s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
    s.login(sender, password = "TelLez2021.")
    s.send_message(message)
    s.quit()

@app.route('/'+str(crypto_hash("info de user"))+ '/'+ str(crypto_hash("recupera datos")))
def recuperar_datos():
    correo_user = request.args.get("correo")
    with open("users.json", "r") as fichero_users:
        usuarios = json.load(fichero_users)    
    for user in usuarios:
        if correo_user == user["correo"]:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            from email.message import EmailMessage

            message = EmailMessage()

            sender = "zelletwallet@gmail.com"
            recipient = correo_user
            body_of_email = "Hola "+user["nombre"]+". Estos son los datos de tu cuenta: \n - Nombre de usuario: " + user["nombre"]+"\n - Contraseña: "+ user["contrasena"]
            message['From'] = sender
            message['To'] = recipient

            message['Subject'] = 'Datos de cuenta'

            message.set_content(body_of_email)

            s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
            s.login(sender, password = "TelLez2021.")
            s.send_message(message)
            s.quit()    
            return "existe"
    return "no_existe"

def bot_send_text():

    bot_message = "Hay un nuevo usuario pendiente de confirmación"
    bot_token = '1784796735:AAGtcZtAfngDY224mkmdFFd3Okxfeyj5Hvs'
    bot_chatID = '1516729742'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)

def actualizar_datos():
    actualiza_user_balances()
    actualizar_balances_cursos()

@app.route('/'+str(crypto_hash("info de user"))+ '/'+ str(crypto_hash("confirmación user mobile")))
def confirmar_user_mobile():
    confirmacion = request.args.get("conf")


    with open("users_queue.json", "r") as fichero_pendientes:
        users_pendientes = json.load(fichero_pendientes)
   
    nombres_usuarios = request.args.get("users")
    # print(nombres_usuarios)
    for user in users_pendientes["usuarios"]:
        if user["nombre"] in nombres_usuarios:
            if confirmacion == "1":
                enviar_correo(user["correo"], user["nombre"])
                with open ("users.json", "r") as fichero_admitidos:
                    users_admitidos = json.load(fichero_admitidos)
                users_admitidos.append(user)
                with open("users.json", "w+") as file:
                    json.dump(users_admitidos, file)
                users_pendientes["usuarios"].remove(user)
        else:
            users_pendientes["usuarios"].remove(user)
                
    with open("users_queue.json", "w+") as file:
        json.dump(users_pendientes, file)
    # for server in url_rasp:
    #     requests.post(server+str(crypto_hash("info de user"))+'/'+str(crypto_hash("confirmación user mobile")), verify=False,params={'users': request.args.get("users"), "conf": request.args.get("conf")})
    actualizar_datos()
    return "Ok"   
         
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000, ssl_context="adhoc") 


