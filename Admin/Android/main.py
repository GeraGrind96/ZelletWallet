from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from kivy.metrics import dp
# from android.permissions import request_permissions, Permission
# request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
import os
import requests
import random
import json
from blockchain import Blockchain
from block import Block
from wallet import Wallet
from transaction import Transaction
from transaction_pool import TransactionPool
from pubsub import PubSub
from crypto_hash import crypto_hash

import time

url_rasp = "https://zellet.iestellez.es:12100/"

def get_blockchain():
    global blockchain
    try:
        result_blockchain = Blockchain.from_json(requests.get(url_rasp+str(crypto_hash("A vuestra puta casa")), verify=False).json())
        print(result_blockchain)
        try:
            blockchain.replace_chain(result_blockchain.chain)
            print('\n -- Successfully synchronized the local chain')
        except Exception as e:
            print(f'\n -- Error synchronizing: {e}') 
    
    except:
        print("No ha sido posible establecer una comunicación con los servidores. Reinicia la aplicación.") 

user_name = "Admin"
blockchain = Blockchain()
get_blockchain()
wallet = Wallet(blockchain)
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)  

wallet_data = {               
        "address": wallet.address,
        "private_key": wallet.private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8'),
        "public_key": wallet.public_key,
    }

with open("admin_data.json", "r+") as file:
    data = json.load(file)
if "address" in data.keys():
    wallet.address = data["address"]
    wallet.public_key = data["public_key"]
    wallet.private_key = data["private_key"] = serialization.load_pem_private_key(data["private_key"].encode('utf-8') , password=None, backend=default_backend())
else:
    with open("admin_data.json", "w+") as file:
        json.dump(wallet_data, file)

data_tables = None

