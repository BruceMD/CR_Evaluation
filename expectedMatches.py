def calc(df):

    matches = 0
    ind = 0
    while ind < len(df):
        if "aaa" in df.ID[ind]:
            win = ind + 1
            count = 1
            while win < len(df):
                if "aaa" in df.ID[win]:
                    break
                else:
                    count += 1
                    win += 1
            matches += q(count)
            ind = win

    print("Expected matches: ", int(matches))


def q(n):
    return n*n/2 - n/2


def printPlot(df):
    hist = [0 for _ in range(50)]

    ind = 0
    while ind < len(df):
        # print(df.ID[ind])
        if "aaa" in df.ID[ind]:
            win = ind + 1
            count = 1
            while win < len(df):
                if "aaa" in df.ID[win]:
                    break
                else:
                    count += 1
                    win += 1
            hist[count] += 1
            ind = win

    for x, num in enumerate(hist):
        if num > 0:
            print(str(x).rjust(3), "# ", "#"*(num//(sum(hist)//1000)), num)


def printDPlot(df):
    hDic = {}
    for row in df.ID:
        if row[13:] not in hDic:
            hDic[row[13:]] = 1
        else:
            hDic[row[13:]] += 1

    dList = ["bbb-"+str(i) for i in range(len(hDic)-1)]
    dList.insert(0, "aaa-0")

    for d in dList:
        print(d.rjust(7), "# ", "#"*(hDic[d]//(sum(hDic.values())//1000)), hDic[d])


def q(n):

    return n*n/2 - n/2
