# Gerekli kütüphaneler
import psutil
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMessageBox,
    QFrame, QLineEdit, QPushButton, QWidget,
    QVBoxLayout, QProgressBar
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
        self.frame_name.setGeometry(150, 150, 120, 30)
        self.frame_name.setFrameShape(QFrame.Box)
        
        self.label_name = QLabel("İsminiz", self.frame_name)
        self.label_name.move(10, 5)
        
        self.frame_inputName = QLabel(self)
        self.frame_inputName.setGeometry(280, 150, 250, 30)
        self.frame_inputName.setFrameShape(QFrame.Box)
        
        self.input_name = QLineEdit(self.frame_inputName)
        self.input_name.move(5, 3)
        self.input_name.setFixedWidth(240)
        self.input_name.setPlaceholderText("İsminizi buraya yazınız!!!")
        
        self.frame_lastname = QFrame(self)
        self.frame_lastname.setGeometry(150, 200, 120, 30)
        self.frame_lastname.setFrameShape(QFrame.Box)
        
        self.label_lastname = QLabel("Soy isminiz", self.frame_lastname)
        self.label_lastname.move(10, 5)
        
        self.frame_inputLastname = QLabel(self)
        self.frame_inputLastname.setGeometry(280, 200, 250, 30)
        self.frame_inputLastname.setFrameShape(QFrame.Box)
        
        self.input_lastname = QLineEdit(self.frame_inputLastname)
        self.input_lastname.move(5, 3)
        self.input_lastname.setFixedWidth(240)
        self.input_lastname.setPlaceholderText("Soy isminizi buraya yazınız!!!")
        
        self.frame_eposta = QFrame(self)
        self.frame_eposta.setGeometry(150, 250, 120, 30)
        self.frame_eposta.setFrameShape(QFrame.Box)
        
        self.label_eposta = QLabel("E-postanız", self.frame_eposta)
        self.label_eposta.move(10, 5)
        
        self.frame_inputEposta = QLabel(self)
        self.frame_inputEposta.setGeometry(280, 250, 250, 30)
        self.frame_inputEposta.setFrameShape(QFrame.Box)
        
        self.input_eposta = QLineEdit(self.frame_inputEposta)
        self.input_eposta.move(5, 3)
        self.input_eposta.setFixedWidth(240)
        self.input_eposta.setPlaceholderText("E-postanızı buraya yazınız!!!")
        
        self.button = QPushButton("Giriş", self)
        self.button.setGeometry(200, 300, 300, 60)
        self.button.clicked.connect(self.girisDogulama)
        
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
                self.parent.appMain()
            QTimer.singleShot(5000, self.close)
        else:
            QMessageBox.information(self, "hatalı", "E-postanız kayıtlı değil")
            QTimer.singleShot(5000, self.close)
        
