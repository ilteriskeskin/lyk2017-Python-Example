import sys
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi


class Pencere(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("ui/main.ui", self)
        self.kaydet.clicked.connect(self.button_action)
        self.json_file = "kisiler.json"
        self.kullanici_listesi.setColumnCount(2)
        self.kullaniciListesi()

    def kullaniciListesi(self):
        try:
            kisiler = json.load(open(self.json_file, "r"))

        except:
            kisiler = []

        self.kullanici_listesi.clearContents()
        self.kullanici_listesi.setRowCount(len(kisiler))

        satir = 0
        for kisi in kisiler:
            telefon = QTableWidgetItem(kisi.get("telefon"))
            isim = QTableWidgetItem(kisi.get("isim"))
            self.kullanici_listesi.setItem(satir, 0, isim)
            self.kullanici_listesi.setItem(satir, 1, telefon)
            satir += 1

    def button_action(self):
        try:
            kisiler = json.load(open(self.json_file, "r"))

        except:
            kisiler = []

        kisiler.append({"isim": self.isim.text(), "telefon":self.telefon.text()})
        open(self.json_file, "w+").write(json.dumps(kisiler))
        self.kullaniciListesi()

if __name__ == '__main__':
    app = QApplication([])
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())