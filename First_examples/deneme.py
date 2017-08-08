def kayit():
    liste=[]

    for i in range(2):
        a=[]
        isim=input("Adını gir: ")
        soyisim=input("Soyadını gir: ")
        a.append(isim)
        a.append(soyisim)
        liste.append(a)
    print(liste)

kayit()

