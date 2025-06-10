# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 06:10:08 2025
@author: pikac
"""
# Gerekli kütüphaneler
import psutil
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMessageBox,
    QFrame, QLineEdit, QPushButton, QWidget,
    QVBoxLayout, QProgressBar, QStackedWidget
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt

class controlOfCPU(QWidget):
    def __init__(self):
        super(controlOfCPU, self).__init__()
        self.setWindowTitle("CPU Kontrolü".encode('utf-8').decode('utf-8'))
        self.setGeometry(200, 200, 300, 200)
        self.setWindowIcon(QIcon("AetAI.png"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel("Anlık CPU kullanımı (%)".encode('utf-8').decode('utf-8'), self)
        layout.addWidget(self.label)
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
        self.label.setText(f"Anlık CPU Kullanımı: %{cpu_kullanim}".encode('utf-8').decode('utf-8'))

class controlOfRAM(QWidget):
    def __init__(self):
        super(controlOfRAM, self).__init__()
        self.setWindowTitle("RAM Kontrolü".encode('utf-8').decode('utf-8'))
        self.setGeometry(200, 200, 300, 200)
        self.setWindowIcon(QIcon("AetAI.png"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel("Anlık RAM kullanımı (%)".encode('utf-8').decode('utf-8'), self)
        layout.addWidget(self.label)
        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        layout.addWidget(self.progressBar)
        self.setLayout(layout)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.guncelleRAM)
        self.timer.start(1000)

    def guncelleRAM(self):
        ram_kullanim = psutil.virtual_memory().percent
        self.progressBar.setValue(ram_kullanim)
        self.label.setText(f"Anlık RAM Kullanımı: %{ram_kullanim}".encode('utf-8').decode('utf-8'))

class girisPenceresi(QWidget):
    def __init__(self, parent=None):
        super(girisPenceresi, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("Giriş Penceresi".encode('utf-8').decode('utf-8'))
        self.setGeometry(400, 400, 500, 500)
        self.setWindowIcon(QIcon("AetAI.png"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.frame_name = QFrame(self)
        self.frame_name.setFrameShape(QFrame.Box)
        self.label_name = QLabel("İsminiz".encode('utf-8').decode('utf-8'), self.frame_name)
        self.label_name.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.frame_name)

        self.input_name = QLineEdit(self)
        self.input_name.setPlaceholderText("İsminizi buraya yazınız!!!".encode('utf-8').decode('utf-8'))
        layout.addWidget(self.input_name)

        self.frame_lastname = QFrame(self)
        self.frame_lastname.setFrameShape(QFrame.Box)
        self.label_lastname = QLabel("Soy isminiz".encode('utf-8').decode('utf-8'), self.frame_lastname)
        self.label_lastname.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.frame_lastname)

        self.input_lastname = QLineEdit(self)
        self.input_lastname.setPlaceholderText("Soy isminizi buraya yazınız!!!".encode('utf-8').decode('utf-8'))
        layout.addWidget(self.input_lastname)

        self.frame_eposta = QFrame(self)
        self.frame_eposta.setFrameShape(QFrame.Box)
        self.label_eposta = QLabel("E-postanız".encode('utf-8').decode('utf-8'), self.frame_eposta)
        self.label_eposta.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.frame_eposta)

        self.input_eposta = QLineEdit(self)
        self.input_eposta.setPlaceholderText("E-postanızı buraya yazınız!!!".encode('utf-8').decode('utf-8'))
        layout.addWidget(self.input_eposta)

        self.button = QPushButton("Giriş".encode('utf-8').decode('utf-8'), self)
        self.button.clicked.connect(self.girisDogulama)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def girisDogulama(self):
        eposta = self.input_eposta.text().strip()
        bulundu = False
        try:
            with open("Users.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if eposta in satir.strip():
                        bulundu = True
                        break
        except FileNotFoundError:
            QMessageBox.critical(self, "Hata".encode('utf-8').decode('utf-8'), "Users.txt dosyası bulunamadı.".encode('utf-8').decode('utf-8'))
            return

        if bulundu:
            QMessageBox.information(self, "Başarılı".encode('utf-8').decode('utf-8'), "Giriş yapabilirsiniz".encode('utf-8').decode('utf-8'))
            if self.parent:
                self.parent.appMain()
            self.close()
        else:
            QMessageBox.warning(self, "Hatalı".encode('utf-8').decode('utf-8'), "E-postanız kayıtlı değil".encode('utf-8').decode('utf-8'))
            QTimer.singleShot(5000, self.close)

class kayitPenceresi(QWidget):
    def __init__(self, parent=None):
        super(kayitPenceresi, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("Kayıt Penceresi".encode('utf-8').decode('utf-8'))
        self.setGeometry(100, 100, 500, 500)
        self.setWindowIcon(QIcon("AetAI.png"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.frm_name = QFrame(self)
        self.frm_name.setFrameShape(QFrame.Box)
        self.lbl_name = QLabel("İsminizi giriniz".encode('utf-8').decode('utf-8'), self.frm_name)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.frm_name)

        self.inpt_name = QLineEdit(self)
        self.inpt_name.setPlaceholderText("İsminizi buraya giriniz!!!".encode('utf-8').decode('utf-8'))
        layout.addWidget(self.inpt_name)

        self.frm_lastname = QFrame(self)
        self.frm_lastname.setFrameShape(QFrame.Box)
        self.lbl_lastname = QLabel("Soy isminiz".encode('utf-8').decode('utf-8'), self.frm_lastname)
        self.lbl_lastname.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.frm_lastname)

        self.inpt_lastname = QLineEdit(self)
        self.inpt_lastname.setPlaceholderText("Soy isminizi buraya giriniz!!!".encode('utf-8').decode('utf-8'))
        layout.addWidget(self.inpt_lastname)

        self.frm_eposta = QFrame(self)
        self.frm_eposta.setFrameShape(QFrame.Box)
        self.lbl_eposta = QLabel("E-postanız".encode('utf-8').decode('utf-8'), self.frm_eposta)
        self.lbl_eposta.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.frm_eposta)

        self.inpt_eposta = QLineEdit(self)
        self.inpt_eposta.setPlaceholderText("E-postanızı buraya giriniz!!!".encode('utf-8').decode('utf-8'))
        layout.addWidget(self.inpt_eposta)

        self.button = QPushButton("Kayıt ol".encode('utf-8').decode('utf-8'), self)
        self.button.clicked.connect(self.kayitDogrulama)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def kayitDogrulama(self):
        eposta = self.inpt_eposta.text().strip()
        ad = self.inpt_name.text().strip()
        soyad = self.inpt_lastname.text().strip()

        if not eposta or not ad or not soyad:
            QMessageBox.warning(self, "Eksik Bilgi".encode('utf-8').decode('utf-8'), "Lütfen tüm alanları doldurunuz.".encode('utf-8').decode('utf-8'))
            return

        bulundu = False
        try:
            with open("Users.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if eposta in satir.strip():
                        bulundu = True
                        break
        except FileNotFoundError:
            pass

        if bulundu:
            QMessageBox.warning(self, "Kayıtlı".encode('utf-8').decode('utf-8'), "E-postanız zaten kayıtlı.".encode('utf-8').decode('utf-8'))
        else:
            try:
                with open("Users.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(f"{ad},{soyad},{eposta}\n")
                QMessageBox.information(self, "Başarılı".encode('utf-8').decode('utf-8'), "Kaydınız başarıyla gerçekleşti.".encode('utf-8').decode('utf-8'))
                if self.parent:
                    self.parent.appMain()
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Hata".encode('utf-8').decode('utf-8'), f"Kayıt sırasında bir hata oluştu: {e}".encode('utf-8').decode('utf-8'))

class AetherAIApp(QMainWindow):
    def __init__(self):
        super(AetherAIApp, self).__init__()
        self.setWindowTitle("Aet AI".encode('utf-8').decode('utf-8'))
        self.setGeometry(200, 200, 700, 700)
        self.setToolTip("AetherAI".encode('utf-8').decode('utf-8'))
        self.setWindowIcon(QIcon("logo.png"))
        self.initUI()

    def initUI(self):
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # İlk ekran (Giriş/Kayıt Ekranı)
        self.initial_screen = QWidget()
        initial_layout = QVBoxLayout()

        self.loginButton = QPushButton("Giriş yap".encode('utf-8').decode('utf-8'), self)
        self.loginButton.setIcon(QIcon("girisYap.png"))
        self.loginButton.clicked.connect(self.girisYap)

        self.signUpButton = QPushButton("Kayıt ol".encode('utf-8').decode('utf-8'), self)
        self.signUpButton.setIcon(QIcon("kayitOL.png"))
        self.signUpButton.clicked.connect(self.kayitOl)

        initial_layout.addStretch()
        initial_layout.addWidget(self.loginButton)
        initial_layout.addWidget(self.signUpButton)
        initial_layout.addStretch()

        self.initial_screen.setLayout(initial_layout)
        self.stacked_widget.addWidget(self.initial_screen)

        # İkinci ekran (Ana Uygulama Ekranı)
        self.main_screen = QWidget()
        main_layout = QVBoxLayout()

        self.cpu_button = QPushButton("CPU Kontrolü".encode('utf-8').decode('utf-8'), self)
        self.cpu_button.clicked.connect(self.cpu_kontrolü)

        self.ram_button = QPushButton("RAM Kontrolü".encode('utf-8').decode('utf-8'), self)
        self.ram_button.clicked.connect(self.ram_kontrolü)

        main_layout.addStretch()
        main_layout.addWidget(self.cpu_button)
        main_layout.addWidget(self.ram_button)
        main_layout.addStretch()

        self.main_screen.setLayout(main_layout)
        self.stacked_widget.addWidget(self.main_screen)

        # Başlangıçta ilk ekranı göster
        self.stacked_widget.setCurrentWidget(self.initial_screen)

    def girisYap(self):
        try:
            self.girisPenceresi = girisPenceresi(parent=self)
            self.girisPenceresi.show()
        except Exception as e:
            print(e)

    def kayitOl(self):
        try:
            self.kayitPenceresi = kayitPenceresi(parent=self)
            self.kayitPenceresi.show()
        except Exception as e:
            print(e)

    def appMain(self):
        self.stacked_widget.setCurrentWidget(self.main_screen)

    def cpu_kontrolü(self):
        self.kontrolEtCPU = controlOfCPU()
        self.kontrolEtCPU.show()

    def ram_kontrolü(self):
        self.kontrolEtRAM = controlOfRAM()
        self.kontrolEtRAM.show()

def ilkKullaniciyiEkle():
    isim = "Muhammet"
    soyisim = "Kaya"
    eposta = "qwklhklel@dlsl"
    satir = f"{isim},{soyisim},{eposta}\n"
    
    try:
        with open("Users.txt", "r", encoding="utf-8") as dosya:
            for mevcut in dosya:
                if eposta in mevcut.strip():
                    print("İlk kullanıcı zaten kayıtlı.")
                    return
    except FileNotFoundError:
        pass

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
