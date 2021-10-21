from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.core.window import Window

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

# from android.permissions import request_permissions, Permission
# request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
import os
import requests
import random

from blockchain import Blockchain
from block import Block
from wallet import Wallet
from transaction import Transaction
from transaction_pool import TransactionPool
from pubsub import PubSub
from crypto_hash import crypto_hash
from kivy.utils import platform
import time

url_rasp = "https://zellet.iestellez.es:12100/"

user_name = ""
blockchain = Blockchain()
pubsub = ""
wallet = ""
transaction_pool = ""



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
            rgba: (0.45,0.51, 0.56, 1) 
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
            rgba: (0.45,0.51, 0.56, 1) 
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
            rgba: (0.45,0.51, 0.56, 1) 
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

<Menu_Acceso>:
    BoxLayout
        background_color: 0.94,0.94,0.95,1
        background_normal: ''
        orientation: 'vertical'
        spacing: 50
        padding: [50,50,50,50]
        BoxLayout:
            # padding: [30,30,30,30]
            orientation: 'vertical'
            background_color: 0.94,0.94,0.95,1
            background_normal: ''
            Image:
                id: introImage

                width: self.parent.width
                # height: self.parent.width/self.image_ratio
                # padding: [50,50,50,50]
                source: 'main_menu.png'
                # size: self.texture_size
                keep_ratio: True

        BoxLayout:
            orientation: 'vertical'
            size_hint: (.5, .2)
            pos_hint:{"center_x": 0.5}
            
            Button:
                text: 'Acceder como usuario'
                background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                canvas.before:
                    Color:
                        rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30]
                font_size: self.width/15
                on_release: app.root.current = "acceso_usuario"

        BoxLayout:
            orientation: 'vertical'
            size_hint: (.5, .2)
            pos_hint:{"center_x": 0.5}

            Button:
                text: 'Crear nuevo usuario'
                background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                canvas.before:
                    Color:
                        rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30]
                font_size: self.width/15
                on_release: app.root.current = "crear_usuario"


        Image:
            id: introImage

            width: self.parent.width
            # height: self.parent.width/self.image_ratio
            # padding: [50,50,50,50]
            source: 'logos_participantes.png'
            # size: self.texture_size
            keep_ratio: True

<Acceso_Usuario>:

    BoxLayout
        orientation: 'vertical'
        padding: [50,50,50,50]

        BoxLayout:
            # padding: [30,20,30,30]
            orientation: 'horizontal'
            Label:
                text: 'Introduce tus datos de usuario:'
                halign: 'center'
                text_size: self.size
                font_size: root.width/10
                # text_size: root.width-20, 20
                color: 0.85,0.55,0.11,1

        BoxLayout:
            padding: [30,20,30,30]
            orientation: 'horizontal'
            Label:
                text: 'Nombre de usuario'
                halign: 'center'
                
                font_size: root.width/30
                # text_size: root.width-20, 20
                color: 0.85,0.55,0.11,1

            TextInput:
                id: user_name
                # padding: [10,10,10,10]
                pos_hint: {'center_x': .5, 'center_y': .5}
                multiline:False
                font_size: root.width/30
                size_hint: (1, .2)


        BoxLayout:
            orientation: 'horizontal'
            padding: [30,20,30,30]
            Label:
                text: 'Contraseña'
                halign: 'center'
                font_size: root.width/30
                # text_size: root.width-20, 20
                color: 0.85,0.55,0.11,1

            TextInput:
                id: key
                password:True
                multiline:False
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: root.width/30
                size_hint: (1, .2)

        BoxLayout:
            orientation: "horizontal"
            padding: [30,40,30,30]

            BoxLayout:
                orientation: "horizontal"
                padding: [20,20,20,20]
                size_hint: (.5, .5)
                pos_hint:{"center_x": 0.5}

                Button:
                    text: 'Acceder'
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: root.acceder(user_name.text, key.text)
                    pos_hint:{"center_x": 0.25, "center_y": 0.80}

            BoxLayout:
                orientation: "horizontal"
                padding: [20,20,20,20]
                size_hint: (.5, .5)
                pos_hint:{"center_x": 0.5}

                Button:
                    text: "Volver"
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: app.root.current = "acceso"
                    pos_hint:{"center_x": 0.75, "center_y": 0.80}

