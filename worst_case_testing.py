import os

def wct():
    x = 5
    y = 2
    lbx = 20
    ubx = 40
    lby = 20
    uby = 40
    nomx = (lbx+ubx)/2
    nomy = (lby+uby)/2
    pointx = [lbx, lbx+1, nomx, ubx-1, ubx]
    pointy = [lby, lby-1, nomy, uby-1, uby]
    print(pointx)
    print(pointy)
    for i in range(0,5):
        for j in range(0,5):
            print(str(pointx[i]) + " " + str(pointy[j]))
wct()
