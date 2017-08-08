#AeO UYGULAMASI

class Birim:
    def __init__(self, insan):
        self.insan = insan

    def hareket_et(self):
        secim = input("Hareket edecek birimi seçiniz: (a/i)")
        if secim == 'a':
            print("Askerler hareket etmeye başladı.")
        elif secim == 'i':
            print("İşçiler hareket etmee başladı.")

    def calis(self):
        print("İşciler çalışmaya başladı.")

    def saldir(self):
        print("Askerler saldırmaya başladı.")

    def savunma(self):
        print("Askerler savunmaya başladı.")

class Isci(Birim):
    def __init__(self, isci):
        super(Isci, self).__init__()
        self.isci = isci

class Asker(Birim):
    def __init__(self, asker):
        super(Asker, self).__init__()
        self.asker = asker

class Bina:
    def __init__(self, bina):
        self.bina = bina

    def olustur(self):
        secim = input("İnşaa edilecek bina türünü seçiniz: (a/k/m)")
        if secim == 'a':
            print("Ambar inşaa edilmeye başlandı.")
        elif secim == 'k':
            print("Kışla edilmeye başlandı.")
        elif secim == 'm':
            print("Merkez binası inşaa edilmeye başlandı.")

    def yemek_uret(self):
        print("Yemek üretimine başlandı...")
        print("Yemek üretimi tamamlandı.")

    def asker_uret(self):
        print("Asker üretimine başlandı...")
        print("Asker üretimi tamamlandı.")

    def isci_uret(self):
        print("İşçi üretimine başlandı...")
        print("İşçi üretimi tamamlandı.")

class Ambar(Bina):
    def __init__(self):
        super(Ambar, self).__init__()

class Kisla(Bina):
    def __init__(self):
        super(Kisla, self).__init__()

class Merkez(Bina):
    def __init__(self):
        super(Merkez, self).__init__()

birim = Birim("birim")
bina = Bina("bina")

print("Seçim listesi: \n"
      "Birim:\n"
      "-->Hareket Et\n"
      "-->Asker\n"
      "-->İşçi\n"
      "Bina:\n"
      "-->Ambar\n"
      "-->Kışla\n"
      "-->Merkez\n")

secim = input("Yapmak istediğiniz seçimi giriniz: (Birim/Bina): ")

if secim == 'Birim':
    print("Birim içinde seçebilecekleriniz:\n"
          "-->Hareket Et\n"
          "-->Asker\n"
          "-->İşçi\n")

    secim = input("Yapmak istediğiniz seçimi giriniz: (Hareket/Asker/Isci): ")

    if secim == 'Hareket':
        birim.hareket_et()
    elif secim == 'Asker':
        secim = input("Askerlere ne yaptırmak istediğinizi giriniz: (saldir/savun): ")
        if secim == 'saldir':
            birim.saldir()
        elif secim == 'savun':
            birim.savunma()
    elif secim == 'Isci':
        birim.calis()

elif secim == 'Bina':
    print("Bina kategorisinde seçebileekleriniz: \n"
          "Oluştur:\n"
          "-->Ambar\n"
          "-->Merkez\n"
          "-->Kışla\n")

    secim = input("Bir seçim yapınız: (olustur): ")

    if secim == 'olustur':
        print("Seçebileceğiniz binalar: \n"
              "-->Ambar\n"
              "-->Merkez\n"
              "-->Kışla\n")
        secim == input("Bir bina seçiniz: (ambar/merkez/kışla): ")

        if secim == 'ambar':
            bina.yemek_uret()
        elif secim == 'merkez':
            bina.isci_uret()
        elif secim == 'kışla':
            bina.asker_uret()


