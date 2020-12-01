def rbt():
    lbx = 20  # changeme
    ubx = 40  # changeme
    lby = 70  # changeme
    uby = 110 # changeme
    lbz = 30  # changeme
    ubz = 80  # changeme

    nomx = (lbx + ubx) / 2
    nomy = (lby + uby) / 2
    nomz = (lbz + ubz) / 2

    print(str(lbx) + ":" + str(ubx))
    print(str(lby) + ":" + str(uby))
    print(str(lbz) + ":" + str(ubz))

    print(str(nomx) + ":" + str(nomy) + ":" + str(nomz))

    xpoints = [(lbx - 1), lbx, (lbx + 1), nomx, (ubx - 1), ubx, (ubx + 1)]
    ypoints = [(lby - 1), lby, (lby + 1), nomy, (uby - 1), uby, (uby + 1)]
    zpoints = [(lbz - 1), lbz, (lbz + 1), nomz, (ubz - 1), ubz, (ubz + 1)]
    cases = 6 * 3 + 1

    print(str(cases))

    print(str(xpoints))
    print(str(ypoints))
    print(str(zpoints))

    count = 1

    for i in range(0, 7):
        print(str(count) + "\t" + str(nomx) + "\t" + str(nomy) + "\t" + str(zpoints[i]))
        count += 1

    for i in range(0, 7):
        if ypoints[i] != nomy:
            print(str(count) + "\t" + str(nomx) + "\t" + str(ypoints[i]) + "\t" + str(nomz))
            count += 1

    for i in range(0, 7):
        if xpoints[i] != nomx:
            print(str(count) + "\t" + str(xpoints[i]) + "\t" + str(nomy) + "\t" + str(nomz))
            count += 1


rbt()
