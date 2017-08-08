from flask import Flask, render_template , request , redirect
import json

app = Flask(__name__)

kullanicilar = {"ahmet":"aksoy","selim":"koc","ayse":"donmez"}

json_file = "kisiler.json"

@app.route("/")
def hello():
	isimler = ["Ahmet", "Burak", "ilteris", "Ali"]
	return render_template("yeni_index.html",isim_listesi = isimler)

@app.route("/kullanicilar")
def kullanicilar():
	try:
		kisi_listesi = json.load(open(json_file,"r"))

	except:
		kisi_listesi = []

	return render_template("kullanici_kaydi.html", kisi_listesi = kisi_listesi)

@app.route("/kullanici_kaydet", methods = ("POST", "GET"))
def kullanici_kaydet():
	try:
		kisi_listesi = json.load(open(json_file,"r"))

	except:
		kisi_listesi = []

	if request.method == "POST":
		if request.form.get('isim', None) and request.form.get('telefon', None):
			if len(kisi_listesi) > 0:
				uid = kisi_listesi[-1].get("id") + 1
			else:
				uid = 1
			kisi_listesi.append({"isim": request.form.get('isim'),
								 "telefon": request.form.get('telefon'),
								 "id":uid,
								 "bio":request.form.get('bio')})

			open(json_file, "w+").write(json.dumps(kisi_listesi))

	return redirect("/kullanicilar")

@app.route("/kullanici/<kullanici>")
def kullanicilar_goruntuleme(kullanici):
	if kullanicilar.get(kullanici,None):
		bulunan_kullanici = kullanicilar.get(kullanici)
	else:
		bulunan_kullanici = None

	return render_template("kullanici.html", bulunan = bulunan_kullanici, kullanici_url = kullanici)

@app.route("/kisi<int:uid>")
def kisi_goruntuleme(uid):
	try:
		kisi_listesi = json.load(open(json_file, "r"))
	except:
		kisi_listesi = []

	bulunan_kisi = None
	for kisi in kisi_listesi:
		if kisi.get("id") == uid:
			bulunan_kisi = kisi
	return render_template("kisi.html", kisi = bulunan_kisi)
@app.route("/secondpage")
def second_page():
	return "Hack the Planet"

app.run(debug = True, host = "0.0.0.0", port = 1453)
