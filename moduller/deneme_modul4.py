import os
import json

dizi = []

soru = input("Hangi dizini silmek istiyorsun? Yolunu ver?: ")

dizi.append(soru)

liste = os.listdir(dizi[0])

for i in liste:
    os.remove(dizi[0] +"/" + i)

os.rmdir(dizi[0])

#os.system("rm -fr %s" % dizi[0])
