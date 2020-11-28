import os

def bva():
    a=int(input("Enter lower bound: "))
    b=int(input("Enter upper bound: "))
    c=int(input("Enter value to test: "))

    if c > a and c < b:
        print("Value is inside bounds.")
    elif c < a:
        print("Value is lesser than lower bound.")
    elif c > b:
        print("Value is greater than upper bound.")
    elif c == a or c==b:
        print("Value on boundries.")

bva()
