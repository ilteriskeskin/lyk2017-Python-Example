n = input("Tas Kagit Makas, birini giriniz: ")
m = input("Tas Kagit Makas, birini giriniz: ")

if n == 'Tas' and m == 'Kagit':
    print("Kagit kazandı")
elif n == 'Tas' and m == 'Makas':
    print("Tas kazandı")
elif n == 'Kagit' and m == 'Tas':
    print("Kagit kazandi")
elif n == 'Kagit' and m == 'Makas':
    print("Makas kazandı")
elif n == 'Makas' and m == 'Tas':
    print("Tas kazandı")
elif n == 'Makas' and m == 'Kagit':
    print("Makas kazandı")
else:
    print("Berabere")