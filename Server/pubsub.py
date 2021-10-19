import time
import json
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from block import Block
from blockchain import Blockchain
from transaction import Transaction
from wallet import Wallet

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-af3ef0a0-0a7e-11ec-8e18-0664d1b72b66'
pnconfig.publish_key = 'pub-c-83008083-ffb0-45d9-8e08-c48a2ef822ad'
pnconfig.ssl = True

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK',
    'TRANSACTION': 'TRANSACTION'
}

def balances_cursos(blockchain): 
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

def user_balances(blockchain):
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

class Listener(SubscribeCallback):
    def __init__(self, blockchain, transaction_pool):
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool

    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                self.transaction_pool.clear_blockchain_transactions(
                    self.blockchain
                )
                user_balances(self.blockchain)
                balances_cursos(self.blockchain)
                with open("blockchain.json", "w+") as blockchain_json_load:
                    json.dump(self.blockchain.to_json(), blockchain_json_load)
                print('\n -- Successfully replaced local chain')

            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')
 
        # elif message_object.channel == CHANNELS['TRANSACTION']:
        #     transaction = Transaction.from_json(message_object.message)
        #     self.transaction_pool.set_transaction(transaction)
        #     print('\n -- Set the new transaction in the transaction pool')

    

class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self, blockchain, transaction_pool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

    def broadcast_transaction(self, transaction):
        """
        Broadcast a transaction to all nodes.
        """
        self.publish(CHANNELS['TRANSACTION'], transaction.to_json())

def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], { 'foo': 'bar' })

if __name__ == '__main__':
    main()
