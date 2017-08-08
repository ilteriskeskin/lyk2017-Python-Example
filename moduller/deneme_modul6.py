import os

dizin = input("Dizin?: ")

def listele(path):
    dosyalar = os.listdir(path)

    for  dosya in dosyalar:
        if os.path.isdir(os.path.join(path, dosya)):
            listele(path + "/" + dosya)
        print(dosya)

listele(dizin)

