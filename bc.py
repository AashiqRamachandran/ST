import os

def bc():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))

    print("Total is: "+str(a+b))

    if a>b:
        print(str(a)+" is greater.")
    elif b>a:
        print(str(b)+" is greater")
    else:
        print("Both are equal")

bc()