Builder.load_string('''

# <SelectableLabel>:
#     # Draw a background to indicate selection
#     canvas.before:
#         Color:
#             rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
#         Rectangle:
#             pos: self.pos
#             size: self.size

<Tabelle_transacciones>:
    orientation: 'horizontal'
    spalte1_SP: 'spalte1'
    spalte2_SP: 'spalte2'
    spalte3_SP: 'spalte3'
    canvas.before:
        Color:
            rgba: (0, 0, 0, 1) 
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        id: SP1
        text: root.spalte1_SP
    Label:
        id: SP2
        text: root.spalte2_SP
    Label:
        id: SP3
        text: root.spalte3_SP

<Tabelle_users>:
    orientation: 'horizontal'
    spalte1_SP: 'spalte1'
    spalte2_SP: 'spalte2'
    canvas.before:
        Color:
            rgba: (0, 0, 0, 1) 
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        id: SP1
        text: root.spalte1_SP
    Label:
        id: SP2
        text: root.spalte2_SP

<Tabelle_cursos>:
    orientation: 'horizontal'
    spalte1_SP: 'spalte1'
    spalte2_SP: 'spalte2'
    canvas.before:
        Color:
            rgba: (0, 0, 0, 1) 
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        id: SP1
        text: root.spalte1_SP
    Label:
        id: SP2
        text: root.spalte2_SP
# <RV>:
#     viewclass: 'SelectableLabel'
#     SelectableRecycleBoxLayout:
#         default_size: None, dp(56)
#         default_size_hint: 1, None
#         size_hint_y: None
#         height: self.minimum_height
#         orientation: 'vertical'
#         multiselect: True
#         touch_multiselect: True

<RV_transacciones>:
    viewclass: 'Tabelle_transacciones'
    RecycleBoxLayout:
        default_size: None, dp(20)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'

<RV_users>:
    viewclass: 'Tabelle_users'
    RecycleBoxLayout:
        default_size: None, dp(20)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'

<RV_cursos>:
    viewclass: 'Tabelle_cursos'
    RecycleBoxLayout:
        default_size: None, dp(20)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'


<Menu_Principal>:
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            orientation: "vertical"
            canvas:
                Color:
                    rgba: (.4,.4,.4,1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [600]
        
            Label:
            
                text: 'Zellet Wallet'

                halign: 'center'
                valign: 'middle'

                text_size: self.size
                font_size: root.width/10
                # text_size: root.width-20, 20
                color: 0.85,0.55,0.11,1

        BoxLayout:

            orientation: 'horizontal'
           

            BoxLayout:
                orientation: 'vertical'
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        id: id_user
                        text: root.saludo
                        font_size: root.width/20
                        color: 0.85,0.55,0.11,1
                    Label:
                        id: user_zellets
                        text: root.zellets
                        font_size: root.width/20
                        color: 0.85,0.55,0.11,1
                BoxLayout:
                    orientation: 'vertical'
                    Image:
                        
                        width: self.parent.width
                        # height: self.parent.width/self.image_ratio
                        # padding: [50,50,50,50]
                        source: 'icon.png'
                        # size: self.texture_size
                        keep_ratio: True

                

            BoxLayout:
                id: transactions
                orientation: 'vertical'
                padding: [10,10,10,10]
                # spacing: 20

                # Label:
                #     text: 'Transacción'
                #     color: 0.85,0.55,0.11,1
                #     font_size: root.width/20
                #     text_size: self.size
                #     halign: 'center'

                BoxLayout:
                    orientation: 'vertical'

                    BoxLayout:
                        id: transactions
                        orientation: 'vertical'
                        # padding: [10,10,10,10]
                        # spacing: 20

                        Label:
                            text: 'Receptor'
                            color: 0.85,0.55,0.11,1
                            font_size: root.width/30
                            halign: 'center'
                            text_size: self.size


                        TextInput:
                            id: recipient
                            multiline:False
                            font_size: root.width/40
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            multiline:False
                            size_hint: (1, 0.8)

                    BoxLayout:
                        id: transactions
                        orientation: 'vertical'
                        # padding: [10,10,10,10]
                        # spacing: 20

                        Label:
                            text: 'Cantidad'
                            color: 0.85,0.55,0.11,1
                            halign: 'center'
                            text_size: self.size
                            font_size: root.width/30


                        TextInput:
                            id: amount
                            multiline:False
                            font_size: root.width/40
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            multiline:False
                            size_hint: (1, 0.8)

                    BoxLayout:
                        id: transactions
                        orientation: 'vertical'
                        # padding: [10,10,10,10]
                        # spacing: 20

                        Label:
                            text: 'Concepto'
                            color: 0.85,0.55,0.11,1
                            halign: 'center'
                            text_size: self.size
                            font_size: root.width/30

                        TextInput:
                            id: concept
                            multiline:False
                            font_size: root.width/40
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            multiline:False
                            size_hint: (1, 0.8)

                BoxLayout:
                    orientation: "vertical"
                    padding: [20,20,20,20]
                    size_hint: (1, .5)
                    pos_hint:{"center_x": 0.5}

                    Button:
                        text: 'Realizar transacción'
                        background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                        canvas.before:
                            Color:
                                rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [30]
                        font_size: self.width/15
                        on_release: root.ejecutar_transaccion(recipient.text, amount.text, concept.text)

        BoxLayout:
            orientation: 'vertical'
            padding: [50,50,50,50]

            BoxLayout:
                orientation: "vertical"
                padding: [20,20,20,20]
                size_hint: (0.5, .5)
                pos_hint:{"center_x": 0.5}

                Button:
                    text: "Ver listas"
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: app.root.current = "listas"

            BoxLayout:
                orientation: "vertical"
                padding: [20,20,20,20]
                size_hint: (0.5, .5)
                pos_hint:{"center_x": 0.5}

                Button:
                    text: "Ver transacciones"
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: app.root.current = "transacciones"

            BoxLayout:
                orientation: "vertical"
                padding: [20,20,20,20]
                size_hint: (0.5, .5)
                pos_hint:{"center_x": 0.5}

                Button:
                    text: "Ver usuarios pendientes"
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: app.root.current = "usuarios"
            
                

<Transacciones>:
    BoxLayout
        orientation: 'vertical'
        BoxLayout:
            RV_transacciones:
                id: rv_transacciones_recibidas
        BoxLayout:
            RV_transacciones:
                id: rv_transacciones_realizadas
        BoxLayout:
            Button:
                text: "Volver"
                font_size: root.width/30
                on_press: app.root.current = "principal"

<Listas>:
    BoxLayout
        orientation: 'vertical'
        BoxLayout:
            RV_users:
                id: rv_users
        BoxLayout:
            RV_cursos:
                id: rv_cursos
        BoxLayout:
            Button:
                text: "Volver"
                font_size: root.width/30
                on_press: app.root.current = "principal"

<Usuarios>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'vertical'
            id: solicitudes
        
            
            pos_hint: {'center_x': .5, 'center_y': .25}
            size_hint:(1, 0.75)
        BoxLayout:
            # orientation: 'vertical'
          
            orientation: "horizontal"

            # pos_hint: {'center_x': .5, 'center_y': .9}
            # size_hint:(.25, 0.25)
            BoxLayout:
                size_hint:(0.3, 0.2)
                padding: [20,20,20,20]
                pos_hint: {'center_x': .5, 'center_y': .5}
                Button:
                    text: 'Aceptar usuarios'
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: root.enviar_usuarios_admitidos() 
            BoxLayout:
                size_hint:(0.3, 0.2)
                padding: [20,20,20,20]
                pos_hint: {'center_x': .5, 'center_y': .5}
                Button:
                    text: 'Volver'
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: app.root.current = "principal"


''')

