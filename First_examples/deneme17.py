import random

random_sayi = random.randrange(1, 100)

while True:
    tahmin = int(input("Bir tahmin giriniz: "))
    if tahmin == random_sayi:
        print("Doğru")
        break
    elif tahmin > random_sayi:
        print("Aşağı in")
    elif tahmin < random_sayi:
        print("Yukarı çık")


