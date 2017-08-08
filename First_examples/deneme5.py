def asalmi(n):

    asal = True
    for i in range(2,n):
        if n % i == 0:
            asal = False
            break
    return asal

print(asalmi())