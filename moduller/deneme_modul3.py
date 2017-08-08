import json
import re

def secim(js):

    dizi = []

    secim = input("Bir yemek numarası seçiniz: ")

    for i in js:
        if secim == i:
            dizi.append(secim)
            print("Siparişe eklendi")
        else:
            print("Olmaz")


def menu():
    dosya = open("sozluk.txt", "r")

    oku = dosya.read()

    js = json.loads(oku)

    print(js)

    parsel = oku.split(",")

    print(parsel)

    secim(js)

menu()

