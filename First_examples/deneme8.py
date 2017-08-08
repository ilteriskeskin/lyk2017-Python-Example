def kare_bul():
    n = int(input("X değerini giriniz: "))
    m = int(input("Y değerini giriniz: "))

    buyuk_kare_x = int(n / 3)
    buyuk_kare_y = int(m / 3)

    kucuk_kare_x = n % 3
    kucuk_kare_y = m % 3

    return (buyuk_kare_x, buyuk_kare_y, '<--->', kucuk_kare_x, kucuk_kare_y)

print(kare_bul())

