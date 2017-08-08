def mukemmel_sayilar():

    son = 1000
    mukemmel = []

    for i in range(6, son):
        bolenler = []
        for j in range(1, i):
            if i % j == 0:
                bolenler.append(j)

        if i == sum(bolenler):
            mukemmel.append(i)

    return mukemmel


print(mukemmel_sayilar())

