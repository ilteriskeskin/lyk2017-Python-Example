import os

dizin = input("Dizin?: ")
dosyalar = os.listdir(dizin)

for dosya in dosyalar:
    baslik = "[DOSYA]"

    if os.path.isdir(os.path.join(dizin,dosya)):
        baslik = "[DİZİN]"
    print(baslik + " " +dosya)




