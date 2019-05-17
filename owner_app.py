from PyQt5 import QtCore, QtGui, QtWidgets
import util
import sqlite3

class RegisterWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 575)
        MainWindow.setMinimumSize(QtCore.QSize(392, 575))
        MainWindow.setMaximumSize(QtCore.QSize(392, 575))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.cityChoice = QtWidgets.QComboBox(self.widget)
        self.cityChoice.setGeometry(QtCore.QRect(20, 70, 320, 20))
        self.cityChoice.setObjectName("cityChoice")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 81, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 50, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.registerButton = QtWidgets.QPushButton(self.widget)
        self.registerButton.setGeometry(QtCore.QRect(20, 510, 111, 25))
        self.registerButton.setObjectName("registerButton")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(160, 510, 211, 20))
        self.label_9.setObjectName("label_9")
        self.townChoice = QtWidgets.QComboBox(self.widget)
        self.townChoice.setGeometry(QtCore.QRect(20, 120, 320, 20))
        self.townChoice.setObjectName("townChoice")
        self.districtChoice = QtWidgets.QComboBox(self.widget)
        self.districtChoice.setGeometry(QtCore.QRect(20, 170, 320, 20))
        self.districtChoice.setObjectName("districtChoice")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(20, 300, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(210, 300, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(20, 350, 161, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(210, 350, 121, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(20, 400, 51, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.nameField = QtWidgets.QLineEdit(self.widget)
        self.nameField.setGeometry(QtCore.QRect(20, 20, 320, 20))
        self.nameField.setObjectName("nameField")
        self.ownerSSNField = QtWidgets.QLineEdit(self.widget)
        self.ownerSSNField.setGeometry(QtCore.QRect(20, 220, 320, 20))
        self.ownerSSNField.setObjectName("ownerSSNField")
        self.addressField = QtWidgets.QLineEdit(self.widget)
        self.addressField.setGeometry(QtCore.QRect(20, 270, 320, 20))
        self.addressField.setObjectName("addressField")
        self.emailField = QtWidgets.QLineEdit(self.widget)
        self.emailField.setGeometry(QtCore.QRect(20, 420, 325, 20))
        self.emailField.setObjectName("emailField")
        self.phoneNumberField = QtWidgets.QLineEdit(self.widget)
        self.phoneNumberField.setGeometry(QtCore.QRect(210, 370, 130, 20))
        self.phoneNumberField.setObjectName("phoneNumberField")
        self.ownerNameField = QtWidgets.QLineEdit(self.widget)
        self.ownerNameField.setGeometry(QtCore.QRect(20, 320, 130, 20))
        self.ownerNameField.setObjectName("ownerNameField")
        self.ownerSurnameField = QtWidgets.QLineEdit(self.widget)
        self.ownerSurnameField.setGeometry(QtCore.QRect(210, 320, 130, 20))
        self.ownerSurnameField.setObjectName("ownerSurnameField")
        self.ownerPhoneNumberField = QtWidgets.QLineEdit(self.widget)
        self.ownerPhoneNumberField.setGeometry(QtCore.QRect(20, 370, 130, 20))
        self.ownerPhoneNumberField.setObjectName("ownerPhoneNumberField")
        self.passwordField = QtWidgets.QLineEdit(self.widget)
        self.passwordField.setGeometry(QtCore.QRect(20, 470, 130, 20))
        self.passwordConfirmation = QtWidgets.QLineEdit(self.widget)
        self.passwordConfirmation.setGeometry(QtCore.QRect(210, 470, 130, 20))
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(20, 450, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(210, 450, 72, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.cityChoice.addItem("Adana", ["Ceyhan", "Çukurova", "Konakoğlu Mah.", "Kozan", "Sarıçam", "Seyhan", "Yüreğir"])
        self.cityChoice.addItem("Adıyaman", ["Besni", "Çelikhan"])
        self.cityChoice.addItem("Afyon", ["Basmakçı", "Çay"])
        self.cityChoice.addItem("Ağrı", ["Diyadin", "Tutak"])
        self.cityChoice.addItem("Amasya", ["Hamamözü", "Merkez"])
        self.cityChoice.addItem("Ankara", ["Akyurt", "Etimesgut"])
        self.cityChoice.addItem("Antalya", ["Akseki", "Aksu"])
        self.cityChoice.addItem("Artvin", ["Ardanuç", "Hopa"])
        self.cityChoice.addItem("Aydın", ["Bozdoğan", "Çine"])
        self.cityChoice.addItem("Balıkesir", ["Ayvalık", "Balya"])
        self.cityChoice.addItem("Bilecik", ["Bozüyük", "Merkez"])
        self.cityChoice.addItem("Bingöl", ["Adaklı", "Genç"])
        self.cityChoice.addItem("Bitlis", ["Ahlat", "Hizan"])
        self.cityChoice.addItem("Bolu", ["Gerede", "Mudurnu"])
        self.cityChoice.addItem("Burdur", ["Bucak", "Gölhisar"])
        self.cityChoice.addItem("Bursa", ["Nilüfer", "Gürsu"])
        self.cityChoice.addItem("Çanakkale", ["Ayvacık", "Biga"])
        self.cityChoice.addItem("Çankırı", ["Orta", "Çerkeş"])
        self.cityChoice.addItem("Çorum", ["Alaca", "Bayat"])
        self.cityChoice.addItem("Denizli", ["Acıpayam", "Merkez"])
        self.cityChoice.addItem("Diyarbakır", ["Bağlar", "Çınar"])
        self.cityChoice.addItem("Edirne", ["Enez", "Keşan"])
        self.cityChoice.addItem("Elazığ", ["Ağın", "Baskil"])
        self.cityChoice.addItem("Erzincan", ["İliç", "Merkez"])
        self.cityChoice.addItem("Erzurum", ["Aşkale", "Çat"])
        self.cityChoice.addItem("Eskişehir", ["Tepebaşı", "Çifteler"])
        self.cityChoice.addItem("Gaziantep", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Giresun", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Gümüşhane", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Hakkari", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Hatay", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Isparta", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Mersin", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("İstanbul", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("İzmir", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kars", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kastamonu", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kayseri", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kırklareli", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kırşehir", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kocaeli", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Konya", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kütahya", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Malatya", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Manisa", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kahramanmaraş", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Mardin", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Muğla", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Muş", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Nevşehir", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Niğde", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Ordu", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Rize", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Sakarya", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Samsun", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Siirt", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Sinop", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Sivas", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Tekirdağ", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Tokat", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Trabzon", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Tunceli", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Şanlıurfa", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Uşak", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Van", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Yozgat", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Zonguldak", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Aksaray", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Bayburt", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Karaman", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kırıkkale", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Batman", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Şırnak", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Bartın", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Ardahan", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Iğdır", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Yalova", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Karabük", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Kilis", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Osmaniye", ["İlçe 1", "İlçe 2"])
        self.cityChoice.addItem("Düzce", ["İlçe 1", "İlçe 2"])

        self.districtChoice.addItem("Semt A")
        self.districtChoice.addItem("Semt B")
        self.districtChoice.addItem("Semt C")
        self.districtChoice.addItem("Semt D")
        self.districtChoice.addItem("Semt F")
        self.districtChoice.addItem("Semt E")

        self.label_9.hide()

        #SETTING RESTRICTIONS AND SLOT-SIGNALS

        class BigIntValidator(QtGui.QDoubleValidator):

            def __init__(self, bottom=float('-inf'), top=float('inf')):
                super(BigIntValidator, self).__init__(bottom, top, 0)
                self.setNotation(QtGui.QDoubleValidator.StandardNotation)

            def validate(self, text, pos):
                if text.endswith('.'):
                    return QtGui.QValidator.Invalid, text, pos
                return super(BigIntValidator, self).validate(text, pos)

        self.nameField.setMaxLength(200)
        self.ownerSSNField.setMaxLength(11)
        self.addressField.setMaxLength(400)
        self.ownerNameField.setMaxLength(100)
        self.ownerSurnameField.setMaxLength(100)
        self.phoneNumberField.setMaxLength(11)
        self.ownerPhoneNumberField.setMaxLength(11)
        self.emailField.setMaxLength(320)
        self.passwordField.setMaxLength(14)
        self.passwordConfirmation.setMaxLength(14)

        self.onlyInt = BigIntValidator()
        self.ownerSSNField.setValidator(self.onlyInt)
        self.phoneNumberField.setValidator(self.onlyInt)
        self.ownerPhoneNumberField.setValidator(self.onlyInt)

        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordConfirmation.setEchoMode(QtWidgets.QLineEdit.Password)

        self.registerButton.clicked.connect(lambda:self.register(MainWindow))
        
        ######

        self.cityChoice.currentIndexChanged.connect(self.cityChoiceIndexChanged)
        self.cityChoiceIndexChanged(self.cityChoice.currentIndex())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YemekSepeti"))
        self.label_5.setText(_translate("MainWindow", "Semt"))
        self.label_3.setText(_translate("MainWindow", "TCKN"))
        self.label_4.setText(_translate("MainWindow", "Restoran Adı"))
        self.label_2.setText(_translate("MainWindow", "İlçe"))
        self.label.setText(_translate("MainWindow", "Şehir"))
        self.label_6.setText(_translate("MainWindow", "Adres"))
        self.registerButton.setText(_translate("MainWindow", "Kayıt Ol"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Başarıyla Kayıt Oldunuz!</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Ad"))
        self.label_11.setText(_translate("MainWindow", "Soyad"))
        self.label_12.setText(_translate("MainWindow", "Restoran Sahibi Telefon No."))
        self.label_13.setText(_translate("MainWindow", "Restoran Telefon No."))
        self.label_14.setText(_translate("MainWindow", "E-Posta"))
        self.label_7.setText(_translate("MainWindow", "Şifre"))
        self.label_8.setText(_translate("MainWindow", "Şifre Tekrar"))

    def cityChoiceIndexChanged(self, index):
        self.townChoice.clear()
        data = self.cityChoice.itemData(index)
        if data is not None:
            self.townChoice.addItems(data)

    def register(self, MainWindow):
        register_form = {
            "email": self.emailField.text(),
            "name": self.nameField.text(),
            "owner_name": self.ownerNameField.text(),
            "owner_surname": self.ownerSurnameField.text(),
            "password": self.passwordField.text(),
            "password_confirmation": self.passwordConfirmation.text(),
            "city": str(self.cityChoice.currentText()),
            "town": str(self.townChoice.currentText()),
            "district": str(self.districtChoice.currentText()),
            "address": self.addressField.text(),
            "owner_ssn" : self.ownerSSNField.text(),
            "phone_number" : self.phoneNumberField.text(),
            "owner_phone_number": self.ownerPhoneNumberField.text(),
        }
        validation_context = util.validate_owner_register(register_form)
        self.label_9.show()
        self.label_9.setText(validation_context['message'])
        

        if validation_context['validated'] == True:
            try:
                util.save_restaurant(register_form)
                MainWindow.close()
                self.show_login_window()

            except sqlite3.OperationalError:
                util.create_tables()
                util.save_restaurant(register_form)
                MainWindow.close()
                self.show_login_window()

            except sqlite3.IntegrityError as e:
                if 'email' in e.__str__():
                    self.label_9.setText("<html><head/><body><p align=\"center\">Bu E-Posta ile Zaten Kayıt Olunmuş!</p></body></html>")
                elif 'name' in e.__str__():
                    self.label_9.setText("<html><head/><body><p align=\"center\">Bu İsimde Bir Restoran Zaten Var!</p></body></html>")
                elif 'phone_number' in e.__str__():
                    self.label_9.setText("<html><head/><body><p align=\"center\">Numarası Bu Olan Bir Restoran Zaten Var!</p></body></html>")
                self.label_9.show()

    def show_login_window(self):
        self.login_window = QtWidgets.QWidget()
        self.login_window_ui = LoginWindow()
        self.login_window_ui.setupUi(self.login_window)
        self.login_window.show()


class LoginWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(319, 211)
        Form.setMinimumSize(QtCore.QSize(319, 211))
        Form.setMaximumSize(QtCore.QSize(319, 211))
        self.emailField = QtWidgets.QLineEdit(Form)
        self.emailField.setGeometry(QtCore.QRect(100, 40, 150, 20))
        self.passwordField = QtWidgets.QLineEdit(Form)
        self.passwordField.setGeometry(QtCore.QRect(100, 90, 150, 20))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(117, 180, 91, 20))
        self.registerBtn = QtWidgets.QPushButton(Form)
        self.registerBtn.setGeometry(QtCore.QRect(160, 140, 141, 23))
        self.loginBtn = QtWidgets.QPushButton(Form)
        self.loginBtn.setGeometry(QtCore.QRect(10, 140, 141, 23))
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label.hide()
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)

        self.passwordField.setMaxLength(14)
        self.emailField.setMaxLength(320)

        self.registerBtn.clicked.connect(lambda:self.show_register_window(Form))
        self.loginBtn.clicked.connect(lambda:self.login(Form))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Hesap Bulunamadı!"))
        self.registerBtn.setText(_translate("Form", "Hesabın Yok Mu? Kayıt Ol"))
        self.loginBtn.setText(_translate("Form", "Giriş Yap"))
        self.label_3.setText(_translate("Form", "E-Posta"))
        self.label_4.setText(_translate("Form", "Şifre"))

    def show_register_window(self, Form):
        Form.close()
        self.register_window = QtWidgets.QMainWindow()
        self.register_window_ui = RegisterWindow()
        self.register_window_ui.setupUi(self.register_window)
        self.register_window.show()

    def login(self, Form):
        login_form = {
            "email": self.emailField.text(),
            "password": self.passwordField.text(),
        }
        restaurant_id = util.authenticate_owner(login_form)
        if restaurant_id == -1:
            self.label.show()
        else:
            self.show_main_window(restaurant_id)
            Form.close()

    def show_main_window(self, restaurant_id):
        self.main_window = QtWidgets.QMainWindow()
        self.main_window_ui = OwnerMainWindow()
        self.main_window_ui.setupUi(self.main_window, restaurant_id)
        self.main_window.show()


class OwnerMainWindow(object):
    def setupUi(self, MainWindow, restaurant_id):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 481)
        MainWindow.setMinimumSize(QtCore.QSize(800, 481))
        MainWindow.setMaximumSize(QtCore.QSize(800, 481))

        self.restaurant_id = restaurant_id

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, 0, 811, 471))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.newOrdersTab = QtWidgets.QWidget()
        self.newOrdersTable = QtWidgets.QTableWidget(self.newOrdersTab)
        self.newOrdersTable.setGeometry(QtCore.QRect(10, 0, 701, 431))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.newOrdersTable.setFont(font)
        self.newOrdersTable.setColumnCount(5)
        self.newOrdersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.newOrdersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.newOrdersTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.newOrdersTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.newOrdersTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.newOrdersTable.setHorizontalHeaderItem(4, item)
        self.newOrderDetailBtn = QtWidgets.QPushButton(self.newOrdersTab)
        self.newOrderDetailBtn.setGeometry(QtCore.QRect(717, 30, 75, 23))
        self.approveButton = QtWidgets.QPushButton(self.newOrdersTab)
        self.approveButton.setGeometry(QtCore.QRect(717, 80, 75, 23))
        self.deliveredButton = QtWidgets.QPushButton(self.newOrdersTab)
        self.deliveredButton.setGeometry(QtCore.QRect(717, 130, 75, 23))
        self.tabWidget.addTab(self.newOrdersTab, "")
        self.productsTab = QtWidgets.QWidget()
        self.productsTable = QtWidgets.QTableWidget(self.productsTab)
        self.productsTable.setGeometry(QtCore.QRect(10, 0, 701, 431))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.productsTable.setFont(font)
        self.productsTable.setColumnCount(4)
        self.productsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(3, item)
        self.newProductButton = QtWidgets.QPushButton(self.productsTab)
        self.newProductButton.setGeometry(QtCore.QRect(717, 30, 75, 23))
        self.editProductButton = QtWidgets.QPushButton(self.productsTab)
        self.editProductButton.setGeometry(QtCore.QRect(717, 80, 75, 23))
        self.deleteProductButton = QtWidgets.QPushButton(self.productsTab)
        self.deleteProductButton.setGeometry(QtCore.QRect(717, 130, 75, 23))
        self.tabWidget.addTab(self.productsTab, "")
        self.pastOrdersTab = QtWidgets.QWidget()
        self.pastOrdersTable = QtWidgets.QTableWidget(self.pastOrdersTab)
        self.pastOrdersTable.setGeometry(QtCore.QRect(10, 0, 701, 431))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.pastOrdersTable.setFont(font)
        self.pastOrdersTable.setColumnCount(4)
        self.pastOrdersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pastOrdersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pastOrdersTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pastOrdersTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pastOrdersTable.setHorizontalHeaderItem(3, item)
        self.pastOrderDetailBtn = QtWidgets.QPushButton(self.pastOrdersTab)
        self.pastOrderDetailBtn.setGeometry(QtCore.QRect(717, 30, 75, 23))
        self.tabWidget.addTab(self.pastOrdersTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_products_timer = QtCore.QTimer()
        self.load_products_timer.timeout.connect(self.load_products_to_table)

        self.newProductButton.clicked.connect(lambda:self.show_new_product_window(self.restaurant_id))
        self.deleteProductButton.clicked.connect(self.delete_products)
        self.editProductButton.clicked.connect(self.update_product)
        self.load_products_to_table()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YemekSepeti"))
        item = self.newOrdersTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.newOrdersTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tarih"))
        item = self.newOrdersTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ürünler"))
        item = self.newOrdersTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tutar"))
        item = self.newOrdersTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Durum"))
        self.newOrderDetailBtn.setText(_translate("MainWindow", "Detay"))
        self.approveButton.setText(_translate("MainWindow", "Onayla"))
        self.deliveredButton.setText(_translate("MainWindow", "Teslim Edildi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newOrdersTab), _translate("MainWindow", "Ana Sayfa"))
        item = self.productsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.productsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "İsim"))
        item = self.productsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fiyat"))
        item = self.productsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Detay"))
        self.newProductButton.setText(_translate("MainWindow", "Yeni Ürün"))
        self.editProductButton.setText(_translate("MainWindow", "Düzenle"))
        self.deleteProductButton.setText(_translate("MainWindow", "Sil"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.productsTab), _translate("MainWindow", "Ürünler"))
        item = self.pastOrdersTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.pastOrdersTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ürünler"))
        item = self.pastOrdersTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tutar"))
        item = self.pastOrdersTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Durum"))
        self.pastOrderDetailBtn.setText(_translate("MainWindow", "Detay"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pastOrdersTab), _translate("MainWindow", "Teslim Edilmiş Siparişler"))

    def show_new_product_window(self, restaurant_id):
        self.new_product_window = QtWidgets.QWidget()
        self.new_product_window_ui = NewProductWindow()
        self.new_product_window_ui.setupUi(self.new_product_window, restaurant_id, self.load_products_timer)
        self.new_product_window.show()

    def load_products_to_table(self):
        con = sqlite3.connect('database.db')
        cursor = con.cursor()
        query = 'SELECT id,name,price,description FROM Product WHERE restaurant_id=?'
        cursor.execute(query, (self.restaurant_id,))
        result = cursor.fetchall()
        self.productsTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        con.close()

    def delete_products(self):
        con = sqlite3.connect('database.db')
        cursor = con.cursor()

        rows = sorted(set(index.row() for index in self.productsTable.selectedIndexes()))
        products_to_delete = []

        for row in rows:
            product_id = self.productsTable.item(row, 0).text()
            products_to_delete.append(product_id)

        for product_id in products_to_delete:
            cursor.execute("DELETE FROM Product WHERE id = ?", (product_id,))

        con.commit()
        con.close()
        self.load_products_to_table()

    def update_product(self):
        rows = sorted(set(index.row() for index in self.productsTable.selectedIndexes()))
        if len(rows) != 1:
            return
        product_id = self.productsTable.item(rows[0], 0).text()
        self.show_product_detail(product_id)

    def show_product_detail(self, product_id):
        self.update_product_window = QtWidgets.QWidget()
        self.update_product_window_ui = UpdateProductWindow()
        self.update_product_window_ui.setupUi(self.update_product_window, product_id, self.load_products_timer)
        self.update_product_window.show()


class NewProductWindow(object):

    def setupUi(self, Form, restaurant_id, timer):
        Form.setObjectName("Form")
        Form.resize(248, 282)
        Form.setMinimumSize(QtCore.QSize(248, 282))
        Form.setMaximumSize(QtCore.QSize(248, 282))
        self.nameField = QtWidgets.QLineEdit(Form)
        self.nameField.setGeometry(QtCore.QRect(40, 50, 161, 20))
        self.descriptionField = QtWidgets.QLineEdit(Form)
        self.descriptionField.setGeometry(QtCore.QRect(40, 110, 161, 20))
        self.priceField = QtWidgets.QLineEdit(Form)
        self.priceField.setGeometry(QtCore.QRect(40, 170, 161, 20))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(37, 220, 75, 23))
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(127, 220, 75, 23))
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(22, 250, 201, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        self.restaurant_id = restaurant_id

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.only_float = QtGui.QDoubleValidator()
        self.priceField.setValidator(self.only_float)

        self.nameField.setMaxLength(200)
        self.descriptionField.setMaxLength(200)

        self.saveButton.clicked.connect(lambda:self.save(timer))
        self.cancelButton.clicked.connect(Form.close)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ürün Adı*"))
        self.label_2.setText(_translate("Form", "Ürün Açıklaması"))
        self.label_3.setText(_translate("Form", "Fiyat*"))
        self.saveButton.setText(_translate("Form", "Kaydet"))
        self.cancelButton.setText(_translate("Form", "İptal"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Bütün Zorunlu Alanları Doldurun!</p></body></html>"))

    def save(self, timer):
        product_name = self.nameField.text()
        product_description = self.descriptionField.text()
        product_price = self.priceField.text().replace(",",".")

        if len(product_price) == 0 or len(product_name) == 0:
            self.label_4.setText("<html><head/><body><p align=\"center\">Bütün Zorunlu Alanları Doldurun!</p></body></html>")
            self.label_4.show()
        else:
            try:
                util.save_product(product_name, product_description, float(product_price), self.restaurant_id)
                self.label_4.setText("<html><head/><body><p align=\"center\">Ürün Kaydedildi!</p></body></html>")
                timer.timeout.emit()
            except sqlite3.OperationalError:
                util.create_tables()
                util.save_product(product_name, product_description, float(product_price), self.restaurant_id)
                self.label_4.setText("<html><head/><body><p align=\"center\">Ürün Kaydedildi!</p></body></html>")
                timer.timeout.emit()
            except sqlite3.IntegrityError:
                self.label_4.setText("<html><head/><body><p align=\"center\">Bu İsme Sahip Bir Ürün Zaten Var!</p></body></html>")
            finally:
                self.label_4.show()


class UpdateProductWindow(object):

    def setupUi(self, Form, product_id, timer):
        Form.setObjectName("Form")
        Form.resize(248, 282)
        Form.setMinimumSize(QtCore.QSize(248, 282))
        Form.setMaximumSize(QtCore.QSize(248, 282))
        self.nameField = QtWidgets.QLineEdit(Form)
        self.nameField.setGeometry(QtCore.QRect(40, 50, 161, 20))
        self.descriptionField = QtWidgets.QLineEdit(Form)
        self.descriptionField.setGeometry(QtCore.QRect(40, 110, 161, 20))
        self.priceField = QtWidgets.QLineEdit(Form)
        self.priceField.setGeometry(QtCore.QRect(40, 170, 161, 20))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(37, 220, 75, 23))
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(127, 220, 75, 23))
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(22, 250, 201, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.hide()

        self.product_id = product_id

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.only_float = QtGui.QDoubleValidator()
        self.priceField.setValidator(self.only_float)

        self.nameField.setMaxLength(200)
        self.descriptionField.setMaxLength(200)

        self.saveButton.clicked.connect(lambda: self.update(timer))
        self.cancelButton.clicked.connect(Form.close)
        self.load_fields()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ürün Adı*"))
        self.label_2.setText(_translate("Form", "Ürün Açıklaması"))
        self.label_3.setText(_translate("Form", "Fiyat*"))
        self.saveButton.setText(_translate("Form", "Kaydet"))
        self.cancelButton.setText(_translate("Form", "İptal"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Bütün Zorunlu Alanları Doldurun!</p></body></html>"))

    def update(self, timer):
        product_name = self.nameField.text()
        product_description = self.descriptionField.text()
        product_price = self.priceField.text().replace(",", ".")

        if len(product_price) == 0 or len(product_name) == 0:
            self.label_4.setText("<html><head/><body><p align=\"center\">Bütün Zorunlu Alanları Doldurun!</p></body></html>")
            self.label_4.show()
        else:
            try:
                util.update_product(product_name, product_description, float(product_price), self.product_id)
                self.label_4.setText("<html><head/><body><p align=\"center\">Ürün Düzenlendi!</p></body></html>")
                timer.timeout.emit()
            except sqlite3.OperationalError:
                util.create_tables()
                util.update_product(product_name, product_description, float(product_price), self.product_id)
                self.label_4.setText("<html><head/><body><p align=\"center\">Ürün Düzenlendi!</p></body></html>")
                timer.timeout.emit()
            except sqlite3.IntegrityError:
                self.label_4.setText("<html><head/><body><p align=\"center\">Bu İsme Sahip Bir Ürün Zaten Var!</p></body></html>")
            finally:
                self.label_4.show()

    def load_fields(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        cursor.execute("SELECT id, name, price, description FROM Product WHERE id=?", (self.product_id,))
        result = list(cursor.fetchone())
        self.nameField.setText(result[1])
        self.descriptionField.setText(result[3])
        self.priceField.setText(str(result[2]).replace(".",","))
        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

