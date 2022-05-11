def calc(testSeries, tpList):       # sorted Pandas series of rec_id and true positive list

    # generate list of expected matches
    allList = []

    for i in range(len(testSeries) - 1):
        for j in range(i+1, len(testSeries)):
            if testSeries[i][:12] == testSeries[j][:12]:
                allList.append(simplify([testSeries[i], testSeries[j]]))
            else:
                break               # because it is ordered, we don't have to look any further

    print("Length all list", len(allList), len(set(allList)))
    print("Length TP list ", len(tpList), len(set(tpList)))

    # remove tpList from allList to get false negatives that were missed in SanteMPI
    fnList = list(set(allList) - set(tpList))

    print("FN: ", len(fnList))
    return fnList


def pairUp(row1, row2):
    return [row1[:-8], row2[:-8]]


def simplify(lis):
    return lis[0] + "," + lis[1]
