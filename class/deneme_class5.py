class Ders:
    def __init__(self, isim):
        self.isim = isim

class Ogrenci():
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        self.dersler = []

    def isim_soyisim(self):
        return self.isim + " " + self.soyisim


ogrenci_isim = input("Öğrenci adı giriniz: ")
ogrenci_soyisim = input("Öğrenci soyadı giriniz: ")

ogrenci = Ogrenci(ogrenci_isim, ogrenci_soyisim)

print("\n Alabileceğiniz dersler: Matematik, Fizik, Biyoloji, Edebiyat, Kimya\n")

ders_sayisi = 0
dersler = []

while ders_sayisi < 2:
    ders_isim = input("Ders ismi giriniz: ")
    ders = Ders(ders_isim)
    dersler.append(ders_isim)
    ders_sayisi += 1

print("\n", ogrenci.isim, ogrenci.soyisim)

print(dersler)


