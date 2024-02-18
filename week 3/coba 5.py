def break_example():
    y=int(input("Enter the number : "))
    for i in range(0,y+1):
        if i == y:
            print("Thank you!!!")
            break
        else:
            print(i)
    print("End of Program")
break_example()