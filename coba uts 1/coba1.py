# def penjumlahan_berulang(hasil):
#     jumlah = 0
#     angka = 1
#     while jumlah < hasil:
#         jumlah += angka
#         angka += 1
#     return jumlah

# hasil = int(input("Masukkan batas : "))

# hasil_penjumlahan = penjumlahan_berulang(hasil)
# print(f"Hasil penjumlahan berulang hingga melebihi {hasil} adalah {hasil_penjumlahan}")


# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False

#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False

#     return True

# print(is_prime(input("Masukkan angka : ")))

# print("Muhammad Adifa Firmansyah")
# print("Im learning python basics")

# nama = input("whats your name ?")
# print ("hello", nama)

# """
# this is commeeeenennnnntttt
# """

# age = input("how old are u ?")
# print("welcome", age)

"""hitung luas bangun datar"""
# # Fungsi menghitung luas persegi
# def luas_persegi(sisi):
#     return sisi * sisi

# # Fungsi menghitung luas segitiga
# def luas_segitiga(alas, tinggi):
#     return 0.5 * alas * tinggi

# # Fungsi menghitung luas lingkaran
# def luas_lingkaran(jari_jari):
#     return 3.14 * jari_jari * jari_jari

# while True:
#     print("Pilih bangun datar yang akan dihitung luas:")
#     print("1. Persegi")
#     print("2. Segitiga")
#     print("3. Lingkaran")
#     print("4. Keluar")

#     pilihan = input("Masukkan pilihan (1/2/3/4): ")

#     if pilihan == '1':
#         sisi = float(input("Masukkan panjang sisi persegi: "))
#         print(f"Luas persegi: {luas_persegi(sisi)}")
#     elif pilihan == '2':
#         alas = float(input("Masukkan panjang alas segitiga: "))
#         tinggi = float(input("Masukkan tinggi segitiga: "))
#         print(f"Luas segitiga: {luas_segitiga(alas, tinggi)}")
#     elif pilihan == '3':
#         jari_jari = float(input("Masukkan jari-jari lingkaran: "))
#         print(f"Luas lingkaran: {luas_lingkaran(jari_jari)}")
#     elif pilihan == '4':
#         break
#     else:
#         print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

"""signal"""
# def signal():
#     n = int(input("Enter n value: "))

#     for i in range(1, n+1):     #kalo dibalik (n, 0, -1)
#         for j in range(1, i + 1):
#             print(chr(65 + j - 1), end=' ') #kalo mau angka(j, ends=' ')
#         print()
# signal()
