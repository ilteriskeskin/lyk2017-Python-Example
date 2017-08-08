def kac_saniye():
    yas = int(input("Yaşını gir: "))
    saniye = (yas*((365*24)+6))*3600
    return saniye

print(kac_saniye())