# Hesabı olmayan kullanıcının kayıt olmasını sağlayan pencere
class kayitPencresi(QWidget):
    def __init__(self):
        super(kayitPencresi, self).__init__()
        
        self.setWindowTitle("Kayıt Penceresi")
        self.setGeometry(100, 100, 150, 150)
        self.setWindowIcon(QIcon("AetAI.png"))
        self.initUI()
        
    def initUI(self):
        self.frm_name = QFrame(self)
        self.frm_name.setGeometry(150, 150, 120, 30)
        self.frm_name.setFrameShape(QFrame.Box)
        
        self.lbl_name = QLabel("İsminizi giriniz", self.frm_name)
        self.lbl_name.move(10, 5)
        
        self.frm_inputName = QLabel(self)
        self.frm_inputName.setGeometry(280, 150, 250, 30)
        self.frm_inputName.setFrameShape(QFrame.Box)
        
        self.inpt_name = QLineEdit(self.frm_inputName)
        self.inpt_name.move(5, 3)
        self.inpt_name.setFixedWidth(240)
        self.inpt_name.setPlaceholderText("İsminizi buraya giriniz!!!")
        
        self.frm_lastname = QFrame(self)
        self.frm_lastname.setGeometry(150, 200, 120, 30)
        self.frm_lastname.setFrameShape(QFrame.Box)
        
        self.lbl_lastname = QLabel("Soy isminiz", self.frm_lastname)
        self.lbl_lastname.move(10, 5)
        
        self.frm_inputLastname = QLabel(self)
        self.frm_inputLastname.setGeometry(280, 200, 250, 30)
        self.frm_inputLastname.setFrameShape(QFrame.Box)
        
        self.inpt_lastname = QLineEdit(self.frm_inputLastname)
        self.inpt_lastname.move(5, 3)
        self.inpt_lastname.setFixedWidth(240)
        self.inpt_lastname.setPlaceholderText("Soy isminizi buraya giriniz!!!")
        
        self.frm_eposta = QFrame(self)
        self.frm_eposta.setGeometry(150, 250, 120, 30)
        self.frm_eposta.setFrameShape(QFrame.Box)
        
        self.lbl_eposta = QLabel("E-postanız", self.frm_eposta)
        self.lbl_eposta.move(10, 5)
        
        self.frm_inputEposta = QLabel(self)
        self.frm_inputEposta.setGeometry(280, 250, 250, 30)
        self.frm_inputEposta.setFrameShape(QFrame.Box)
        
        self.inpt_eposta = QLineEdit(self.frm_inputEposta)
        self.inpt_eposta.move(5, 3)
        self.inpt_eposta.setFixedWidth(240)
        self.inpt_eposta.setPlaceholderText("E-postanızı buraya giriniz!!!")
        
        self.button = QPushButton("Kayıt ol", self)
        self.button.setGeometry()
        self.button.clicked.connect(self.kayitDogrulama)
        
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
        with open("Users.txt", "a", encoding="utf-8") as dosya:
            dosya.write(eposta + "\n")
            QMessageBox.information(self, "başarılı", "Kaydınız başarıyla gerçekleşti")

class AetherAIApp(QMainWindow): # Main class
    def __init__(self):
        super(AetherAIApp, self).__init__()

        self.setWindowTitle("Aet AI")
        self.setGeometry(200, 200, 700, 700)
        self.setToolTip("AetherAI")
        self.setWindowIcon(QIcon("logo.png"))
        self.initUI()
        
    def initUI(self):
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
            self.girisPenceresi = girisPenceresi()
            self.girisPenceresi.show()
        except Exception as e:
            print(e)
    
    def kayitOl(self):
        try:
            self.kayitPencresi = kayitPencresi()
            self.kayitPencresi.show()
        except Exception as e:
            print(e)
        
    def appMain(self):
        if self.centralWidget():
            self.centralWidget().deleteLater()
        
        self.main_widget = QWidget()
        self.layout = QVBoxLayout()
        
        self.cpu_button = QPushButton("CPU Kontrolü", self)
        self.cpu_button.setIcon(QIcon())
        self.cpu_button.setGeometry(100, 100, 100, 50)
        self.cpu_button.clicked.connect(self.cpu_kontrolü)
        
        self.ram_button = QPushButton("RAM Kontolü", self)
        self.ram_button.setIcon(QIcon())
        self.ram_button.setGeometry(100, 100, 100, 50)
        self.ram_button.clicked.connect(self.ram_kontrolü)
        
        self.layout.addWidget(self.cpu_button)
        self.layout.addWidget(self.ram_button)
        
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        
    def cpu_kontrolü(self):
        self.kontrolEtCPU = controlOfCPU()
        self.kontrolEtCPU.show()
        
    def ram_kontrolü(self):
        self.kontrolEtRAM = controlOfRAM()
        self.kontrolEtRAM.show()
        
def ilkKullaniciyiEkle():
    isim = "Muhammet"
    soyisim = "Kaya"
    eposta = "owdhklawj@uweıo"
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
