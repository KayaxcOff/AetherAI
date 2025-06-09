import psutil
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMessageBox,
    QFrame, QLineEdit, QPushButton, QWidget,
    QVBoxLayout, QProgressBar, QHBoxLayout
    )
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import time

class controlOfCPU(QWidget):
    
    def __init__(self):
        super(controlOfCPU, self).__init__()
        
        self.setWindowTitle("CPU Kontrolü")
        self.setGeometry(200, 200, 300, 200)
        self.setWindowIcon(QIcon("AetAI.png"))
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.label = QLabel("Anlık CPU kullanımı (%)", self)
        layout.addLayout(self.label)
        
        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        layout.addWidget(self.progressBar)

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.guncelleCPU)
        self.timer.start(1000)

    def guncelleCPU(self):
        cpu_kullanim = psutil.cpu_percent(interval=0.1)
        self.progressBar.setValue(cpu_kullanim)
        self.label.setText(f"Anlık CPU Kullanımı: %{cpu_kullanim}")
        
class controlOfRAM(QWidget):
    def __init__(self):
        pass
    
    def initUI(self):
        pass

class girisPenceresi(QWidget):
    def __init__(self, parent=None):
        super(girisPenceresi, self).__init__(parent)
        self.parent = parent
        
        self.setWindowTitle("Giriş Penceresi")
        self.setGeometry(400, 400, 500, 500)
        self.setWindowIcon(QIcon("AetAI.png"))
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.frame_name = QFrame(self)
        self.frame_name.setFrameShape(QFrame.Box)
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("İsminiz"))
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("İsminizi buraya yazınız!!!")
        name_layout.addWidget(self.input_name)
        self.frame_name.setLayout(name_layout)
        layout.addWidget(self.frame_name)

        self.frame_lastname = QFrame(self)
        self.frame_lastname.setFrameShape(QFrame.Box)
        lastname_layout = QHBoxLayout()
        lastname_layout.addWidget(QLabel("Soy isminiz"))
        self.input_lastname = QLineEdit()
        self.input_lastname.setPlaceholderText("Soy isminizi buraya yazınız!!!")
        lastname_layout.addWidget(self.input_lastname)
        self.frame_lastname.setLayout(lastname_layout)
        layout.addWidget(self.frame_lastname)

        self.frame_eposta = QFrame(self)
        self.frame_eposta.setFrameShape(QFrame.Box)
        eposta_layout = QHBoxLayout()
        eposta_layout.addWidget(QLabel("E-postanız"))
        self.input_eposta = QLineEdit()
        self.input_eposta.setPlaceholderText("E-postanızı buraya yazınız!!!")
        eposta_layout.addWidget(self.input_eposta)
        self.frame_eposta.setLayout(eposta_layout)
        layout.addWidget(self.frame_eposta)

        self.button = QPushButton("Giriş", self)
        self.button.clicked.connect(self.girisDogulama)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
    def girisDogulama(self):
        eposta = self.input_eposta.text()
        bulundu = False
        with open("Users.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                if eposta in satir:
                    bulundu = True
                    break
                
        if bulundu:
            QMessageBox.information(self, "başarılı", "Giriş yapabilirsiniz")
            if self.parent:
                self.parent.setAuthenticated(True)  # Bayrağı güncelle
            QTimer.singleShot(5000, self.close)
        else:
            QMessageBox.information(self, "hatalı", "E-postanız kayıtlı değil")
            QTimer.singleShot(5000, self.close)
        
class kayitPenceresi(QWidget):
    def __init__(self, parent=None):
        super(kayitPenceresi, self).__init__(parent)
        self.parent = parent
        
        self.setWindowTitle("Kayıt Penceresi")
        self.setGeometry(100, 100, 150, 150)
        self.setWindowIcon(QIcon("AetAI.png"))
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.frm_name = QFrame(self)
        self.frm_name.setFrameShape(QFrame.Box)
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("İsminizi giriniz"))
        self.inpt_name = QLineEdit()
        self.inpt_name.setPlaceholderText("İsminizi buraya giriniz!!!")
        name_layout.addWidget(self.inpt_name)
        self.frm_name.setLayout(name_layout)
        layout.addWidget(self.frm_name)

        self.frm_lastname = QFrame(self)
        self.frm_lastname.setFrameShape(QFrame.Box)
        lastname_layout = QHBoxLayout()
        lastname_layout.addWidget(QLabel("Soy isminiz"))
        self.inpt_lastname = QLineEdit()
        self.inpt_lastname.setPlaceholderText("Soy isminizi buraya giriniz!!!")
        lastname_layout.addWidget(self.inpt_lastname)
        self.frm_lastname.setLayout(lastname_layout)
        layout.addWidget(self.frm_lastname)

        self.frm_eposta = QFrame(self)
        self.frm_eposta.setFrameShape(QFrame.Box)
        eposta_layout = QHBoxLayout()
        eposta_layout.addWidget(QLabel("E-postanız"))
        self.inpt_eposta = QLineEdit()
        self.inpt_eposta.setPlaceholderText("E-postanızı buraya giriniz!!!")
        eposta_layout.addWidget(self.inpt_eposta)
        self.frm_eposta.setLayout(eposta_layout)
        layout.addWidget(self.frm_eposta)

        self.button = QPushButton("Kayıt ol", self)
        self.button.clicked.connect(self.kayitDogrulama)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
    def kayitDogrulama(self):
        eposta = self.inpt_eposta.text()
        bulundu = False
        with open("Users.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                if eposta in satir:
                    bulundu = True
                    break   
            if bulundu:
                QMessageBox.information(self, "kayıtlı", "E-postanız zaten kayıtlı")    
            else:
                with open("Users.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(eposta + "\n")
                    QMessageBox.information(self, "başarılı", "Kaydınız başarıyla gerçekleşti")
                    if self.parent:
                        self.parent.setAuthenticated(True)  # Bayrağı güncelle
        QTimer.singleShot(5000, self.close)

class AetherAIApp(QMainWindow):
    def __init__(self):
        super(AetherAIApp, self).__init__()
        self.isAuthenticated = False  # Giriş/kayıt durumu bayrağı

        self.setWindowTitle("Aet AI")
        self.setGeometry(200, 200, 700, 700)
        self.setToolTip("AetherAI")
        self.setWindowIcon(QIcon("logo.png"))
        self.initUI()
        
    def initUI(self):
        if self.centralWidget():
            self.centralWidget().deleteLater()
            
        if self.isAuthenticated:
            self.appMain()
        else:
            self.central_widget = QWidget(self)
            self.layout = QVBoxLayout()
            
            self.loginButton = QPushButton("Giriş yap", self)
            self.loginButton.setIcon(QIcon("girisYap.png"))
            self.loginButton.setGeometry(150, 350, 120, 40)
            self.loginButton.clicked.connect(self.girisYap)
            
            self.signUpButton = QPushButton("Kayıt ol", self)
            self.signUpButton.setIcon(QIcon("kayitOL.png"))
            self.signUpButton.setGeometry(300, 350, 120, 40)
            self.signUpButton.clicked.connect(self.kayitOl)
            
            self.layout.addWidget(self.loginButton)
            self.layout.addWidget(self.signUpButton)
            self.central_widget.setLayout(self.layout)
            self.setCentralWidget(self.central_widget)
        
    def girisYap(self):
        try:
            self.girisPenceresi = girisPenceresi(self)  # Ayrı bir pencere olarak
            self.girisPenceresi.show()
        except Exception as e:
            print(e)
    
    def kayitOl(self):
        try:
            self.kayitPenceresi = kayitPenceresi(self)  # Ayrı bir pencere olarak
            self.kayitPenceresi.show()
        except Exception as e:
            print(e)
        
    def appMain(self):
        if self.centralWidget():
            self.centralWidget().deleteLater()
        
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout()
        
        self.cpu_button = QPushButton("CPU Kontrolü", self)
        self.cpu_button.setGeometry(100, 100, 100, 50)
        self.cpu_button.clicked.connect(self.cpu_kontrolü)
        
        self.ram_button = QPushButton("RAM Kontrolü", self)
        self.ram_button.setGeometry(200, 100, 100, 50)
        self.ram_button.clicked.connect(self.ram_kontrolü)
        
        self.layout.addWidget(self.cpu_button)
        self.layout.addWidget(self.ram_button)
        
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        
    def setAuthenticated(self, value):
        self.isAuthenticated = value
        self.initUI()  # Bayrak değiştiğinde arayüzü yeniden yükle

    def cpu_kontrolü(self):
        self.kontrolEtCPU = controlOfCPU()
        self.kontrolEtCPU.show()
        
    def ram_kontrolü(self):
        self.kontrolEtRAM = controlOfRAM()
        self.kontrolEtRAM.show()
        
def ilkKullaniciyiEkle():
    isim = "Muhammet"
    soyisim = "Kaya"
    eposta = "muham123cak@gmail.com"
    satir = f"{isim},{soyisim},{eposta}\n"
    
    try:
        with open("Users.txt", "r", encoding="utf-8") as dosya:
            for mevcut in dosya:
                if eposta in mevcut:
                    print("İlk kullanıcı zaten kayıtlı.")
                    return
    except FileNotFoundError:
        pass  # Dosya yoksa yazmaya geç

    with open("Users.txt", "a", encoding="utf-8") as dosya:
        dosya.write(satir)
        print("İlk kullanıcı başarıyla eklendi.")
    
def openWindow():
    app = QApplication(sys.argv)
    window = AetherAIApp()
    window.show()
    sys.exit(app.exec_())

ilkKullaniciyiEkle()
openWindow()
