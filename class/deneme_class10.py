class Pokemon:
    def __init__(self, adi, soyadi):
        self.adi = adi
        self.soyadi = soyadi

class Digimon(Pokemon):
    def __init__(self,adi, soyadi, form):
        super(Digimon, self).__init__(adi, soyadi)
        self.form = form

    def isim_yaz(self):
        print(self.adi)

    def bilgiler(self):
        print("FORM: ", self.form)

class Senior(Pokemon):
    def __init__(self, ad, soyadi, saldırı_gucu):
        super().__init__(ad, soyadi)
        self.saldiri_gucu = saldırı_gucu

    def saldir(self):
        print(self.adi + " " + str(self.saldiri_gucu) + " ile saldırıyor!")

class Junior(Digimon):
    def __init__(self, adi, soyadi, ozel_guc):
        super(Junior, self).__init__(adi, soyadi, 1)
        self.ozel_guc = ozel_guc

    def bilgiler(self):
        super().bilgiler()
        print("Ozel Güç: ", self.ozel_guc)

j = Junior("Junior", "Nesnesi", "ozel")

j.bilgiler()

s = Senior("Senior", "Poke", 100)
s.saldir()

