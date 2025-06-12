# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 06:10:08 2025

@author: pikac
"""
# Gerekli kütüphaneler
import psutil
import sys
import os

# Güvenli encoding ayarı
try:
    # Windows için encoding ayarı
    if os.name == 'nt':  # Windows
        import locale
        try:
            locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
        except:
            try:
                locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
            except:
                pass
        
        # Windows console encoding
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        elif hasattr(sys.stdout, 'buffer'):
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
except Exception as e:
    print(f"Encoding ayarı yapılamadı: {e}")
    pass  # Encoding ayarı yapılamazsa devam et

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMessageBox,
    QFrame, QLineEdit, QPushButton, QWidget,
    QVBoxLayout, QProgressBar, QStackedWidget, QHBoxLayout
    )
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

class controlOfCPU(QWidget):
    
    def __init__(self):
        super(controlOfCPU, self).__init__()
        
        self.setWindowTitle("CPU Kontrolü")
        self.setGeometry(200, 200, 400, 150)
        try:
            self.setWindowIcon(QIcon("AetAI.png"))
        except:
            pass  # Icon dosyası yoksa devam et
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.label = QLabel("Anlık CPU kullanımı (%)", self)
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
        try:
            cpu_kullanim = psutil.cpu_percent(interval=0.1)
            self.progressBar.setValue(int(cpu_kullanim))
            self.label.setText(f"Anlık CPU Kullanımı: %{cpu_kullanim:.1f}")
        except Exception as e:
            print(f"CPU güncellenirken hata: {e}")

class controlOfRAM(QWidget):
    def __init__(self):
        super(controlOfRAM, self).__init__()
        
        self.setWindowTitle("RAM Kontrolü")
        self.setGeometry(200, 200, 400, 200)
        try:
            self.setWindowIcon(QIcon("AetAI.png"))
        except:
            pass  # Icon dosyası yoksa devam et
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        # RAM kullanımı etiketi
        self.label_usage = QLabel("Anlık RAM kullanımı", self)
        layout.addWidget(self.label_usage)
        
        # RAM kullanım çubuğu
        self.progressBar_usage = QProgressBar(self)
        self.progressBar_usage.setMinimum(0)
        self.progressBar_usage.setMaximum(100)
        layout.addWidget(self.progressBar_usage)
        
        # RAM detay bilgileri
        self.label_total = QLabel("Toplam RAM: ", self)
        layout.addWidget(self.label_total)
        
        self.label_available = QLabel("Kullanılabilir RAM: ", self)
        layout.addWidget(self.label_available)
        
        self.label_used = QLabel("Kullanılan RAM: ", self)
        layout.addWidget(self.label_used)

        self.setLayout(layout)

        # Timer ile sürekli güncelleme
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.guncelleRAM)
        self.timer.start(1000)

    def guncelleRAM(self):
        try:
            # RAM bilgilerini al
            ram = psutil.virtual_memory()
            
            # Yüzdelik kullanım
            kullanim_yuzdesi = ram.percent
            self.progressBar_usage.setValue(int(kullanim_yuzdesi))
            self.label_usage.setText(f"Anlık RAM Kullanımı: %{kullanim_yuzdesi:.1f}")
            
            # GB cinsinden bilgiler
            total_gb = ram.total / (1024**3)
            available_gb = ram.available / (1024**3)
            used_gb = ram.used / (1024**3)
            
            self.label_total.setText(f"Toplam RAM: {total_gb:.2f} GB")
            self.label_available.setText(f"Kullanılabilir RAM: {available_gb:.2f} GB")
            self.label_used.setText(f"Kullanılan RAM: {used_gb:.2f} GB")
        except Exception as e:
            print(f"RAM güncellenirken hata: {e}")

class AetAIAppEN(QWidget):
    """English version fallback for Unicode issues"""
    def __init__(self):
        super(AetAIAppEN, self).__init__()
        self.setWindowTitle("AetAI - Main Application")
        self.setGeometry(400, 400, 500, 300)
        try:
            self.setWindowIcon(QIcon("AetAI.png"))
        except:
            pass
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        # Welcome message
        self.welcome_label = QLabel("Welcome to AetAI System Monitor!", self)
        self.welcome_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 20px;")
        layout.addWidget(self.welcome_label)
        
        # Button layout
        button_layout = QHBoxLayout()
        
        self.cpu_button = QPushButton("CPU Control", self)
        self.cpu_button.setMinimumSize(150, 50)
        self.cpu_button.clicked.connect(self.cpu_control)
        button_layout.addWidget(self.cpu_button)
        
        self.ram_button = QPushButton("RAM Control", self)
        self.ram_button.setMinimumSize(150, 50)
        self.ram_button.clicked.connect(self.ram_control)
        button_layout.addWidget(self.ram_button)
        
        layout.addLayout(button_layout)
        
        # Exit button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setMinimumSize(100, 30)
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)
        
        self.setLayout(layout)
        
        # Window references
        self.cpu_window = None
        self.ram_window = None
        
    def cpu_control(self):
        try:
            if self.cpu_window is None or not self.cpu_window.isVisible():
                self.cpu_window = controlOfCPU()
                self.cpu_window.show()
            else:
                self.cpu_window.raise_()
                self.cpu_window.activateWindow()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"CPU window error: {e}")
        
    def ram_control(self):
        try:
            if self.ram_window is None or not self.ram_window.isVisible():
                self.ram_window = controlOfRAM()
                self.ram_window.show()
            else:
                self.ram_window.raise_()
                self.ram_window.activateWindow()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"RAM window error: {e}")

class AetAIApp(QWidget):
    def __init__(self):
        super(AetAIApp, self).__init__()
        self.setWindowTitle("AetAI - Ana Uygulama")
        self.setGeometry(400, 400, 500, 300)
        try:
            self.setWindowIcon(QIcon("AetAI.png"))
        except:
            pass
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        # Hoş geldin mesajı
        self.welcome_label = QLabel("AetAI Sistem Monitörüne Hoş Geldiniz!", self)
        self.welcome_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 20px;")
        layout.addWidget(self.welcome_label)
        
        # Butonlar için horizontal layout
        button_layout = QHBoxLayout()
        
        self.cpu_button = QPushButton("CPU Kontrolü", self)
        self.cpu_button.setMinimumSize(150, 50)
        self.cpu_button.clicked.connect(self.cpu_kontrolü)
        button_layout.addWidget(self.cpu_button)
        
        self.ram_button = QPushButton("RAM Kontrolü", self)
        self.ram_button.setMinimumSize(150, 50)
        self.ram_button.clicked.connect(self.ram_kontrolü)
        button_layout.addWidget(self.ram_button)
        
        layout.addLayout(button_layout)
        
        # Çıkış butonu
        self.exit_button = QPushButton("Çıkış", self)
        self.exit_button.setMinimumSize(100, 30)
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)
        
        self.setLayout(layout)
        
        # CPU ve RAM pencere referansları
        self.cpu_window = None
        self.ram_window = None
        
    def cpu_kontrolü(self):
        try:
            if self.cpu_window is None or not self.cpu_window.isVisible():
                self.cpu_window = controlOfCPU()
                self.cpu_window.show()
            else:
                self.cpu_window.raise_()
                self.cpu_window.activateWindow()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"CPU penceresi açılırken hata: {e}")
        
    def ram_kontrolü(self):
        try:
            if self.ram_window is None or not self.ram_window.isVisible():
                self.ram_window = controlOfRAM()
                self.ram_window.show()
            else:
                self.ram_window.raise_()
                self.ram_window.activateWindow()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"RAM penceresi açılırken hata: {e}")

class girisPenceresi(QWidget):
    def __init__(self, parent=None):
        super(girisPenceresi, self).__init__()
        self.parent = parent
        
        self.setWindowTitle("Giriş Penceresi")
        self.setGeometry(400, 400, 550, 400)
        try:
            self.setWindowIcon(QIcon("AetAI.png"))
        except:
            pass
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Başlık
        title_label = QLabel("AetAI Giriş", self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        layout.addWidget(title_label)
        
        # İsim alanı
        name_layout = QHBoxLayout()
        name_label = QLabel("İsminiz:", self)
        name_label.setMinimumWidth(100)
        self.input_name = QLineEdit(self)
        self.input_name.setPlaceholderText("İsminizi buraya yazınız")
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.input_name)
        layout.addLayout(name_layout)
        
        # Soyisim alanı
        lastname_layout = QHBoxLayout()
        lastname_label = QLabel("Soy isminiz:", self)
        lastname_label.setMinimumWidth(100)
        self.input_lastname = QLineEdit(self)
        self.input_lastname.setPlaceholderText("Soy isminizi buraya yazınız")
        lastname_layout.addWidget(lastname_label)
        lastname_layout.addWidget(self.input_lastname)
        layout.addLayout(lastname_layout)
        
        # E-posta alanı
        email_layout = QHBoxLayout()
        email_label = QLabel("E-postanız:", self)
        email_label.setMinimumWidth(100)
        self.input_eposta = QLineEdit(self)
        self.input_eposta.setPlaceholderText("E-postanızı buraya yazınız")
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.input_eposta)
        layout.addLayout(email_layout)
        
        # Giriş butonu
        self.button = QPushButton("Giriş Yap", self)
        self.button.setMinimumSize(200, 40)
        self.button.clicked.connect(self.girisDogulama)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
    def girisDogulama(self):
        eposta = self.input_eposta.text().strip()
        
        if not eposta:
            QMessageBox.warning(self, "Uyarı", "Lütfen e-posta adresinizi giriniz!")
            return
            
        bulundu = False
        try:
            with open("Users.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if eposta in satir:
                        bulundu = True
                        break
        except FileNotFoundError:
            QMessageBox.warning(self, "Hata", "Kullanıcı dosyası bulunamadı!")
            return
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dosya okuma hatası: {e}")
            return
                
        if bulundu:
            QMessageBox.information(self, "Başarılı", "Giriş başarılı! Ana uygulamaya yönlendiriliyorsunuz...")
            if self.parent:
                self.parent.appMain()
            self.close()
        else:
            QMessageBox.warning(self, "Hatalı", "E-postanız kayıtlı değil! Lütfen önce kayıt olunuz.")

class kayitPencresi(QWidget):
    def __init__(self):
        super(kayitPencresi, self).__init__()
        
        self.setWindowTitle("Kayıt Penceresi")
        self.setGeometry(400, 400, 550, 400)
        try:
            self.setWindowIcon(QIcon("AetAI.png"))
        except:
            pass
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Başlık
        title_label = QLabel("AetAI Kayıt", self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        layout.addWidget(title_label)
        
        # İsim alanı
        name_layout = QHBoxLayout()
        name_label = QLabel("İsminiz:", self)
        name_label.setMinimumWidth(100)
        self.inpt_name = QLineEdit(self)
        self.inpt_name.setPlaceholderText("İsminizi buraya giriniz")
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.inpt_name)
        layout.addLayout(name_layout)
        
        # Soyisim alanı
        lastname_layout = QHBoxLayout()
        lastname_label = QLabel("Soy isminiz:", self)
        lastname_label.setMinimumWidth(100)
        self.inpt_lastname = QLineEdit(self)
        self.inpt_lastname.setPlaceholderText("Soy isminizi buraya giriniz")
        lastname_layout.addWidget(lastname_label)
        lastname_layout.addWidget(self.inpt_lastname)
        layout.addLayout(lastname_layout)
        
        # E-posta alanı
        email_layout = QHBoxLayout()
        email_label = QLabel("E-postanız:", self)
        email_label.setMinimumWidth(100)
        self.inpt_eposta = QLineEdit(self)
        self.inpt_eposta.setPlaceholderText("E-postanızı buraya giriniz")
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.inpt_eposta)
        layout.addLayout(email_layout)
        
        # Kayıt butonu
        self.button = QPushButton("Kayıt Ol", self)
        self.button.setMinimumSize(200, 40)
        self.button.clicked.connect(self.kayitDogrulama)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
    def kayitDogrulama(self):
        isim = self.inpt_name.text().strip()
        soyisim = self.inpt_lastname.text().strip()
        eposta = self.inpt_eposta.text().strip()
        
        if not all([isim, soyisim, eposta]):
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurunuz!")
            return
        
        # E-posta format kontrolü
        if "@" not in eposta or "." not in eposta:
            QMessageBox.warning(self, "Uyarı", "Lütfen geçerli bir e-posta adresi giriniz!")
            return
        
        bulundu = False
        try:
            with open("Users.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if eposta in satir:
                        bulundu = True
                        break   
        except FileNotFoundError:
            pass  # Dosya yoksa yaratılacak
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dosya okuma hatası: {e}")
            return
            
        if bulundu:
            QMessageBox.warning(self, "Kayıtlı", "E-postanız zaten kayıtlı!")
            return
        
        # Kayıt et
        try:
            with open("Users.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"{isim},{soyisim},{eposta}\n")
                QMessageBox.information(self, "Başarılı", "Kaydınız başarıyla gerçekleşti! Şimdi giriş yapabilirsiniz.")
                self.close()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Kayıt sırasında hata: {e}")

class AetherAIApp(QMainWindow):  # Main class
    def __init__(self):
        super(AetherAIApp, self).__init__()

        self.setWindowTitle("AetherAI")
        self.setGeometry(200, 200, 700, 500)
        self.setToolTip("AetherAI")
        try:
            self.setWindowIcon(QIcon("logo.png"))
        except:
            pass
        
        # Ana uygulama penceresi referansı
        self.main_app = None
        
        self.initUI()
        
    def initUI(self):
        # Ana widget ve layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout()
        
        # Başlık
        title_label = QLabel("AetherAI'ye Hoş Geldiniz", self.central_widget)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 40px;")
        layout.addWidget(title_label)
        
        # Açıklama
        desc_label = QLabel("Sistem monitöring uygulamasına erişmek için giriş yapın veya kayıt olun.", self.central_widget)
        desc_label.setStyleSheet("font-size: 14px; margin: 20px;")
        layout.addWidget(desc_label)
        
        # Butonlar için horizontal layout
        button_layout = QHBoxLayout()
        
        self.loginButton = QPushButton("Giriş Yap", self.central_widget)
        self.loginButton.setMinimumSize(150, 50)
        try:
            self.loginButton.setIcon(QIcon("girisYap.png"))
        except:
            pass
        self.loginButton.clicked.connect(self.girisYap)
        button_layout.addWidget(self.loginButton)
        
        self.signUpButton = QPushButton("Kayıt Ol", self.central_widget)
        self.signUpButton.setMinimumSize(150, 50)
        try:
            self.signUpButton.setIcon(QIcon("kayitOL.png"))
        except:
            pass
        self.signUpButton.clicked.connect(self.kayitOl)
        button_layout.addWidget(self.signUpButton)
        
        layout.addLayout(button_layout)
        
        self.central_widget.setLayout(layout)
        
    def girisYap(self):
        try:
            self.girisPenceresi = girisPenceresi(self)
            self.girisPenceresi.show()
            print("Giriş penceresi açıldı")  # Debug için
        except Exception as e:
            print(f"Giriş penceresi hatası: {e}")
            QMessageBox.critical(self, "Hata", f"Giriş penceresi açılırken hata oluştu: {e}")
    
    def kayitOl(self):
        try:
            self.kayitPencresi = kayitPencresi()
            self.kayitPencresi.show()
            print("Kayıt penceresi açıldı")  # Debug için
        except Exception as e:
            print(f"Kayıt penceresi hatası: {e}")
            QMessageBox.critical(self, "Hata", f"Kayıt penceresi açılırken hata oluştu: {e}")
    
    def appMain(self):
        """Başarılı girişten sonra ana uygulamayı göster"""
        try:
            print("Ana uygulama başlatılıyor...")  # Debug
            self.main_app = AetAIApp()
            print("Ana uygulama oluşturuldu")  # Debug
            self.main_app.show()
            print("Ana uygulama gösterildi")  # Debug
            self.hide()  # Ana pencereyi gizle
            print("Ana pencere gizlendi")  # Debug
        except UnicodeEncodeError as e:
            print(f"Unicode hatası: {e}")
            QMessageBox.information(self, "Bilgi", 
                               "Unicode karakter sorunu. Uygulama İngilizce modda açılacak.")
            # Fallback - İngilizce versiyonu aç
            self.main_app = AetAIAppEN()  # İngilizce versiyon
            self.main_app.show()
            self.hide()
        except Exception as e:
            print(f"Ana uygulama hatası: {e}")
            QMessageBox.critical(self, "Hata", f"Ana uygulama açılırken hata: {str(e)}")
        
def ilkKullaniciyiEkle():
    """İlk kullanıcıyı güvenli şekilde ekle"""
    isim = "Muhammet"
    soyisim = "Kaya"
    eposta = "dqkgwqwı@ulawe.dwjl"
    satir = f"{isim},{soyisim},{eposta}\n"
    
    try:
        # Önce dosyayı okumaya çalış
        with open("Users.txt", "r", encoding="utf-8") as dosya:
            for mevcut in dosya:
                if eposta in mevcut:
                    print("İlk kullanıcı zaten kayıtlı.")
                    return
    except FileNotFoundError:
        print("Users.txt dosyası bulunamadı, yeni dosya oluşturulacak.")
    except Exception as e:
        print(f"Dosya okuma hatası: {e}")
        return

    try:
        # Kullanıcıyı ekle
        with open("Users.txt", "a", encoding="utf-8") as dosya:
            dosya.write(satir)
            print("İlk kullanıcı başarıyla eklendi.")
    except Exception as e:
        print(f"Kullanıcı ekleme hatası: {e}")
    
def main():
    """Ana fonksiyon - uygulamayı başlat"""
    try:
        # Qt uygulaması için encoding ayarları
        if hasattr(sys, 'setdefaultencoding'):
            sys.setdefaultencoding('utf-8')
        
        app = QApplication(sys.argv)
        
        # Qt için encoding ayarı
        app.setApplicationName("AetherAI")
        
        # İlk kullanıcıyı ekle
        ilkKullaniciyiEkle()
        
        # Ana pencereyi başlat
        window = AetherAIApp()
        window.show()
        
        sys.exit(app.exec_())
        
    except Exception as e:
        print(f"Uygulama başlatılırken hata: {e}")
        input("Çıkmak için Enter'a basın...")

if __name__ == "__main__":
    main()
