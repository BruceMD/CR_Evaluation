import calcFN
import time


# finding the number of TPs and FPs from the results, return TP list
def evaluate(santeDF):
    tp, fp, tn, fn = 0, 0, 0, 0
    tpList = []
    fullList = []

    print("SanteDF length:", len(santeDF))

    # taking the pairs of records for comparison
    # pairUp takes [:18] slice of record XXX names and sorts them sequentially/alphabetically
    # simplify returns them in String format
    for row in santeDF.itertuples():
        fullList.append(calcFN.simplify(pairUp(row)))

    fullList = sorted(fullList)

    # DeDuplicating this list into a set and back to a list, splitting them up again
    ddList = [dd.split(",") for dd in list(set(fullList))]

    print("Found Positives:", len(ddList))

    # count the number of tps and fps in the deduplicated list, create TP list
    for dd in ddList:
        if dd[0][:13] == dd[1][:13]:
            tpList.append(calcFN.simplify(dd))
            tp += 1
        else:
            fp += 1

    print("TP: ", tp)
    print("FP: ", fp)

    return sorted(tpList)


def pairUp(row):
    return sorted([row.a_rec[:-8], row.b_rec[:-8]])
