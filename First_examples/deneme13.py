### DOSYA İŞLERMLERİ###

dosya = open("deneme.txt", "w")

a, b = 1,1

dosya.write( str(a) + "\n" )

while b < 1000:
    dosya.write( str(b) + "\n" )
    a, b = b, a+b

dosya.close()

for fib in open("deneme.txt", "r"):
    print(fib)

