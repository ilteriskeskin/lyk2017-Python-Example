import random

dizi = []

while len(dizi) < 3:
    toplam = 0
    random_sayi = random.randint(1, 500)
    for j in range(1, random_sayi):
        if random_sayi % j == 0:
            toplam += j
    if toplam == random_sayi:
        dizi.append(random_sayi)
print(dizi)