import  sys
import time
from PyQt5 import  QtWidgets
import smtplib  # smtplib modulunu projemize ekledik

class Mail(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.gorsel()

    def gorsel(self):
        self.email = QtWidgets.QLabel("Kullanıcı Email :")
        self.sifre = QtWidgets.QLabel("Kullanıcı Şifre :")
        self.alici_mail = QtWidgets.QLabel("Alıcı Email :")
        self.konu_basligi =QtWidgets.QLabel("Konu Başlığı   :")
        self.mesajiniz =QtWidgets.QLabel("           Mesaj :")


        self.mailim = QtWidgets.QLineEdit()
        self.sifrem = QtWidgets.QLineEdit()
        self.sifrem.setEchoMode(QtWidgets.QLineEdit.Password)
        self.alici = QtWidgets.QLineEdit()
        self.gonder = QtWidgets.QPushButton("Gönder")
        self.konu = QtWidgets.QLineEdit()
        self.mesaj =QtWidgets.QLineEdit()
        self.cevap = QtWidgets.QLabel("")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.email)
        h_box1.addWidget(self.mailim)
        h_box1.addStretch()

        h_box2 =QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.sifre)
        h_box2.addWidget(self.sifrem)
        h_box2.addStretch()

        h_box7=QtWidgets.QHBoxLayout()
        h_box7.addStretch()
        h_box7.addWidget(self.alici_mail)
        h_box7.addWidget(self.alici)
        h_box7.addStretch()


        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.konu_basligi)
        h_box3.addWidget(self.konu)
        h_box3.addStretch()

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.mesajiniz)
        h_box4.addWidget(self.mesaj)
        h_box4.addStretch()

        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.cevap)
        h_box5.addStretch()

        h_box6 = QtWidgets.QHBoxLayout()
        h_box6.addStretch()
        h_box6.addWidget(self.gonder)



        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box7)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)
        v_box.addStretch()
        v_box.addLayout(h_box6)






        self.email.setFixedSize(70,20)
        self.mailim.setFixedSize(150,20)
        
        self.alici_mail.setFixedSize(70, 20)
        self.alici.setFixedSize(150, 20)
        self.konu_basligi.setFixedSize(70, 20)
        self.konu.setFixedSize(150, 20)
        self.mesajiniz.setFixedSize(70, 20)
        self.mesaj.setFixedSize(150, 100)
        self.setLayout(v_box)

        self.gonder.clicked.connect(self.kontrol)

        self.setWindowTitle("Gmail Gönderme")
        self.setFixedSize(350,350)
        self.setStyleSheet("background-color:lightblue")

        self.show()
    def kontrol(self):
        self.email_text = """
        From: {}
        To: {}
        Subject: {}
        {}
        """.format(self.mailim.text(), self.alici.text(), self.konu.text(), self.mesaj.text())

        try:
            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik

            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık

            server.login(self.mailim.text(), self.sifrem.text())  # Gmail SMTP server'ına giriş yaptık

            server.sendmail(self.mailim.text(),self.alici.text(), self.email_text)  # Mail'imizi gönderdik

            server.close()  # SMTP serverimizi kapattık
            self.cevap.setText("Gönderiliyor")
            time.sleep(3)
            self.cevap.setText("mail gönderildi")

        except:
            self.cevap.setText("Gönderiliyor")
            time.sleep(3)
            self.cevap.setText("hata oluştu")




if __name__== '__main__':
    uygulama = QtWidgets.QApplication(sys.argv)
    mail = Mail()
    sys.exit(uygulama.exec_())

