def kullanici_goster(kullanicilar):
	print("Kullanıcı Adı", " | ", "Seçilen Dersler")
	for kullanici in kullanicilar:
		print(kullanici['isim'], kullanici['dersler'])


def ders_secim(kullanicilar, dersler, isim):
	tercih = 'E'
	while tercih == 'E':
		print("Ders seçimi yapmak için lütfen dersin kodunu girin: \n")
		try:
			count = 0
			while count < len(dersler):
				print("Code: " + str(count+1) + " Ders Adı: " + dersler[count] + "\n")
				count += 1
			ders_secim = int(input())
			ders = dersler[ders_secim-1]
			print("Seçilen ders: ", ders)
			for kullanici in kullanicilar:
				if kullanici['isim'] == isim:
					if ders in kullanici['dersler'] :
						print("=================")
						print("Bu dersi daha önce seçmişsiniz. Lütfen tekrar seçim yapın.")
						print("=================")
						break
					else:
						kullanici['dersler'].append(ders)
		except:
			print("Hatalı ders seçimi")
			tercih = input("Yeni bir ders seçimi yapmak ister misiniz? (E / H)")
		kullanici_goster(kullanicilar)


def kullanici_giris(kullanicilar, dersler):
	while True:
		isim = input("Giriş yapmak için adınızı girin: ")
		parola = input("Giriş yapmak için parolanızı girin: ")
		if any(kullanici['isim'] == isim and kullanici['parola'] == parola for kullanici in kullanicilar):
			print("===========")
			print("Giriş başarılı")
			print("===========")
			break
		else:
			print("Yanlış bir kullanıcı / parola ile girdiniz. Lütfen tekrar deneyin.")
	ders_secim(kullanicilar, dersler, isim)


def ders_kayit(kullanicilar):
	dersler = []
	count = 0
	while count < 3:
		isim = input("Ders adı giriniz: ")
		if not isim in dersler:
			dersler.append(isim)
			count += 1
		else:
			print("Bu ders daha önce tanımlanmış. Lütfen başka bir ders girin.")
	kullanici_giris(kullanicilar, dersler)


def kullanici_kayit():
	kullanicilar = []
	kayit_tercih = 'E'
	while kayit_tercih == 'E':
		isim = input("Kullanıcı adını giriniz: ")
		parola = str(input("Kullanıcı parolası giriniz: "))
		if not any(kullanici['isim'] == isim for kullanici in kullanicilar):
			kullanicilar.append({'isim': isim, 'parola': parola, 'dersler': []})
		else:
			print("Bu kullanıcı daha önce kaydedilmiş.")
		kayit_tercih = input("Yeni kullanıcı kaydetmek istiyor musunuz?: (E / H) ")
	else:
		ders_kayit(kullanicilar)


kullanici_kayit()