<Crear_Usuario>:

    BoxLayout
        orientation: 'vertical'
        # spacing: 5
        padding: [20,20,20,20]

        BoxLayout:
            # padding: [30,30,30,30]
            orientation: 'horizontal'
            Label:
                text: 'Introduce tus datos de usuario:'
                halign: 'center'
                text_size: self.size
                font_size: root.width/18
                # text_size: root.width-20, 20
                color: 0.85,0.55,0.11,1
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Nombre de usuario'
                halign: 'center'
                font_size: root.width/30
                color: 0.85,0.55,0.11,1

            TextInput:
                id: user_name
                pos_hint: {'center_x': .5, 'center_y': .5}
                multiline:False
                font_size: root.width/30
                size_hint: (1, .4)

        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Contraseña'
                halign: 'center'
                font_size: root.width/30
                color: 0.85,0.55,0.11,1

            TextInput:
                id: key
                password:True
                pos_hint: {'center_x': .5, 'center_y': .5}
                multiline:False
                font_size: root.width/30
                size_hint: (1, .4)

        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Repetir contraseña'
                halign: 'center'
                font_size: root.width/30
                color: 0.85,0.55,0.11,1

            TextInput:
                id: key_rep
                password:True
                pos_hint: {'center_x': .5, 'center_y': .5}
                multiline:False
                font_size: root.width/30
                size_hint: (1, .4)

        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Nombre y apellidos'
                halign: 'center'
                font_size: root.width/30
                color: 0.85,0.55,0.11,1

            TextInput:
                id: nombre_apellidos
                pos_hint: {'center_x': .5, 'center_y': .5}
                multiline:False
                font_size: root.width/30
                size_hint: (1, .4)

        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Correo'
                halign: 'center'
                font_size: root.width/30
                color: 0.85,0.55,0.11,1

            TextInput:
                id: correo
                pos_hint: {'center_x': .5, 'center_y': .5}
                multiline:False
                font_size: root.width/30
                size_hint: (1, .4)

        BoxLayout:
            orientation:"horizontal"
            BoxLayout:

                Label:
                    text: 'Curso'
                    halign: 'center'
                    font_size: root.width/30
                    color: 0.85,0.55,0.11,1
            
            BoxLayout:
                orientation: 'horizontal'

                Spinner:
                    id: curso
                    values: ["1º ESO", "2º ESO", "3º ESO", "4º ESO",]
                    font_size: root.width/30
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    size_hint: (1, .4)

                Spinner:
                    id: letra
                    values: ["A", "B", "C", "D",]
                    font_size: root.width/30
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    size_hint: (1, .4)


        BoxLayout:
            orientation: "horizontal"
            # padding: [30,40,30,30]

            BoxLayout:
                orientation: "vertical"
                padding: [20,20,20,20]
                size_hint: (.5, .9)
                pos_hint:{"center_x": 0.5}
                Button:
                    text: "Volver"
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: app.root.current = "acceso"

            BoxLayout:
                orientation: "vertical"
                padding: [20,20,20,20]
                size_hint: (.5, .9)
                pos_hint:{"center_x": 0.5}
                Button:
                    text: 'Acceder'
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: root.creacion_usuario(user_name.text, key.text, key_rep.text, nombre_apellidos.text, correo.text, curso.text, letra.text)




<Menu_Principal>:

    BoxLayout:
        orientation: "vertical"
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
            # padding: [50,50,50,50]
            # spacing: 20
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
                    text: "Volver"
                    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                    canvas.before:
                        Color:
                            rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [30]
                    font_size: self.width/15
                    on_release: app.root.current = "acceso"

                

