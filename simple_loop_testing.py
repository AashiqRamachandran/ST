import os


def slt():
    print("Loop size is 5")
    n = 4  # user input
    ub = n  # user input
    m = n + 1  # m is always n+1

    if m > n:
        print("vaues out of bound")

    if n >= ub:
        print("Value is inside bounds and beginning loop testing.")

        for i in range(0, 5):  # for  i =0, i<n;i++
            print("In execution " + str(i))
            if i == 4:
                print("Time to execute till UB and UB-1")

        for i in range(0, 5):  # for i=0;i<n;i++
            print('In execution ' + str(i))
        print("Time to execute till n")


slt()
