import socket

# Server socketimizi hazırlıyoruz. (AF_INET, AF_UNIX) (SOCK_STREAM, SOCK_RAW, SOCK_DGRAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kullanacağımız IP ve PORT'u belirttik.
host = "0.0.0.0"
port = 1453

# Server socketimizin kullanacağı host ve port'u bir tuple içerisinde belirtiyoruz. (DAHA SOCKET AÇILMADI / DİNLENMİYOR)
server.bind((host, port))

# Socket'i dinlemeye başla, (listen'e parametre vererek dinlenecek maksimum sayı belirtilebilir)
server.listen()

print("[SERVER] Bağlantı bekleniyor...")

client, addr = server.accept()  # Bağlantı gelince bunu client ve addr değişkenlerine aktardık.

print("[SERVER] Biri bağlandı: %s" % str(addr))

# Veri taşıma yapacağımız için göndereceğimiz metni 'encode' ettik. Burada 'encode' ettiğimiz karakter seti önemli
client.send("Sunucuma hosgeldin :)".encode('utf-8'))

# Client'ten gelecek mesajı bekleyelim. (1024 byte'dan fazla olmayacak)
gelenMesaj = client.recv(1024)

print("[SERVER] İstemciden gelen mesaj: " + gelenMesaj.decode('utf-8'))

while True:
    gidecekMesaj = input("Göndermek istediğiniz mesaj: ")

    client.send(gidecekMesaj.encode('utf-8'))

    gelenMesaj = client.recv(1024)
    gelenMesaj = gelenMesaj.decode("utf-8")
    print("[SERVER] İstemciden gelen mesaj: " + gelenMesaj)

    if gelenMesaj == "exit":
        break

# İstemci ile olan bağlantımızı sonlandırdık. (artık bizi dinlemiyor ve biz de ona bir şey söyleyemiyoruz.)
client.close()