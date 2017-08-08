class Kurs:
    adi = "PHP"
    vantilator = 0

    def araVer(self):
        print(self.adi + " sınıfı ara veriyor")
        pass

    def vantilator_lazim_mi(self):
        return self.vantilator < 2

php = Kurs()
php.araVer()
php.vantilator = 10
python = Kurs()
python.adi = "Python"
python.araVer()

while python.vantilator_lazim_mi():
    print(str(python.vantilator) + " yetmez " + str((python.vantilator+1)) + " olsun")
    python.vantilator += 1


