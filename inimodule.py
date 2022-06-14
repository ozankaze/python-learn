# untuk mengambil data kita menggunakan (import)
# import day

# kalau penamaan tidak suka bisa menggunakan {as (nama file yang kita suka)}
# import day as belajarModule

# print(belajarModule.memberRedvalvet)
# print(belajarModule.namaOrang('Luffy'))

# untuk mengimport suatu object yang sepesifik
# from day import namaOrang
# from day import memberRedvalvet

# namaOrang('Luffy')
# print(memberRedvalvet)

# build in module datetime

# import datetime as dt
# import calendar as cl

# now = dt.datetime.now()
# print(now.strftime("%Y, %B"))

# yy = 2022
# mm = 6
# print(cl.month(yy, mm))

# === Global dan local variable

# ini adalah global variable
# nama = "Irene"

# def namaOrang():
#     # kalau akses global variable pake cara ini
#     global nama

#     # ini adalah local variable
#     nama = "Yeri"
#     print("Akses dari dalam", nama)

# namaOrang()
# print("Akses dari luar", nama)

# === Exception -> untuk menghentikan proggram (debugging)

# nama = "Zan"

# untuk menghentikan proggram kita pakai ini
# raise Exception("Stop")

# print(i + nama)
# print("Finis")

# === Bermain Ala-Ala PUBG

# nama = input("Pilih senjata apa nie? ")
# senjata = {
#         "nama" : nama,
#         "power" : 400 
#     }

# def startGame():
#     pilihan = input("Mau apa? 1. Main game 2. Lihat status senjata 3. Nambah demage 4. Keluar.  ")
    
#     if pilihan == "1":
#         goPlay()
#     elif pilihan == "2":
#         goSenjata()
#     elif pilihan == "3":
#         goDemage()
#     else:
#         goExit()

# def goPlay():
#     print("We ayo main")
#     startGame()

# def goSenjata():
#     print("Weh senjatanya")
#     print(senjata)
#     startGame()

# def goDemage():
#     senjata['power'] += 600
#     print("Demage di tambah", senjata['power'])
#     startGame()

# def goExit():
#     print("Exit")

# startGame()