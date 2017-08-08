def bolenler():
    n = int(input("Birinci sayıyı giriniz: "))
    m = int(input("İkinci sayıyı giriniz: "))

    dizi1 = []

    if n > m:
        en_kucuk = m
    elif m > n:
        en_kucuk = n

    for i in range(1,en_kucuk):
        if n % i == 0 and m % i == 0:
            dizi1.append(i)

    return dizi1

print(bolenler())
