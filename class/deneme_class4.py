class Ogrenci:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        self.dersler = []

    def isim_soyisim(self):
        return self.isim + " " + self.soyisim

    def kayit(self, ders):
        self.dersler.append(ders)

class Ogretmen:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def isim_soyisim(self):
        return self.isim + " " + self.soyisim

class Ders:
    def __init__(self, isim, gun, saat):
        self.isim = isim
        self.gun = gun
        self.saat = saat

ogrenci_adi = input("Öğrenci adını giriniz: ")
ogrenci_soyadi = input("Öğrenci soyadını giriniz: ")

ogrenci = Ogrenci(ogrenci_adi, ogrenci_soyadi)

#print(ogrenci.isim)
#print(ogrenci.soyisim)
print(ogrenci.isim_soyisim())

ders = Ders("Matematik", "Pazartesi", "10:00")
ogrenci.kayit(ders)
print(ogrenci.dersler[0].isim, ogrenci.dersler[0].gun, ogrenci.dersler[0].saat)
