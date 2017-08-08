def ogrenci_ekleme():
    f = open("deneme.txt", "w")
    name = input("Bir isim giriniz: ")
    count = 0
    grades = []
    grades.append(name)
    f.write(name)

    while count < 3:
        grade = int(input("Not giriniz: "))
        grades.append(grade)
        f.write(str(grade))
        count += 1
    f.close()
    return grades

print(ogrenci_ekleme())


