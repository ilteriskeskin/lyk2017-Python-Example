while True:
    x = input("Bir sayı giriniz: ")
    if not x:
        break
    try:
        print(float(x)**2)
    except BaseException as e:
        print("Girdiğiniz veri bir sayı değil. Details: ",str(e))