<Transacciones>:
    BoxLayout
        orientation: 'vertical'
        canvas:
            Color:
                rgba: (0.94,.94,.95,1) 
            Rectangle:
                size: self.size
                pos: self.pos
        BoxLayout:
            RV_transacciones:
                id: rv_transacciones_recibidas
        BoxLayout:
            RV_transacciones:
                id: rv_transacciones_realizadas
        BoxLayout:
            size_hint:(0.5, 0.3)
            padding: [20,20,20,20]
            pos_hint: {'center_x': .5, 'center_y': .1}
            Button:
                background_color: 0,0,0,0
                canvas.before:
                    Color:
                        rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30]
                text: "Volver"
                font_size: root.width/30
                on_release: app.root.current = "principal"

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
            size_hint:(0.5, 0.3)
            padding: [20,20,20,20]
            pos_hint: {'center_x': .5, 'center_y': .1}
            Button:
                
                background_color: 0,0,0,0
                canvas.before:
                    Color:
                        rgba: (.4,.4,.4,1) if self.state=='normal' else (.87,.44,.007,1)  # visual feedback of press
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30]
                text: "Volver"
                font_size: root.width/30
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
        self.saludo = "Hola "+user_name
    
    def get_zellets(self):
        peticion = requests.get(url_rasp+str(crypto_hash("A vuestra puta casa"))+'/'+str(crypto_hash("Devuelve dinero cartera")), verify=False, timeout=10,
                params={'user': user_name}).json()

        return str(peticion["balance"])

    def resetForm(self):
        self.ids['recipient'].text = ""
        self.ids['amount'].text = ""
        self.ids['concept'].text = ""

    def ejecutar_transaccion(self, receptor, cantidad, concepto):
        app = App.get_running_app()

        app.recipient = receptor
        app.amount = cantidad
        app.concept = concepto
        if receptor.rstrip() == user_name:
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
                    int(cantidad),
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
                        content = Button(text='UPS! Parece que se ha realizado otra transacción en este mismo instante. Realiza la transacción de nuevo.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
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

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of lista_dinero_users in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))

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

class Menu_Acceso(Screen):   
    blockchain = Blockchain()

#################################################################################################### 

