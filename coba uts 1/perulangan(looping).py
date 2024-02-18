# def  sum_of_two_no():
# 	num1 = 1.5
# 	num2 = 6.3
# 	sum = float(num1) + float(num2)
# 	print("The sum is =" , sum)

# sum_of_two_no()

"""Write a PYTHON program to find 
largest of three numbers!"""

# def find_largest_number(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     num3 = float(input("Enter the third number:"))

#     largest = find_largest_number(num1, num2, num3)
#     print(f"The largest number is: {largest}")
# except ValueError:
#     print("Invalid input. Please enter valid numbers.")

"""Write a PYTHON program to print Fibonacci series up to n!"""

# def fibonacci_series(n):
#     fib_sequence = []
#     a, b = 0, 1

#     while a <= n:
#         fib_sequence.append(a)
#         a, b = b, a + b

#     return fib_sequence

# try:
#     n = int(input("Enter the value of n: "))

#     if n >= 0:
#         fib_sequence = fibonacci_series(n)
#         print("Fibonacci series up to", n, ":")
#         for num in fib_sequence:
#             print(num, end=" ")
#     else:
#         print("Please enter a non-negative integer for 'n'.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer for 'n'.")

""""odd number"""
# def print_odd_numbers(n):
#     for num in range(1, n + 1, 2):
#         print(num, end=" ")

# try:
#     n = int(input("Enter the value of n: "))

#     if n >= 1:
#         print("Odd numbers up to", n, ":")
#         print_odd_numbers(n)
#     else:
#         print("Please enter a positive integer for 'n'.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer for 'n'.")


# def using_if_elif():
# 	age = 27
# 	if age >= 60:
# 		print("hahaha child")
# 	elif 18>= age < 60:
# 		print ("you old")
# 	else: 
# 		print ("old man")
# using_if_elif()

"""Buatlah program Python yang mencetak tabel perkalian dari 
angka 1 hingga 10. Tabel perkalian akan menampilkan hasil 
perkalian dari masing-masing angka dengan angka-angka lainnya 
dalam rentang tersebut."""

# def tabel_perkalian():
#     for i in range (1, 11):
#         for j in range (1,11):
#             hasil = i * j
#             print (f"hasil perkalian {i} x {j} = {hasil}")

# tabel_perkalian()

"""Buatlah program Python yang mencetak pola bintang segitiga siku-siku terbalik.
Pola ini memiliki n baris, dan setiap barisnya memiliki jumlah bintang yang berkurang
secara berurutan dari atas ke bawah.
"""

# def pola_bintang():
#     try:
#         n = int(input("Masukkan nilai n : "))

#         if n > 0:
#             for i in range(n, 0, -1):
#                 for j in range(i):
#                     print("*", end=" ")
#                 print()
#         else:
#             print("Masukkan bilangan bulat positif.")
#     except ValueError:
#         print("Input tidak valid. Masukkan bilangan bulat positif.")
    
# pola_bintang()

"""Buatlah program Python yang menerima bilangan bulat
positif n sebagai input dari pengguna dan mencetak semua 
bilangan prima dari 2 hingga n.
"""

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# try:
#     n = int(input("Masukkan nilai n: "))

#     if n >= 2:
#         print("Bilangan prima antara 2 dan", n, "adalah:", end=" ")
#         for num in range(2, n + 1):
#             if is_prime(num):
#                 print(num, end=" ")
#         print()
#     else:
#         print("Masukkan bilangan bulat positif yang lebih besar dari 1.")
# except ValueError:
#     print("Input tidak valid. Masukkan bilangan bulat positif yang lebih besar dari 1.")

"""Buatlah program Python yang meminta pengguna untuk memasukkan jumlah 
suku n, suku pertama a, dan selisih d dalam deret aritmatika. 
Program ini harus mencetak deret aritmatika sesuai dengan parameter yang dimasukkan.
"""

# def deret_aritmatika():
#     try:
#         n = int(input("Masukkan jumlah suku (n): "))
#         a = int(input("Masukkan suku pertama (a): "))
#         d = int(input("Masukkan selisih (d): "))

#         if n > 0:
#             print("Deret aritmatika:")
#             for i in range(n):
#                 print(a, end=" ")
#                 a += d
#             print()
#         else:
#             print("Masukkan jumlah suku (n) yang lebih besar dari 0.")
#     except ValueError:
#         print("Input tidak valid. Masukkan bilangan bulat positif untuk n, a, dan d.")
# deret_aritmatika()