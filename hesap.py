from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
import sys


class Obje():
    def __init__(self):
        self.yazilacaklar = None
        self.islemler = []
        self.islem = []
        self.islem_alani = QLineEdit(self)


        self.sifir = QPushButton("0", self)
        self.bir = QPushButton("1", self)
        self.iki = QPushButton("2", self)
        self.uc = QPushButton("3", self)
        self.dort = QPushButton("4", self)
        self.bes = QPushButton("5", self)
        self.alti = QPushButton("6", self)
        self.yedi = QPushButton("7", self)
        self.sekiz = QPushButton("8", self)
        self.dokuz = QPushButton("9", self)


        self.virgul = QPushButton(",",self)
        self.isaret_degistir = QPushButton("", self)
        self.silme = QPushButton("<", self)
        self.butun_sil = QPushButton("C", self)

        self.arti = QPushButton("+",self)
        self.eksi = QPushButton("-", self)
        self.carpi = QPushButton("x", self)
        self.bolu = QPushButton("/", self)
        self.esittir = QPushButton("=",self)

        self.islemler = [self.arti, self.eksi,self.carpi, self.bolu]

        self.islem_alani.setGeometry(60,80,200,30)

        self.sifir.setGeometry(80,340,80,55)
        self.bir.setGeometry(0,285,80,55)
        self.iki.setGeometry(80,285,80,55)
        self.uc.setGeometry(160,285,80,55)
        self.dort.setGeometry(0,230,80,55)
        self.bes.setGeometry(80,230,80,55)
        self.alti.setGeometry(160,230,80,55)
        self.yedi.setGeometry(0,175,80,55)
        self.sekiz.setGeometry(80,175,80,55)
        self.dokuz.setGeometry(160,175,80,55)

        self.virgul.setGeometry(160,340,80,55)
        self.isaret_degistir.setGeometry(0,340,80,55)
        self.silme.setGeometry(160,120,80,55)
        self.butun_sil.setGeometry(80,120,80,55)

        self.bolu.setGeometry(240,120,80,55)
        self.carpi.setGeometry(240,175,80,55)
        self.eksi.setGeometry(240,230,80,55)
        self.arti.setGeometry(240,285,80,55)
        self.esittir.setGeometry(240,340,80,55)


        self.sifir.setStyleSheet("background-color: #ecf0f1")
        self.bir.setStyleSheet("background-color: #ecf0f1")
        self.iki.setStyleSheet("background-color: #ecf0f1")
        self.uc.setStyleSheet("background-color: #ecf0f1")
        self.dort.setStyleSheet("background-color: #ecf0f1")
        self.bes.setStyleSheet("background-color: #ecf0f1")
        self.alti.setStyleSheet("background-color: #ecf0f1")
        self.yedi.setStyleSheet("background-color: #ecf0f1")
        self.sekiz.setStyleSheet("background-color: #ecf0f1")
        self.dokuz.setStyleSheet("background-color: #ecf0f1")

        self.virgul.setStyleSheet("background-color: #ecf0f1")
        self.isaret_degistir.setStyleSheet("background-color: #ecf0f1")
        self.esittir.setStyleSheet("background-color: #3498db")




