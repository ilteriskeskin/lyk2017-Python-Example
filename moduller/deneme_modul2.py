import json

dosya = open("sozluk.txt", "r")
oku = dosya.readline()

js = json.loads(oku)
print(js)

