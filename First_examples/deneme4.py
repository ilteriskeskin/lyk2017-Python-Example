def collatz():

    n = int(input("Bir n değeri giriniz: "))
    dizi = [n]

    while n > 1:
        if n % 2 == 0:
            n = n / 2

        elif n % 2 != 0:
            n = 3 * n + 1

        dizi.append(n)

    return dizi


print(collatz())

