# i = 1
# n = int(input("Lebokne angka = "))
# while (i <= n):
#     print(i)
#     i+=1

# sum1 = int(input("Masukkan sum nya = "))
# count = int(input("masukkan nilai hitung = " ))
# while(count > 1):
#     sum1 = sum1+count
#     count = count + 1
# print(f"hasil dari {count}")
# print(f"Hasil dari {sum1}")

"""Ganjil"""
# def for_loop_exe():
#     n = int(input("Masukkan nomer : "))
#     for i in range(1, n, 2):
#         print(i)
# for_loop_exe()

"""Genap"""
# def for_loop_exe():
#     n = int(input("Masukkan nomer : "))
#     for i in range(0, n, 2):
#         print(i)
# for_loop_exe()

"""Write a PYTHON program to 
print the natural numbers up to n
"""
# def for_loop_exe():
#     try:
#         n = int(input("Enter a value for n: "))
#         if n < 1:
#             print("Please enter a positive integer.")
#         else:
#             print("Natural numbers up to", n, "are:")
#             for i in range(1, n + 1):
#                 print(i)
#     except ValueError:
#         print("Invalid input. Please enter a valid positive integer for n.")
# for_loop_exe()

"""Even number"""
# def even_number():
#     try:
#         n = int(input("Enter a value for n: "))
#         if n < 1:
#             print("Please enter a positive integer.")
#         else:
#             print("Even numbers up to", n, "are:")
#             for i in range(0, n, 2):
#                 print(i)
#     except ValueError:
#         print("Invalid input. Please enter a valid positive integer for n.")
# even_number()

"""Odd number"""
# def odd_number():
#     try:
#         n = int(input("Masukkan sampai angka berapa : "))
#         if n < 1:
#             print("Masukan bilangan positive")
#         else:
#             print("Angka ganjil dari 1 hingga", n, "adalah:")
#             for i in range(1, n, 2):
#                 print(i)
#     except ValueError:
#         print("Masukan seng positive blok")
# odd_number()

# """double"""
def double_number():
    try:
        n = int(input("Enter a value for n: "))
        if n < 1:
            print("Please enter a positive integer.")
        else:
            print("Sequence of numbers up to n^2:")
            number = 1
            while number <= n ** 2:
                print(number, end=" ")
                number *= 2
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for n.")
double_number()

"""sum given"""
# import math

# def calculate_sequence_sum(n):
#     sequence_sum = 0
#     for i in range(n + 1):
#         factorial = math.factorial(i)
#         sequence_sum += 1 / factorial
#     return sequence_sum

# try:
#     n = int(input("Masukkan nilai n: "))
#     if n < 0:
#         print("Harap masukkan bilangan bulat non-negatif.")
#     else:
#         result = calculate_sequence_sum(n)
#         print(f"Jumlah dari urutan adalah: {result:.6f}")
# except ValueError:
#     print("Input tidak valid. Harap masukkan bilangan bulat non-negatif untuk n.")


"""luas persegi"""
def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def main():
    while True:
        try:
            panjang = float(input("Masukkan panjang bangun persegi panjang (0 untuk keluar): "))
            if panjang == 0:
                break
            lebar = float(input("Masukkan lebar bangun persegi panjang: "))
            luas = hitung_luas_persegi_panjang(panjang, lebar)
            print(f"Luas bangun persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
        except ValueError:
            print("Masukkan tidak valid. Harap masukkan angka.")
