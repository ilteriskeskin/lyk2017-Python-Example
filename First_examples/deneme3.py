def sayi_gir():

    dizi = []

    for i in range(4):
        sayi = int(input("Bir sayı giriniz: "))
        dizi.append(sayi)

    carpim = (dizi[0] + dizi[1]) * (dizi[2] + dizi[3])

    return carpim

print(sayi_gir())

