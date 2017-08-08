class Ders:
    def __init__(self, isim, gun, saat):
        self.isim = isim
        self.gun = gun
        self.saat = saat

class Kisi:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

class Ogrenci(Kisi):
    pass

class Ogretmen(Kisi):
    pass

ogrenci_isim = input("Öğrenci adı giriniz: ")
ogrenci_soyisim = input("Öğrenci soyadı giriniz: ")

ogretmen_isim = input("Öğretmen adı giriniz: ")
ogretmen_soyisim = input("Öğretmen soyadı giriniz: ")

ders_isim = input("Ders ismi giriniz: ")
ders_gun = input("Ders günü giriniz: ")
ders_saat = input("Ders saati giriniz: ")

ogrenci = Ogrenci(ogrenci_isim, ogrenci_soyisim)
ogretmen = Ogretmen(ogretmen_isim, ogretmen_soyisim)
ders = Ders(ders_isim, ders_gun, ders_saat)

print("\n", ogrenci.isim, ogrenci.soyisim, ",", ogretmen.isim, ogretmen.soyisim, "öğretmenini çok seviyor.\n")
print("|Ders| |Gün| |Saat|\n")
print(ders.isim, ",", ders.gun, ",", ders.saat)


