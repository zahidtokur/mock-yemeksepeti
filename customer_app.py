from PyQt5 import QtCore, QtGui, QtWidgets
import util
import sqlite3
from time import sleep

class LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 395)
        MainWindow.setMinimumSize(QtCore.QSize(590, 395))
        MainWindow.setMaximumSize(QtCore.QSize(850, 569))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 175, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 225, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 123, 70, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 77, 70, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.registerEmail = QtWidgets.QLineEdit(self.widget)
        self.registerEmail.setGeometry(QtCore.QRect(110, 20, 140, 24))

        self.registerPw = QtWidgets.QLineEdit(self.widget)
        self.registerPw.setGeometry(QtCore.QRect(110, 70, 140, 24))

        self.registerPwConfirm = QtWidgets.QLineEdit(self.widget)
        self.registerPwConfirm.setGeometry(QtCore.QRect(110, 120, 140, 24))

        self.registerName = QtWidgets.QLineEdit(self.widget)
        self.registerName.setGeometry(QtCore.QRect(110, 170, 140, 24))

        self.registerSurname = QtWidgets.QLineEdit(self.widget)
        self.registerSurname.setGeometry(QtCore.QRect(110, 220, 140, 24))

        self.registerButton = QtWidgets.QPushButton(self.widget)
        self.registerButton.setGeometry(QtCore.QRect(80, 290, 111, 41))

        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(30, 340, 211, 20))

        self.horizontalLayout.addWidget(self.widget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)

        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(110, 20, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)

        self.loginEmail = QtWidgets.QLineEdit(self.widget_2)
        self.loginEmail.setGeometry(QtCore.QRect(35, 60, 200, 24))

        self.loginPw = QtWidgets.QLineEdit(self.widget_2)
        self.loginPw.setGeometry(QtCore.QRect(35, 160, 200, 24))
        self.loginPw.setText("")

        self.loginButton = QtWidgets.QPushButton(self.widget_2)
        self.loginButton.setGeometry(QtCore.QRect(80, 290, 111, 41))

        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(116, 120, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)

        self.rememberMeCBox = QtWidgets.QCheckBox(self.widget_2)
        self.rememberMeCBox.setGeometry(QtCore.QRect(170, 230, 81, 17))

        self.keepSignedInCBox = QtWidgets.QCheckBox(self.widget_2)
        self.keepSignedInCBox.setGeometry(QtCore.QRect(30, 230, 121, 17))

        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        MainWindow.setStatusBar(self.statusbar)

        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(40, 340, 191, 20))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

 

        self.label_9.hide()
        self.label_10.hide()
        # SETTING RESTRICTIONS AND SLOT-SIGNALS

        self.registerButton.clicked.connect(self.register)
        self.loginButton.clicked.connect(lambda:self.login(MainWindow))

        self.registerName.setMaxLength(100)
        self.registerSurname.setMaxLength(100)
        self.registerPw.setMaxLength(14)
        self.registerPwConfirm.setMaxLength(14)
        self.registerEmail.setMaxLength(320)

        self.loginEmail.setMaxLength(320)
        self.loginPw.setMaxLength(14)

        self.registerPw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.registerPwConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPw.setEchoMode(QtWidgets.QLineEdit.Password)

        #####

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YemekSepeti"))
        self.label_5.setText(_translate("MainWindow", "Ad"))
        self.label_3.setText(_translate("MainWindow", "Soyad"))
        self.label_4.setText(_translate("MainWindow", "E-Posta"))
        self.label_2.setText(_translate("MainWindow", "Şifre Tekrar"))
        self.label.setText(_translate("MainWindow", "Şifre"))
        self.registerButton.setText(_translate("MainWindow", "Kayıt Ol"))
        self.label_7.setText(_translate("MainWindow", "E-Posta"))
        self.loginButton.setText(_translate("MainWindow", "Giriş Yap"))
        self.label_8.setText(_translate("MainWindow", "Şifre"))
        self.rememberMeCBox.setText(_translate("MainWindow", "Beni Hatırla"))
        self.keepSignedInCBox.setText(_translate("MainWindow", "Oturumumu açık tut"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Başarıyla Kayıt Oldunuz!</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hesap Bulunamadı!</p></body></html>"))

    def register(self):
        register_form = {
            "email" : self.registerEmail.text(),
            "name" : self.registerName.text(),
            "surname" : self.registerSurname.text(),
            "password" : self.registerPw.text(),
            "password_confirmation" : self.registerPwConfirm.text(),
        }
        validation_context = util.validate_user_register(register_form)
        self.label_9.setText("<html><head/><body><p align=\"center\">"+validation_context['message']+"</p></body></html>")
        self.label_9.show()
        
        if validation_context['validated'] == True:
            try:
                util.save_customer(register_form)
            except sqlite3.OperationalError:
                util.create_tables()
                util.save_customer(register_form)
            except sqlite3.IntegrityError:
                self.label_9.setText("<html><head/><body><p align=\"center\">Bu E-Posta ile Zaten Kayıt Olunmuş!</p></body></html>")

    def login(self, MainWindow):
        login_form = {
            "email" : self.loginEmail.text(),
            "password" : self.loginPw.text(),
        }
        user_id = util.authenticate_user(login_form)
        if user_id == -1:
            self.label_10.show()
            return
        self.show_main_window(user_id)
        MainWindow.close()

    def show_main_window(self, user_id):
        self.main_window = QtWidgets.QMainWindow()
        self.main_window_ui = CustomerMainWindow()
        self.main_window_ui.setupUi(self.main_window, user_id)
        self.main_window.show()


class CustomerMainWindow(object):
    def setupUi(self, MainWindow, user_id):
        MainWindow.resize(598, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 411))
        self.mainTab = QtWidgets.QWidget()
        self.mainListWidget = QtWidgets.QListWidget(self.mainTab)
        self.mainListWidget.setGeometry(QtCore.QRect(170, 30, 391, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mainListWidget.setFont(font)
        self.backButton = QtWidgets.QPushButton(self.mainTab)
        self.backButton.setGeometry(QtCore.QRect(468, 320, 75, 23))
        self.cityChoice = QtWidgets.QComboBox(self.mainTab)
        self.cityChoice.setGeometry(QtCore.QRect(20, 70, 120, 22))
        self.townChoice = QtWidgets.QComboBox(self.mainTab)
        self.townChoice.setGeometry(QtCore.QRect(20, 140, 120, 22))
        self.districtChoice = QtWidgets.QComboBox(self.mainTab)
        self.districtChoice.setGeometry(QtCore.QRect(20, 210, 120, 22))
        self.label = QtWidgets.QLabel(self.mainTab)
        self.label.setGeometry(QtCore.QRect(60, 40, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.mainTab)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.mainTab)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.searchButton = QtWidgets.QPushButton(self.mainTab)
        self.searchButton.setGeometry(QtCore.QRect(40, 260, 75, 23))
        self.tabWidget.addTab(self.mainTab, "")
        self.basketTab = QtWidgets.QWidget()
        self.basketTable = QtWidgets.QTableWidget(self.basketTab)
        self.basketTable.setGeometry(QtCore.QRect(40, 40, 511, 192))
        self.basketTable.setColumnCount(5)
        self.basketTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.basketTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.basketTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.basketTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.basketTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.basketTable.setHorizontalHeaderItem(4, item)
        self.removeProductButton = QtWidgets.QPushButton(self.basketTab)
        self.removeProductButton.setGeometry(QtCore.QRect(70, 310, 95, 23))
        self.confirmButton = QtWidgets.QPushButton(self.basketTab)
        self.confirmButton.setGeometry(QtCore.QRect(230, 310, 95, 23))
        self.label_4 = QtWidgets.QLabel(self.basketTab)
        self.label_4.setGeometry(QtCore.QRect(240, 250, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.totalPrice = QtWidgets.QLabel(self.basketTab)
        self.totalPrice.setGeometry(QtCore.QRect(240, 280, 71, 16))
        self.emptyBasketButton = QtWidgets.QPushButton(self.basketTab)
        self.emptyBasketButton.setGeometry(QtCore.QRect(390, 310, 95, 23))
        self.tabWidget.addTab(self.basketTab, "")
        self.addressTab = QtWidgets.QWidget()
        self.newAddressButton = QtWidgets.QPushButton(self.addressTab)
        self.newAddressButton.setGeometry(QtCore.QRect(450, 80, 111, 23))
        self.editAddressButton = QtWidgets.QPushButton(self.addressTab)
        self.editAddressButton.setGeometry(QtCore.QRect(450, 160, 111, 23))
        self.deleteAddressButton = QtWidgets.QPushButton(self.addressTab)
        self.deleteAddressButton.setGeometry(QtCore.QRect(454, 230, 101, 23))
        self.addressList = QtWidgets.QListWidget(self.addressTab)
        self.addressList.setGeometry(QtCore.QRect(35, 51, 401, 261))
        self.tabWidget.addTab(self.addressTab, "")
        MainWindow.setCentralWidget(self.centralwidget)

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

        self.user_id = user_id
        self.restaurants = []
        self.products = []
        self.addresses = []

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.cityChoice.currentIndexChanged.connect(self.cityChoiceIndexChanged)
        self.cityChoiceIndexChanged(self.cityChoice.currentIndex())

        self.searchButton.clicked.connect(self.load_restaurants)

        self.mainListWidget.itemDoubleClicked.connect(self.handle_double_click)

        self.backButton.hide()
        self.backButton.clicked.connect(self.load_restaurants)

        self.load_basket_timer = QtCore.QTimer()
        self.load_basket_timer.timeout.connect(self.load_basket)
        self.load_addresses_timer = QtCore.QTimer()
        self.load_addresses_timer.timeout.connect(self.load_addresses)


        self.emptyBasketButton.clicked.connect(self.empty_basket)
        self.removeProductButton.clicked.connect(self.remove_from_basket)

        self.newAddressButton.clicked.connect(lambda:self.show_address_window(self.load_addresses_timer))
        self.load_addresses()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Geri"))
        self.label.setText(_translate("MainWindow", "Şehir:"))
        self.label_2.setText(_translate("MainWindow", "İlçe:"))
        self.label_3.setText(_translate("MainWindow", "Semt:"))
        self.searchButton.setText(_translate("MainWindow", "Ara"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("MainWindow", "Restoran Ara"))
        item = self.basketTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.basketTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Adet"))
        item = self.basketTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ürün Adı"))
        item = self.basketTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Açıklama"))
        item = self.basketTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Toplam Tutar"))
        self.removeProductButton.setText(_translate("MainWindow", "Seçili Ürünü Kaldır"))
        self.confirmButton.setText(_translate("MainWindow", "Onayla"))
        self.label_4.setText(_translate("MainWindow", "Sepet Tutarı:"))
        self.totalPrice.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0 TL</p></body></html>"))
        self.emptyBasketButton.setText(_translate("MainWindow", "Sepeti Boşalt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.basketTab), _translate("MainWindow", "Sepetim"))
        self.newAddressButton.setText(_translate("MainWindow", "Adres Ekle"))
        self.editAddressButton.setText(_translate("MainWindow", "Seçili Adresi Düzenle"))
        self.deleteAddressButton.setText(_translate("MainWindow", "Sil"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addressTab), _translate("MainWindow", "Adreslerim"))

    def cityChoiceIndexChanged(self, index):
        self.townChoice.clear()
        data = self.cityChoice.itemData(index)
        if data is not None:
            self.townChoice.addItems(data)

    def load_restaurants(self):
        self.mainListWidget.clear()
        self.backButton.hide()
        city = self.cityChoice.currentText()
        town = self.townChoice.currentText()
        district = self.districtChoice.currentText()
        self.restaurants = util.find_restaurants(city, town, district)
        for data in self.restaurants:
            self.mainListWidget.addItem(list(data)[1])

    def handle_double_click(self):
        current_item = self.mainListWidget.currentItem()
        if current_item.text().endswith("TL"):
            current_index = self.mainListWidget.currentRow()
            product_details = list(self.products[current_index])
            self.add_to_basket_window = QtWidgets.QWidget()
            self.add_to_basket_window_ui = AddToBasketWindow()
            self.add_to_basket_window_ui.setupUi(self.add_to_basket_window, self.load_basket_timer, product_details[0], 
                                                    product_details[1], product_details[2], product_details[3])
            self.add_to_basket_window.show()

        else:
            current_index = self.mainListWidget.currentRow()
            restaurant_id = list(self.restaurants[current_index])[0]
            self.products = util.find_products(restaurant_id)
            self.mainListWidget.clear()
            for data in self.products:
                self.mainListWidget.addItem(list(data)[1] + " " + str(list(data)[2]) + " TL")
        
            self.backButton.show()

    def load_basket(self):
        con = sqlite3.connect('basket.db')
        cursor = con.cursor()
        query = 'SELECT product_id,piece,name,description,total_price FROM Basket'
        cursor.execute(query)
        result = cursor.fetchall()
        self.basketTable.setRowCount(0)
        count = 0
        for row_number, row_data in enumerate(result):
            self.basketTable.insertRow(row_number)
            count += 1
            for column_number, data in enumerate(row_data):
                self.basketTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        con.close()
        self.update_basket_tab_text(count)
        self.calculate_total_price()

    def calculate_total_price(self):
        price = 0
        for row in range(self.basketTable.rowCount()):
            price += float(self.basketTable.item(row, 4).text().replace(",","."))
        price = str(price).replace(".",",")
        self.totalPrice.setText("<html><head/><body><p align=\"center\">"+ price +" TL</p></body></html>")

    def empty_basket(self):
        util.empty_basket_db()
        self.load_basket()

    def remove_from_basket(self):
        con = sqlite3.connect('basket.db')
        cursor = con.cursor()

        rows = sorted(set(index.row()for index in self.basketTable.selectedIndexes()))
        products_to_delete = []

        for row in rows:
            product_id = self.basketTable.item(row, 0).text()
            products_to_delete.append(product_id)

        for product_id in products_to_delete:
            cursor.execute("DELETE FROM Basket WHERE product_id = ?", (product_id,))

        con.commit()
        con.close()
        self.load_basket()

    def update_basket_tab_text(self, count):
        if count > 0:
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.basketTab), "Sepetim(" +str(count)+ ")")
        else:
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.basketTab), "Sepetim")

    def show_address_window(self, timer, update=False, address_details=None):
        if not update:
            self.address_window = QtWidgets.QWidget()
            self.address_window_ui = AddressWindow()
            self.address_window_ui.setupUi(self.address_window, self.user_id, timer)
            self.address_window.show()

    def load_addresses(self):
        self.addressList.clear()
        self.addresses = util.find_addresses(self.user_id)
        for data in self.addresses:
            item = str(list(data)[5])[:30] + "... " + str(list(data)[3]) + "/" + str(list(data)[2])
            self.addressList.addItem(item)
            
        

class AddToBasketWindow(object):
    def setupUi(self, Form, timer, product_id, product_name, product_price, product_description):
        Form.resize(400, 164)
        Form.setMinimumSize(QtCore.QSize(400, 164))
        Form.setMaximumSize(QtCore.QSize(400, 164))
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setEnabled(True)
        self.name.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.name.setFrame(True)
        self.name.setReadOnly(True)
        self.description = QtWidgets.QLineEdit(Form)
        self.description.setGeometry(QtCore.QRect(20, 110, 113, 20))
        self.description.setReadOnly(True)
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setGeometry(QtCore.QRect(160, 50, 113, 20))
        self.price.setReadOnly(True)
        self.piece = QtWidgets.QSpinBox(Form)
        self.piece.setGeometry(QtCore.QRect(300, 50, 61, 22))
        self.piece.setProperty("value", 1)
        self.piece.setMinimum(1)
        self.addToBasketButton = QtWidgets.QPushButton(Form)
        self.addToBasketButton.setGeometry(QtCore.QRect(290, 105, 75, 23))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 90, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(310, 30, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.price_label = QtWidgets.QLabel(Form)
        self.price_label.setGeometry(QtCore.QRect(190, 110, 51, 16))

        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = float(str(product_price).replace(",","."))

        self.name.setText(self.product_name)
        self.description.setText(self.product_description)
        self.description.setCursorPosition(0)
        self.price.setText(str(self.product_price) + " TL")

        self.retranslateUi(Form)
        self.price_label.setText(str(self.product_price) + " TL")

        self.piece.valueChanged.connect(self.calculate_price)
        self.addToBasketButton.clicked.connect(lambda:self.addToBasket(Form, timer))

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addToBasketButton.setText(_translate("Form", "Sepete Ekle"))
        self.label.setText(_translate("Form", "Ürün:"))
        self.label_2.setText(_translate("Form", "Açıklama:"))
        self.label_3.setText(_translate("Form", "Fiyat:"))
        self.label_4.setText(_translate("Form", "Toplam Tutar:"))
        self.label_5.setText(_translate("Form", "Adet:"))
        self.price_label.setText(_translate("Form", "20.05 TL"))

    def calculate_price(self):
        new_price = self.product_price * self.piece.value()
        self.price_label.setText(str(new_price) + " TL")

    def addToBasket(self, Form, timer):
        con = sqlite3.connect('basket.db')
        cursor = con.cursor()
        values = (self.product_id, self.piece.value(), self.product_name, self.product_description, 
                  str(self.product_price * self.piece.value()).replace(".",","))

        cursor.execute("INSERT INTO Basket (product_id, piece, name, description, total_price) VALUES (?,?,?,?,?)", values)
        con.commit()
        con.close()        
        timer.timeout.emit()
        Form.close()


class AddressWindow(object):
    def setupUi(self, Form, user_id, timer, address_details=None):
        Form.resize(335, 407)
        Form.setMinimumSize(QtCore.QSize(335, 407))
        Form.setMaximumSize(QtCore.QSize(335, 407))
        self.phoneNumber = QtWidgets.QLineEdit(Form)
        self.phoneNumber.setGeometry(QtCore.QRect(70, 230, 180, 20))
        self.cityChoice = QtWidgets.QComboBox(Form)
        self.cityChoice.setGeometry(QtCore.QRect(110, 30, 100, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cityChoice.setFont(font)
        self.townChoice = QtWidgets.QComboBox(Form)
        self.townChoice.setGeometry(QtCore.QRect(110, 110, 100, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.townChoice.setFont(font)
        self.districtChoice = QtWidgets.QComboBox(Form)
        self.districtChoice.setGeometry(QtCore.QRect(110, 170, 100, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.districtChoice.setFont(font)
        self.address = QtWidgets.QLineEdit(Form)
        self.address.setGeometry(QtCore.QRect(10, 280, 141, 20))
        self.addressDescription = QtWidgets.QLineEdit(Form)
        self.addressDescription.setGeometry(QtCore.QRect(170, 280, 141, 20))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 200, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 140, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 260, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 370, 241, 20))
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(120, 340, 75, 23))

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

        self.cityChoice.currentIndexChanged.connect(self.cityChoiceIndexChanged)
        self.cityChoiceIndexChanged(self.cityChoice.currentIndex())

        class BigIntValidator(QtGui.QDoubleValidator):

            def __init__(self, bottom=float('-inf'), top=float('inf')):
                super(BigIntValidator, self).__init__(bottom, top, 0)
                self.setNotation(QtGui.QDoubleValidator.StandardNotation)

            def validate(self, text, pos):
                if text.endswith('.'):
                    return QtGui.QValidator.Invalid, text, pos
                return super(BigIntValidator, self).validate(text, pos)

        self.onlyInt = BigIntValidator()
        self.phoneNumber.setValidator(self.onlyInt)
        self.phoneNumber.setMaxLength(11)
        self.address.setMaxLength(300)
        self.addressDescription.setMaxLength(300)

        update = False

        if address_details != None:
            self.address_details = address_details
            update = True
        
        self.user_id = user_id
        self.timer = timer

        self.label_7.hide()

        self.saveButton.clicked.connect(lambda:self.save_or_update_address(update, Form))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Telefon Numarası:"))
        self.label_2.setText(_translate("Form", "Şehir:"))
        self.label_3.setText(_translate("Form", "İlçe:"))
        self.label_4.setText(_translate("Form", "Semt:"))
        self.label_5.setText(_translate("Form", "Adres Tarifi:"))
        self.label_6.setText(_translate("Form", "Adres:"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\">Bütün Alanlar Zorunludur</p></body></html>"))
        self.saveButton.setText(_translate("Form", "Kaydet"))

    def save_or_update_address(self, update, Form):
        address_form = {
            "phone_number": self.phoneNumber.text(),
            "city": str(self.cityChoice.currentText()),
            "town": str(self.townChoice.currentText()),
            "district": str(self.districtChoice.currentText()),
            "address": self.address.text(),
            "address_description": self.addressDescription.text(),
            "user_id": self.user_id
        }

        validation_context = util.validate_address(address_form)
        self.label_7.setText("<html><head/><body><p align=\"center\">" +validation_context['message']+ "</p></body></html>")
        self.label_7.show()

        if not update:
            if validation_context['validated'] == True:
                util.save_address(address_form)
                self.timer.timeout.emit()
                sleep(1)
                Form.close()


    def cityChoiceIndexChanged(self, index):
        self.townChoice.clear()
        data = self.cityChoice.itemData(index)
        if data is not None:
            self.townChoice.addItems(data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
