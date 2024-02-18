"""check student performance"""
# def student_performance(percentage):
#     if percentage >=90:
#         return "Excellent"
#     elif percentage >=80:
#         return "Very good performance"
#     elif percentage >=70:
#         return "Good performance"
#     elif percentage >=60:
#         return "average performance"
#     else:
#         return "Below performance"
# try:
#     percentage = float(input("Masukkan nlai : "))
#     if 0<= percentage <= 100:
#         result = student_performance(percentage)
#         print(f"The student result is = {result}")
#     else:
#         print("Invalid percentage input 0 between 100")
# except ValueError:
#     print("Invalid input. Please enter a valid percentage as number")
# student_performance(percentage)

"""check zero number"""
# def check_zero(number):
#     if number >=1:
#         return True
#     elif number <=-1:
#         return True
#     else:
#         return False
#     print(check_zero())

# try:
#     number = float(input("Masukkan angka : "))
#     if -100 <= number <= 100:
#         result = check_zero(number)
#         print(f"Hasil pengecekan angaka = {result}")
#     else:
#         print("Input salah, silakan masukkan angka antara -100 dan 100.")
# except ValueError:
#     print("Senggenah ae su")

# check_zero(number)

"""check positive negative number"""
# def check_number_pos_neg(number):
#     if number > 0:
#         return "positive masse"
#     else:
#         return "negative leee"

# try:
#     number = float(input("lebokno angka cok : "))
#     if -100 <= number <=100:
#         result = check_number_pos_neg(number)
#         print(f"hayo masuk angka apa coba : {result}")
#     else:
#         print("cok seng genah ae senggel po")
# except ValueError:
#     print("Asu seng genah ae lah gok")

"""check vowel or not"""
# def check_vowel():
#     vowels = "AIUEOaiueo"

#     if vowels:
#         return True
#     else:
#         return False
    
# try:
#     huruf = input("Masukkan huruf : ")
#     result = check_vowel()
#     print(f"hasil dari huruf adalah {result}")
# except ValueError:
#     print("senggenah lah")

"""check largest number"""
# def check_largest(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2>= num3:
#         return num2
#     else:
#         return num3

# try:
#     n1 = int(input("Masukkan angka pertama = "))
#     n2 = int(input("Masukkan angka kedua = "))
#     n3 = int(input("Masukkan angka ketiga = "))

#     largest = check_largest(n1, n2, n3)
#     print(f"hasil dari angka terbesar : {largest}")
# except ValueError:
#     print("Senggenah lah")

"""check smallest number"""
# def check_smallest(num1, num2, num3, num4):
#     if num1 <= num2 and num1 <= num3 and num1 <= num4:
#         return num1
#     elif num2 <= num1 and num2 <= num3 and num2 <= num4:
#         return num2
#     elif num3 <= num1 and num3 <= num2 and num3 <= num4:
#         return num3
#     else:
#         return num4
    
# try:
#     n1 = int(input("Masukkan angka pertama = "))
#     n2 = int(input("Masukkan angka kedua = "))
#     n3 = int(input("Masukkan angka ketiga = "))
#     n4 = int(input("Masukkan angka keempat = "))
    
#     smallest = (check_smallest(n1, n2, n3, n4))
#     print(F"Hasil dari angka terkecil adalah : {smallest}")
# except ValueError:
#     print("Senggenah lah")

"""check leap year"""
# def leap_year(year):
#     if (year% 4 == 0 and year %100 != 0) or (year% 400 == 0):
#         return True
#     else:
#         return False
    
# try:
#     year = int(input("Masukkan tahun : "))
#     if year >= 0:
#         if leap_year(year):
#             print(f"{year} tahun kabisat.")
#         else:
#             print(f"{year} bukan tahun kabisat.")
#     else:
#         print("Masukiin yang positive lah.")

# except ValueError:
#     print("Invalid tidak tersedia. Masukkan tahun yang valid")

"""case company driver """
# def company_insurance(marital_status, gender, age):
#     if marital_status == "ws" or (marital_status == "rung" and ((gender == "lanang" and age >= 30) or (gender == "wadon" and age >= 25))):
#         return "oleh asuransi"
#     else:
#         return "gaoleh cok nguteg sitik"
    
# try:
#     marital_status = input("ws kawin rung ?")
#     gender = input("lanang po po masse ?")
#     age = int(input("piro umurmu lek ?"))

#     result = company_insurance(marital_status, gender, age)
#     print(f"seng nyetir {result}")
# except ValueError:
#     print("seng genah ae to le")