class Pencere(QWidget, Obje):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(959,141,318,400)

        self.sifir.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.bir.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.iki.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.uc.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.dort.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.bes.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.alti.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.yedi.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.sekiz.clicked.connect(lambda: self.yaz(tur = "sayi"))
        self.dokuz.clicked.connect(lambda: self.yaz(tur = "sayi"))

        self.arti.clicked.connect(lambda:self.yaz(tur = "islem"))
        self.eksi.clicked.connect(lambda:self.yaz(tur = "islem"))
        self.carpi.clicked.connect(lambda:self.yaz(tur = "islem"))
        self.bolu.clicked.connect(lambda:self.yaz(tur = "islem"))
        self.virgul.clicked.connect(lambda:self.yaz(tur = "islem"))

        self.esittir.clicked.connect(lambda:self.yaz(tur = "esittir"))
        self.silme.clicked.connect(lambda:self.yaz(tur = "yan"))
        self.butun_sil.clicked.connect(lambda:self.yaz(tur = "yan"))

        
        
        self.show()
    
    def yaz(self, tur):
        sender = self.sender()
        if tur == "sayi":
            self.yazilacaklar = self.islem_alani.text() + sender.text()
            self.islem_alani.setText(self.yazilacaklar)
        
        elif tur == "islem":
            self.yazilacaklar = self.islem_alani.text() + sender.text()
            self.islem_alani.setText(self.yazilacaklar)
            self.islem.append(sender.text())
        
        elif tur == "yan":
            if sender.text() == "<":
                self.yazilacaklar = self.islem_alani.text()[:-1]
                self.islem_alani.setText(self.yazilacaklar)
            
            elif sender.text() == "C":
                self.islem_alani.setText("")
            
        
        elif tur == "esittir":
            # for i in self.islem:
            #     self.islemler = self.yazilacaklar.split(i)
            

            for i in self.islem:
                if i == "+":
                    toplam = 0
                    self.islemler = self.yazilacaklar.split("+")
                    for j in self.islemler:
                        if "," in j:
                            self.virgullu = j.split(",")
                            bir = str(self.virgullu[0])
                            iki = str(self.virgullu[1])
                            j = float(bir + "." + iki)

                        try:
                            toplam += float(j)
                        except:
                            continue
                    self.islem_alani.setText(str(toplam))
                
                elif i == "-":
                    self.islemler = self.yazilacaklar.split("-")
                    for j in self.islemler[0]:
                        if "," in j:
                            self.virgullu = j.split(",")
                            bir = str(self.virgullu[0])
                            iki = str(self.virgullu[1])
                            birinci = float("0" + bir + "." + iki)
                        else:
                            birinci = j
                    for j in self.islemler[1:]:
                        if "," in j:
                            self.virgullu = j.split(",")
                            bir = str(self.virgullu[0])
                            iki = str(self.virgullu[1])
                            j = float(bir + "." + iki)
                            birinci = float(birinci)
                            
                            # try:
                            birinci -= j
                            # except:
                                # continue
                        else:
                            birinci = float(birinci)
                            # try:
                            birinci -= float(j)
                            # except:
                            #     continue
                        
                    self.islem_alani.setText(str(birinci))
                
                elif i == "x":
                    self.islemler = self.yazilacaklar.split("x")
                    carpim = 1
                    for j in self.islemler:
                        if "," in j:
                            self.virgullu = j.split(",")
                            bir = self.virgullu[0]
                            iki = self.virgullu[1]
                            j = float(self.virgullu[0] + "." + self.virgullu[1])
                            try:
                                carpim *= float(j)
                            except:
                                continue
                        
                        else:
                            # try:
                            carpim *= float(j)
                    
                    self.islem_alani.setText(str(carpim))
                
                elif i == "/":
                    self.islemler = self.yazilacaklar.split("/")
                    for j in self.islemler[0]:
                        if "," in j:
                            self.virgullu = j.split(",")
                            bir = str(self.virgullu[0])
                            iki = str(self.virgullu[1])
                            birinci = float("0" + bir + "." + iki)
                        else:
                            birinci = j
                    for j in self.islemler[1:]:
                        if "," in j:
                            self.virgullu = j.split(",")
                            bir = str(self.virgullu[0])
                            iki = str(self.virgullu[1])
                            j = float(bir + "." + iki)
                            birinci = float(birinci)
                            # try:
                            birinci /= float(j)
                        
                            # except:
                            #     continue
                        else:
                            birinci = float(birinci)
                            # try:
                            birinci /= float(j)
                            # except:
                            #     continue
                    
                    self.islem_alani.setText(str(birinci))
                    
                        

app = QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())



































