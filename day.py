# print('Hello Zan')

# VARIABLE adalah tempat menyimpan data

# nama = "Hallo ....."
# print(nama)

# TIPE DATA (DATA TYPE)
# untuk melihat type daya bisa menggunakan, type(variable)

# angka
# numberZ = 123
# print(numberZ)

# string
# stringZ = "halo kaka"
# print(stringZ)

# congcatiation
# pemainBola = "Cristiano"
# blackPink = "jisoo"
# print(pemainBola + " Ronaldo")
# print(pemainBola + " " + blackPink)
# print("jisoo akan menggung \n di yogyakarta")
# blackPink.capitalize()

# escaping
# pubg = "senjata saya pakai"
# print(pubg + "M4 \" Glacier" )

# aplikasi sederhana menggunakan interaksi input
# pubg = input("Anda suka pakai senjata apa? ")
# sniper = input("Anda pakai seniper pake tipe apa? ")
# print("Halo saya suka bermain PUBG menggunakan senjata " + pubg + " pakai sniper jenis " + sniper)

# boolean ada lah objeak atau tipe data yang nilainya true/false
# boolean adalah hasil atau nilai sesuatu antara true/false
# angka1 = 20000
# angka2 = 100000
# print(angka1 > angka2)
# == -> apakah angka1 sama dengan angak2
# angka 1 nggak "lebih besar" daripada 2
# if angka1 < angka2: 
#     print("Ya Betul") #true
# else: 
#     print("Ya Salah") #false

# elif
# uang = input("Uang kamu ada berapa? ")
# utang = 30000

# if int(uang) < utang:
#     print("Wah duitnya kurang")
# elif int(uang) == utang:
#     print("Kesuwun wis bayar")
# else:
#     print("Pak duitmu kelebihan")

# logika operator
# and(&), or(|), not(!=)

# & jika memakai operator ini syarat1 dan syarat2 harus terpenuhi.
# | jika memakai operator ini syarat1 atau syarat2, sayaratnya cukup salah satu aah terpenuhi. walaupun ada fals jawabanya tetep benar.

# syarat1 = True
# syarat2 = False

# if syarat1 | syarat2:
#     print("ya betul")
# else:
#     print("ya sayah")

# putri mencari jodoh

# tamu = "Cewe"
# baik = True
# jujur = True

# if baik & jujur:
#     if tamu == str("Cewe"):
#         print("Yuk nikah")
#     else:
#         print("Kita saudara ajah")
# else:
#     print("Kamu bukan tipe ku")

# halooo saya
# <h1> PUBG </h1>
# <h2> Valorant </h2>
# <h2> Dota 2 </h2>

# <h2> Toshiba </h2>
# <h2> Daihatsu </h2>

# while loop

# count = 0

# while count < 5:
#     print("Yey akhirnya saya punya M4 Glacier")
#     count = count+1
# else:
#     print("Hup berhenti sampai sini")

# for in loop

# pubgSenjata = ['M4', 'AWM', 'AKM', 'MINI 14']

# for pubg in pubgSenjata:
#     print("Saya pakai senjata", pubg)

# loop bercabang = 2.50

# angkaPertama = 1

# while angkaPertama < 5:
#     angkaKedua = 0
#     while angkaKedua < angkaPertama:
#         print('*', end="")
#         angkaKedua = angkaKedua+1
#     print("End")
#     angkaPertama = angkaPertama+1

# list -> adalah kumpulan beberapa data dalam variable

# game = ["PUBG", "MOBILE LEGEND", "APEX LEGEND", "VALORANT"]
# rilisTahun = [2011, 2009, 2007, 2019]
# buatanNegara = ["TOKYO", 2019, "KOREA", 9090]

# game.append("HUHAK") -> untuk menambahkan
# game[0] = "LEGEND" -> untuk mengedit
# del rilisTahun[2] -> untuk menghapus

# print(rilisTahun)

# list tuple -> ini sifatnya immutable, gak bisa di ganti, edit, delete, tambah

# memberRedvelvet = ("Irene", "Joy", "Yeri", "Wendy", "Seul-gi") -> tuple
# memberBlackpink = ["Jisoo", "Lisa", "Jeny", "Rose"] -> merubah menjadi tuple

# print(tuple(memberBlackpink)) -> merubah menjadi tuple

# list[], tuple(), 
# dictionary{} 
# key:value

# memberRedvalvet = {
#     'nama'  : 'Irene',
#     'age'   : '17',
#     'hobi'  : 'Nyanyi'
# }

# memberRedvalvet['genre'] = 'Slow' -> menambah
# memberRedvalvet['nama'] = 'Yeri' -> mengedit
# del memberRedvalvet['age'] -> mengedit

# for key, value in memberRedvalvet.items():
#     print(key + " - " + value)

# nested dictionary{} 

# girlKorea = { 
#             1 : {'nama' : 'Irene', 'age' : '17', 'hobi' : 'BlackPink'},
#             2 : {'nama' : 'Jiso', 'age' : '27', 'band' : 'RedValvet'},
#             3 : {'nama' : 'Rose', 'age' : '17', 'hobi' : 'BlackPink'},
#             4 : {'nama' : 'Yeri', 'age' : '27', 'band' : 'RedValvet'},
#             }

# menampilkan scara spesifik
# print(girlKorea[2]['nama'])

# for key, value in girlKorea.items():
#     print("\nKey", key)
    
#     for key2 in value:
#         print(key2 + "-" + value[key2])

# functions() -> adalah beberapa baris code / satu code kita buat jadi 1 functions dan bisa di pakai berulang
# makanya kita buat jadi satu, kalau butuh kita bisa panggil functions nya.
  
# def namafunction():
#     print("------")
#     print("Member Black Pink Jisoo")
#     print("------")

# namafunction()

# argument / parameter -> adalah variable yang kita oper ke dalam functions, untuk kita pakai di dalam fungsinya

# def memberBlackPink(namaMember = "member tidak di ketahui"):
#     print("Hei nama saya", namaMember)

# memberBlackPink("Jisoo")
# memberBlackPink("Rose")
# memberBlackPink("Lisa")
# memberBlackPink("Jennie")
# memberBlackPink()

# argement parameter lebih dari satu -> jadi untuk menambahkan parameter anda bisa memisahkan menggunakan , contoh(a, b)

# def belajarHitung(A, B):
#     print("Hasil dari A dan B =", A + B)

# belajarHitung(30, 90)
# belajarHitung(30, 989237210)

# Return -> return adalah mengembalikan suatu nilai. Dia tidak bertugas untuk print. Kita g tau mau di apain di dalamnya, mau di olah dll.

# def belajarHitung(a, b):
#     c = a + b
#     return c

# print(belajarHitung(20, 30))

# keyword argument -> untuk menentukan posisi urutan memanggil. Terbalik atau berbeda dari sebelumnya.

# def namaGirlBand(nama, negara):
#     print("nama =", nama + " - negara = ", negara)

# namaGirlBand(negara = 'Korea', nama = 'Jisoo')