class Acceso_Usuario(Screen):
       
    def acceder(self, usuario, clave):

        global user_name 
        global blockchain 
        global pubsub 
        global wallet 
        global transaction_pool

        app = App.get_running_app()
        app.access_user = usuario
        app.access_key = clave

        try:
            peticion_user = requests.get(url_rasp+str(crypto_hash("info de user"))+'/'+str(crypto_hash("Tome informaçao")),  verify=False, timeout=10,
            params={'user': usuario.rstrip(),
                    'key': clave})

            if(peticion_user.text == "no_existe"):
                content = Button(text='El usuario no existe',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                popup = Popup(title="Error",  content=content, auto_dismiss=False)
                
                content.bind(on_press=popup.dismiss)
                popup.open()

                self.ids['user_name'].text = ""
                self.ids['key'].text = ""
                return True
                    
            else:

                datos_usuario = peticion_user.json()

                self.get_blockchain()
        
                user_name = datos_usuario["nombre"]
                wallet = Wallet(blockchain)
                wallet.address = datos_usuario["address"]
                wallet.public_key = datos_usuario["public_key"]
                wallet.private_key = datos_usuario["private_key"] = serialization.load_pem_private_key(datos_usuario["private_key"].encode('utf-8') , password=None, backend=default_backend())
                transaction_pool = TransactionPool()
                pubsub = PubSub(blockchain, transaction_pool)                

                content = Button(text='Hola, '+usuario,size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                popup = Popup(title="Acceso",  content=content, auto_dismiss=False)
                
                content.bind(on_press=popup.dismiss)
                popup.open()
                self.ids['user_name'].text = ""
                self.ids['key'].text = ""
                self.manager.current = 'principal'
        except:
           
            content = Button(text='No ha sido posible establecer una conexión con los servidores. Inténtelo más tarde.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
            popup = Popup(title="Error",  content=content, auto_dismiss=False)
            
            content.bind(on_press=popup.dismiss)
            popup.open()

            return True

    def get_blockchain(self):
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
            content = Button(text='No ha sido posible establecer una conexión con los servidores. Inténtelo de nuevo.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
            popup = Popup(title="Error",  content=content, auto_dismiss=False)
            
            content.bind(on_press=popup.dismiss)
            popup.open()

            return True

####################################################################################################        

class Crear_Usuario(Screen):
    def creacion_usuario(self, user, clave, clave_rep, nombre_apellidos, correo, curso, letra):
        app = App.get_running_app()
        app.user_name = user
        app.key = clave
        app.key_rep = clave_rep
        app.nombre_apellidos = nombre_apellidos
        app.correo = correo
        app.curso = curso
        app.letra = letra

        if(clave == clave_rep):
      
            self.wallet = Wallet()

            try:

                peticion_existe_user = requests.get(url_rasp+str(crypto_hash("info de user"))+'/'+str(crypto_hash("Existe el usuario?")),verify=False,
                params={'user': user})

                if(peticion_existe_user.text != "no_existe"):
                    content = Button(text='Ya existe un usuario con ese nombre',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    return True

                elif user == "":
                    content = Button(text='No se ha especificado un nombre de usuario.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    return True

                elif clave == "":
                    content = Button(text='No se ha especificado la contraseña.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    return True

                elif clave_rep == "":
                    content = Button(text='No se ha repetido la contraseña.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    return True

                elif nombre_apellidos == "":
                    content = Button(text='No se ha especificado el nombre del usuario.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    return True

                elif correo == "":
                    content = Button(text='No se ha especificado el correo del usuario.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    return True

                elif curso == "":
                    content = Button(text='No se ha especificado el curso del usuario.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    return True

                elif letra == "":
                    content = Button(text='No se ha especificado el grupo del usuario.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Error",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    return True                   

                else:
                    requests.post(url_rasp+str(crypto_hash("info de user"))+'/'+str(crypto_hash("Deme la informaçao")), verify=False,json = {
                    "nombre": user.rstrip(),
                    "nombre_y_apellidos": nombre_apellidos,
                    "correo": correo.rstrip(),
                    "curso": curso + " " + letra,
                    "contrasena": clave,
                    "address": self.wallet.address,
                    "private_key": self.wallet.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
                ).decode('utf-8'),
                    "public_key": self.wallet.public_key
                })

                    content = Button(text='Gracias por unirte al monedero social. En breve se confirmará tu alta.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                    popup = Popup(title="Aviso",  content=content, auto_dismiss=False)
                    
                    content.bind(on_press=popup.dismiss)
                    popup.open()

                    self.ids['user_name'].text = ""
                    self.ids['key'].text = ""
                    self.ids['key_rep'].text = ""
                    self.ids['nombre_apellidos'].text = ""
                    self.ids['correo'].text = ""
                    self.ids['curso'].text = ""
                    self.ids['letra'].text = ""

                    self.manager.current = 'acceso'

                    return True
            except:
                content = Button(text='No ha sido posible establecer una conexión con los servidores. Inténtelo más tarde.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
                popup = Popup(title="Error",  content=content, auto_dismiss=False)
                
                content.bind(on_press=popup.dismiss)
                popup.open()

        else:
            content = Button(text='Las contraseñas no coinciden.',size_hint =(.2, .2), pos_hint ={'center_x':.5, 'center_y':.5})
            popup = Popup(title="Error",  content=content, auto_dismiss=False)
            
            content.bind(on_press=popup.dismiss)
            popup.open()

            return True

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


class LoginApp(MDApp):

    recipient = StringProperty(None)
    amount = ObjectProperty("integer")





    def build(self):

        manager = ScreenManager()
        manager.add_widget(Menu_Acceso(name='acceso'))
        manager.add_widget(Menu_Principal(name='principal'))
        manager.add_widget(Acceso_Usuario(name='acceso_usuario'))
        manager.add_widget(Crear_Usuario(name='crear_usuario'))
        manager.add_widget(Listas(name='listas'))
        manager.add_widget(Transacciones(name='transacciones'))

        return manager

    def on_key(self, key, *args):
        if key == 27 or key == 1001:  # the esc key
            pass

    Window.bind(on_keyboard=on_key)

if __name__ == '__main__':
    LoginApp().run()


