# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 600)
        MainWindow.setMinimumSize(QSize(880, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(60, 231, 195);")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.introduccion_datos = QWidget()
        self.introduccion_datos.setObjectName(u"introduccion_datos")
        self.stackedWidget.addWidget(self.introduccion_datos)
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 10, 561, 41))
        self.label.setStyleSheet(u"font: 25 36pt \"Roboto\";\n"
"color: rgb(226, 113, 17);")
        self.label_title_5 = QLabel(self.menu)
        self.label_title_5.setObjectName(u"label_title_5")
        self.label_title_5.setGeometry(QRect(410, 210, 211, 51))
        self.label_title_5.setFont(font1)
        self.label_title_5.setStyleSheet(u"color: rgb(226, 113, 17);")
        self.cantidad = QLineEdit(self.menu)
        self.cantidad.setObjectName(u"cantidad")
        self.cantidad.setGeometry(QRect(620, 274, 101, 41))
        self.cantidad.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.label_title_4 = QLabel(self.menu)
        self.label_title_4.setObjectName(u"label_title_4")
        self.label_title_4.setGeometry(QRect(520, 270, 91, 51))
        self.label_title_4.setFont(font1)
        self.label_title_4.setStyleSheet(u"color: rgb(226, 113, 17);")
        self.label_3 = QLabel(self.menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 160, 221, 41))
        self.label_3.setStyleSheet(u"font: 25 20pt \"Roboto\";\n"
"color: rgb(226, 113, 17);")
        self.ejecutar_trans = QPushButton(self.menu)
        self.ejecutar_trans.setObjectName(u"ejecutar_trans")
        self.ejecutar_trans.setGeometry(QRect(730, 274, 151, 41))
        self.ejecutar_trans.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(226, 113, 17);\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.nombre_receptor = QLineEdit(self.menu)
        self.nombre_receptor.setObjectName(u"nombre_receptor")
        self.nombre_receptor.setGeometry(QRect(620, 214, 261, 41))
        self.nombre_receptor.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.balance = QLineEdit(self.menu)
        self.balance.setObjectName(u"balance")
        self.balance.setGeometry(QRect(20, 50, 131, 41))
        self.balance.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.label_title_7 = QLabel(self.menu)
        self.label_title_7.setObjectName(u"label_title_7")
        self.label_title_7.setGeometry(QRect(50, 20, 71, 21))
        self.label_title_7.setFont(font1)
        self.label_title_7.setStyleSheet(u"color: rgb(226, 113, 17);")
        self.refrescar = QPushButton(self.menu)
        self.refrescar.setObjectName(u"refrescar")
        self.refrescar.setGeometry(QRect(390, 390, 141, 71))
        self.refrescar.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(226, 113, 17);\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.menu_posicionamiento = QPushButton(self.menu)
        self.menu_posicionamiento.setObjectName(u"menu_posicionamiento")
        self.menu_posicionamiento.setGeometry(QRect(630, 370, 251, 41))
        self.menu_posicionamiento.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(226, 113, 17);\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_title_19 = QLabel(self.menu)
        self.label_title_19.setObjectName(u"label_title_19")
        self.label_title_19.setGeometry(QRect(70, 100, 251, 51))
        self.label_title_19.setFont(font1)
        self.label_title_19.setStyleSheet(u"color: rgb(226, 113, 17);")
        self.transacciones_recibidas = QTreeWidget(self.menu)
        self.transacciones_recibidas.setObjectName(u"transacciones_recibidas")
        self.transacciones_recibidas.setGeometry(QRect(20, 140, 321, 131))
        self.transacciones_recibidas.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.label_title_20 = QLabel(self.menu)
        self.label_title_20.setObjectName(u"label_title_20")
        self.label_title_20.setGeometry(QRect(60, 300, 241, 51))
        self.label_title_20.setFont(font1)
        self.label_title_20.setStyleSheet(u"color: rgb(226, 113, 17);")
        self.transacciones_realizadas = QTreeWidget(self.menu)
        self.transacciones_realizadas.setObjectName(u"transacciones_realizadas")
        self.transacciones_realizadas.setGeometry(QRect(20, 340, 321, 131))
        self.transacciones_realizadas.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.menu_usuarios_pendientes = QPushButton(self.menu)
        self.menu_usuarios_pendientes.setObjectName(u"menu_usuarios_pendientes")
        self.menu_usuarios_pendientes.setGeometry(QRect(630, 420, 251, 41))
        self.menu_usuarios_pendientes.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(226, 113, 17);\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.menu)
        self.pag_usuarios_pendientes = QWidget()
        self.pag_usuarios_pendientes.setObjectName(u"pag_usuarios_pendientes")
        self.label_4 = QLabel(self.pag_usuarios_pendientes)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 50, 301, 41))
        self.label_4.setStyleSheet(u"font: 25 20pt \"Roboto\";\n"
"color: rgb(226, 113, 17);")
        self.aceptar_user = QPushButton(self.pag_usuarios_pendientes)
        self.aceptar_user.setObjectName(u"aceptar_user")
        self.aceptar_user.setGeometry(QRect(310, 380, 91, 41))
        self.aceptar_user.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(226, 113, 17);\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.lista_usuarios_pendientes = QTreeWidget(self.pag_usuarios_pendientes)
        self.lista_usuarios_pendientes.setObjectName(u"lista_usuarios_pendientes")
        self.lista_usuarios_pendientes.setGeometry(QRect(20, 120, 861, 221))
        self.lista_usuarios_pendientes.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.no_aceptar_user = QPushButton(self.pag_usuarios_pendientes)
        self.no_aceptar_user.setObjectName(u"no_aceptar_user")
        self.no_aceptar_user.setGeometry(QRect(490, 380, 91, 41))
        self.no_aceptar_user.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(226, 113, 17);\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.volver_pendientes = QPushButton(self.pag_usuarios_pendientes)
        self.volver_pendientes.setObjectName(u"volver_pendientes")
        self.volver_pendientes.setGeometry(QRect(730, 440, 151, 41))
        self.volver_pendientes.setStyleSheet(u"QPushButton {\n"
"		background-color: rgb(226, 113, 17);\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.pag_usuarios_pendientes)
        self.pag_cartera = QWidget()
        self.pag_cartera.setObjectName(u"pag_cartera")
        self.label_6 = QLabel(self.pag_cartera)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 10, 411, 41))
        self.label_6.setStyleSheet(u"font: 25 36pt \"Roboto\";\n"
"color: rgb(226, 113, 17);")
        self.pos_users = QTreeWidget(self.pag_cartera)
        self.pos_users.setObjectName(u"pos_users")
        self.pos_users.setGeometry(QRect(20, 170, 401, 191))
        self.pos_users.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.pos_cursos = QTreeWidget(self.pag_cartera)
        self.pos_cursos.setObjectName(u"pos_cursos")
        self.pos_cursos.setGeometry(QRect(490, 170, 391, 191))
        self.pos_cursos.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.label_8 = QLabel(self.pag_cartera)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(600, 120, 201, 41))
        self.label_8.setStyleSheet(u"font: 25 18pt \"Roboto\";\n"
"color: rgb(226, 113, 17);")
        self.label_7 = QLabel(self.pag_cartera)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 120, 261, 41))
        self.label_7.setStyleSheet(u"font: 25 18pt \"Roboto\";\n"
"color: rgb(226, 113, 17);")
        self.volver_posicionamiento = QPushButton(self.pag_cartera)
        self.volver_posicionamiento.setObjectName(u"volver_posicionamiento")
        self.volver_posicionamiento.setGeometry(QRect(730, 440, 151, 41))
        self.volver_posicionamiento.setStyleSheet(u"QPushButton {\n"
"		background-color: rgb(226, 113, 17);\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.pag_cartera)
        self.pag_inicio = QWidget()
        self.pag_inicio.setObjectName(u"pag_inicio")
        self.stackedWidget.addWidget(self.pag_inicio)
        self.pag_nuevo_usuario = QWidget()
        self.pag_nuevo_usuario.setObjectName(u"pag_nuevo_usuario")
        self.stackedWidget.addWidget(self.pag_nuevo_usuario)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgba(33, 33, 75,0);")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"border: none;\n"
"border-radius:20px;")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.mensajes = QLineEdit(self.frame_label_credits)
        self.mensajes.setObjectName(u"mensajes")
        self.mensajes.setGeometry(QRect(10, 0, 891, 20))
        self.mensajes.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.mensajes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Moneda social admin", None))
        self.label_title_5.setText(QCoreApplication.translate("MainWindow", u"Nombre del receptor", None))
        self.label_title_4.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enviar Zellets", None))
        self.ejecutar_trans.setText(QCoreApplication.translate("MainWindow", u"Ejecutar transacci\u00f3n", None))
        self.label_title_7.setText(QCoreApplication.translate("MainWindow", u"Zellets", None))
        self.refrescar.setText(QCoreApplication.translate("MainWindow", u"Refrescar datos", None))
        self.menu_posicionamiento.setText(QCoreApplication.translate("MainWindow", u"Posicionamiento global", None))
        self.label_title_19.setText(QCoreApplication.translate("MainWindow", u"Transacciones emitidas", None))
        ___qtreewidgetitem = self.transacciones_recibidas.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Concepto", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Balance", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Emisor", None));
        self.label_title_20.setText(QCoreApplication.translate("MainWindow", u"Transacciones recibidas", None))
        ___qtreewidgetitem1 = self.transacciones_realizadas.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Concepto", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Balance", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Receptor", None));
        self.menu_usuarios_pendientes.setText(QCoreApplication.translate("MainWindow", u"Usuarios pendientes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Usuarios pendientes", None))
        self.aceptar_user.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        ___qtreewidgetitem2 = self.lista_usuarios_pendientes.headerItem()
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"Correo", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Curso", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Nombre y apellidos", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Nombre de usuario", None));
        self.no_aceptar_user.setText(QCoreApplication.translate("MainWindow", u"No aceptar", None))
        self.volver_pendientes.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Posicionamiento", None))
        ___qtreewidgetitem3 = self.pos_users.headerItem()
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"Zellets", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtreewidgetitem4 = self.pos_cursos.headerItem()
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"Zellets", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Curso", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Zellets por curso", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Zellets por usuario", None))
        self.volver_posicionamiento.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
    # retranslateUi

