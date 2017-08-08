import math
import random

random_sayi = random.randrange(1 , 100)

print(random_sayi)

kare_kok = math.sqrt(random_sayi)

print(kare_kok)

if kare_kok == int(kare_kok):
    print("Tam sayıdır.")
else:
    print("Tam sayı değildir.")