#################################################################################################### 

class Menu_Principal(Screen):

    zellets = StringProperty()
    saludo = StringProperty()
    
    # def __init__(self, **kwargs):
    #     super(Menu_Principal, self).__init__(**kwargs)
        # self.dinero_en_cuenta = "0"
    #     self.zellets = "Tienes "+self.get_zellets()+" Zellets"

    def on_pre_enter(self, *args):
        self.zellets = "Tienes "+self.get_zellets()+" Zellets"
        self.saludo = "Hola Admin"
    
    def get_zellets(self):
        dinero = wallet.balance

        return str(dinero)




    def resetForm(self):
        self.ids['recipient'].text = ""
        self.ids['amount'].text = ""
        self.ids['concept'].text = ""

    def ejecutar_transaccion(self, receptor, cantidad, concepto):
        app = App.get_running_app()

        app.recipient = receptor
        app.amount = cantidad
        app.concept = concepto
        if receptor == user_name:
            content = Button(text='No puedes enviarte monedas a tí mismo',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
            popup = Popup(title="Error",  content=content, auto_dismiss=False)           
            content.bind(on_press=popup.dismiss)
            popup.open()
        else:
            try:
                addr_receptor = requests.get(url_rasp+str(crypto_hash("info de user"))+'/'+str(crypto_hash("nombre from address")), verify=False,params={'user': receptor.rstrip()})

                if addr_receptor.text != "no_existe":
                    transaction = Transaction(
                    wallet,
                    addr_receptor.text,
                    int(cantidad.rstrip()),
                    concepto,
                    receptor.rstrip(),
                    user_name,
                    )
                    transaction_data = [transaction.to_json()]
                    block = Block.mine_block(blockchain.chain[-1], transaction_data)
                    pubsub.broadcast_block(block)
                    time.sleep(1)

                    bloque_nuevo = block.to_json()
                    bloque_nuevo_en_blockchain = blockchain.to_json()[-1]

                    if  bloque_nuevo['hash'] != bloque_nuevo_en_blockchain['hash']:
                        content = Button(text='Se ha producido un error al realizar la transacción.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                        popup = Popup(title="Error",  content=content, auto_dismiss=False)           
                        content.bind(on_press=popup.dismiss)
                        popup.open()
                    else:
                        content = Button(text='Transacción realizada correctamente.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                        popup = Popup(title="Aviso",  content=content, auto_dismiss=False)           
                        content.bind(on_press=popup.dismiss)
                        popup.open()
                        self.resetForm()
                else:
                    content = Button(text='El usuario receptor no existe',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)           
                    content.bind(on_press=popup.dismiss)
                    popup.open()
            except:
                content = Button(text='No ha sido posible establecer una conexión con los servidores. Inténtelo más tarde.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                popup = Popup(title="Error",  content=content, auto_dismiss=False)
                
                content.bind(on_press=popup.dismiss)
                popup.open()

                return True

class Tabelle_users(BoxLayout):
    pass

class Tabelle_cursos(BoxLayout):
    pass

class Tabelle_transacciones(BoxLayout):
    pass

class RV_users(RecycleView):
    def __init__(self, **kwargs):
        super(RV_users, self).__init__(**kwargs)

    def actualizar_dinero_users(self):
        try:
            balances_usuarios = requests.get(url_rasp+str(crypto_hash("A vuestra puta casa"))+ '/'+ str(crypto_hash("Muestra monederos usuarios")), verify=False)
            balances_usuarios_json = balances_usuarios.json()
            lista_dinero_users = [{'SP1': 'Usuario', 'SP2': 'Zellets'}]
            for user in balances_usuarios_json["data"]:
                lista_dinero_users.append({'SP1': user["user"], 'SP2' : user[str("balance")]})
            self.data = [{'spalte1_SP': str(x['SP1']), 'spalte2_SP': str(x['SP2'])} for x in lista_dinero_users]
        except:
            content = Button(text='No ha sido posible establecer una conexión con los servidores. Inténtelo más tarde.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
            popup = Popup(title="Error",  content=content, auto_dismiss=False)
            
            content.bind(on_press=popup.dismiss)
            popup.open()

            return True

class RV_cursos(RecycleView):
    def __init__(self, **kwargs):
        super(RV_cursos, self).__init__(**kwargs)

    def actualizar_dinero_cursos(self):
        try:
            balances_cursos = requests.get(url_rasp+str(crypto_hash("A vuestra puta casa"))+ '/'+ str(crypto_hash("Muestra balance por curso")), verify=False)
            balances_cursos_json = balances_cursos.json()

            lista_dinero_cursos = [{'SP1': 'Curso', 'SP2': 'Zellets'}]
            for user in balances_cursos_json["data"]:
                lista_dinero_cursos.append({'SP1': user["curso"], 'SP2' : user[str("balance")]})
            self.data = [{'spalte1_SP': str(x['SP1']), 'spalte2_SP': str(x['SP2'])} for x in lista_dinero_cursos]
        except:
            content = Button(text='No ha sido posible establecer una conexión con los servidores. Inténtelo más tarde.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
            popup = Popup(title="Error",  content=content, auto_dismiss=False)
            
            content.bind(on_press=popup.dismiss)
            popup.open()

            return True

class RV_transacciones(RecycleView):
    def __init__(self, **kwargs):
        super(RV_transacciones, self).__init__(**kwargs)

    def actualizar_transacciones_realizadas(self):
        lista_transacciones_realizadas = [{'SP1': 'Receptor', 'SP2': 'Cantidad', 'SP3': 'Concepto'}]

        blockchain_json = blockchain.to_json()
        for i in range(1, len(blockchain_json)):
            bloque = blockchain_json[i]
            if bloque["data"][0]["input"]["address"] == wallet.address:   
                lista_transacciones_realizadas.append({'SP1': bloque["data"][0]["receiver"], 'SP2': str(bloque["data"][0]["output"][bloque["data"][0]["recipient"]]), 'SP3': bloque["data"][0]["concept"]}) 
                # print("Receptor: "+bloque["data"][0]["receiver"])   
                # print("Cantidad: "+str(bloque["data"][0]["output"][bloque["data"][0]["recipient"]]))   
                # print("Concepto: "+bloque["data"][0]["concept"])   
        self.data = [{'spalte1_SP': str(x['SP1']), 'spalte2_SP': str(x['SP2']), 'spalte3_SP': str(x['SP3'])} for x in lista_transacciones_realizadas]

    def actualizar_transacciones_recibidas(self):
        lista_transacciones_recibidas = [{'SP1': 'Emisor', 'SP2': 'Cantidad', 'SP3': 'Concepto'}]

        blockchain_json = blockchain.to_json()
        for i in range(1, len(blockchain_json)):
            bloque = blockchain_json[i]
            if bloque["data"][0]["recipient"] == wallet.address and bloque["data"][0]["emitter"] != None:  
                lista_transacciones_recibidas.append({'SP1': bloque["data"][0]["emitter"], 'SP2': str(bloque["data"][0]["output"][bloque["data"][0]["recipient"]]), 'SP3': bloque["data"][0]["concept"]})   
                # print("Emisor: "+bloque["data"][0]["emitter"])   
                # print("Cantidad: "+str(bloque["data"][0]["output"][bloque["data"][0]["recipient"]]))  
                # print("Concepto: "+bloque["data"][0]["concept"])   
        self.data = [{'spalte1_SP': str(x['SP1']), 'spalte2_SP': str(x['SP2']), 'spalte3_SP': str(x['SP3'])} for x in lista_transacciones_recibidas]

####################################################################################################


       
#################################################################################################### 

class Listas(Screen):
    def on_pre_enter(self, *args):
        self.ids.rv_users.actualizar_dinero_users()
        self.ids.rv_cursos.actualizar_dinero_cursos()
        return super().on_pre_enter(*args)

class Transacciones(Screen):
    def on_pre_enter(self, *args):
        self.ids.rv_transacciones_recibidas.actualizar_transacciones_recibidas()
        self.ids.rv_transacciones_realizadas.actualizar_transacciones_realizadas()
        return super().on_pre_enter(*args)

class Usuarios(Screen):
    data_tables = ""
    button = ""
    usuarios_admitidos = []

    def on_pre_enter(self, *args):
        self.add_datatable()
        # self.add_button()
        return super().on_pre_enter(*args)

    def add_datatable(self):
        usuarios_pendientes = requests.get(url_rasp+str(crypto_hash("info de user"))+ '/'+ str(crypto_hash("entrega usuarios pendientes")), verify=False)
        users_json = usuarios_pendientes.json()
        datos = []
        for user in users_json["usuarios"]:
            datos.append((user["nombre"], user["nombre_y_apellidos"], user["correo"], user["curso"]))
        datos.append(("-","-","-","-"))

        if self.data_tables:
            self.ids.solicitudes.remove_widget(self.data_tables)

        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            size_hint=(0.9, 0.6),
            column_data=[
                ("Nombre de usuario", dp(30)),
                ("Nombre y apellidos", dp(30)),
                ("Correo", dp(30)),
                ("Curso", dp(30)),
            ],
            row_data=datos
        )
        self.data_tables.bind(on_check_press=self.boton_presionado)
        self.ids.solicitudes.add_widget(self.data_tables)

        # self.button = Button(text="Aceptar usuarios", size_hint_y=None)
        # self.button.bind(on_press=self.enviar_usuarios_admitidos)
        # self.ids.solicitudes.add_widget(self.button)

    def boton_presionado(self, instance_table, current_row):

        if current_row[0] in self.usuarios_admitidos:
            self.usuarios_admitidos.remove(current_row[0])
        else:
            self.usuarios_admitidos.append(current_row[0])
        # print(self.usuarios_admitidos)

    def enviar_usuarios_admitidos(self):
        requests.get(url_rasp+str(crypto_hash("info de user"))+'/'+str(crypto_hash("confirmación user mobile")), verify=False,params={'users': self.usuarios_admitidos, "conf": "1"})
        self.usuarios_admitidos.clear()
        self.ids.solicitudes.remove_widget(self.data_tables)
        self.add_datatable()

class LoginApp(MDApp):

    recipient = StringProperty(None)
    amount = ObjectProperty("integer")
    
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Menu_Principal(name='principal'))
        manager.add_widget(Listas(name='listas'))
        manager.add_widget(Transacciones(name='transacciones'))
        manager.add_widget(Usuarios(name='usuarios'))

        return manager

if __name__ == '__main__':
    LoginApp().run()


