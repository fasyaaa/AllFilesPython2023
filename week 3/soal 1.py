#1
# def two_number():
#     a= int(input("Enter the number : "))
#     b= int(input("Enter the number : "))
#     if a>b:
#         largest=a
#     elif(b>a):
#         largest=b
#     else:
#         largest="sama"

#     print("The number largest is : ", largest)

# two_number()

#2
# def three_number():
#     a= int(input("Enter the number : "))
#     b= int(input("Enter the number : "))
#     c= int(input("Enter the number : "))

#     if (a>b) and (b>=c):
#         largest=a
#     elif (b>=a) and (b>=c):
#         largest=b
#     else:
#         largest=c

#     print("The number largest is : ", largest)

# three_number()

#3
# def fibo_numbers():
#     length =int(input("Enter the length for fibonacci : "))
#     x= 0
#     y= 1
#     iteration = 0

#     if length <= 0:
#         print("Please provide number grater then zero")
#     elif length == 1:
#         print("this fibonacci sequence has {} element".format(length), ":")
#         print(x)
#     else:
#         print("This fibonacci sequence has {} element" .format(length), ":")
#     while (iteration < length):
#         print(x, end=',')
#         z= x + y
#         x = y
#         y = z
#         iteration += 1

# fibo_numbers()

#4
# def odd_number():
#     n = int(input("Enter number : "))
#     for i in range(1, n, 2):
#         print(i)

# odd_number()


#5
# def design():
#     n = int(input("Enter range column : "))
#     for i in range(n):
#         print("A B C")

# design()

# def hitung_odd_or_even():
#     x=int(input("enter number : "))
#     if x % 2 == 0 :
#         print ("Number is even")
#     else:  
#         print ("Number is odd")

# hitung_odd_or_even()

# angka = int(input(": "))

# if angka == 1:
#     for i in range (5):
#         print(i+1)

# else:
#     for i in range (angka):
#         print(i+1)

# print ("selesai")
nama = "kih"
if len(nama) == 3:
    print('Nama terlambat 3 huruf')
else:
    print ('Nama tidak terlambat 3 huruf')
