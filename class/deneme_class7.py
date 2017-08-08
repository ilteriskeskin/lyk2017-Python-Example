class Album:
    albumler = []
    def __init__(self, isim, tur):
        self.isim = isim
        self.tur = tur
        self.sarkilar = []
        Album.albumler.append(self)

    def albume_ekle(self, sarki):
        self.sarkilar.append(sarki)

class Sarki:
    def __init__(self, isim, sure):
        self.isim = isim
        self.sure = sure

album_listesi = {"pop": ["Yolla","Karakedi"],"sanat":["saklı","intizar"]}

for item in album_listesi.items():
    for album_adi in item[1]:
        a = Album(album_adi, item[0])

while True:
    isim = input("Bir şarkı adı giriniz: ")
    sure = input("Bir şarkı süresi giriniz: ")

    print("Album Adı" + " | " + "Album Türü")

    for album in Album.albumler:
        print(album.isim, "----->", album.tur)


    secim = input("Bir albüm seçiniz: ")

    for album in Album.albumler:
        if album.isim == secim:
            secilen_album = album

    sarki = Sarki(isim, sure)

    album.albume_ekle(sarki)

    tercih = input("Yeni bir şarkı girmek istiyor musunuz?: (e/h): ")

    if tercih != 'e':
        break

print("Album adı: ")
for album in Album.albumler:
    print(album.isim , "  " , album.tur , "  " , len(album.sarkilar))



