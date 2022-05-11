import time
import pandas as pd


def main(df):
    grDict = {}

    # matching rec_ids to golden ids
    for row in df.itertuples():
        if row.golden_id not in grDict:
            grDict[row.golden_id] = [row.a_rec[:-8], row.b_rec[:-8]]
        else:
            grDict[row.golden_id].append(row.a_rec[:-8])
            grDict[row.golden_id].append(row.b_rec[:-8])

    # dealing with duplications
    for key, value in grDict.items():
        grDict[key] = list(set(value))
    #        print(key, grDict[key])


    # checking to see if all values represent the same original record
    processGRDic = {}
    FNGRCount, FPGRCount, uniqueCount = 0, 0, 0
    for key, value in grDict.items():
        temp = value[0][:12]
        switch = True
        for v in value:
            if v[:12] != temp:                          # all values aren't from the same rec - FALSE POSITIVE
                FPGRCount += 1
                switch = False
                tempLabel = majorLabel(value)
                while tempLabel in processGRDic:        # just trying to make sure we don't merge golden records now
                    tempLabel += "*"                    # add an asterisk every time we have already included this GR
                    # print(tempLabel, tempLabel in processGRDic)
                processGRDic[tempLabel] = value
                break
        if switch:
            tempLabel = value[0][:12]
            while tempLabel in processGRDic:            # just trying to make sure we don't merge golden records now
                tempLabel += "*"                        # add an asterisk every time we have already included this GR
            processGRDic[tempLabel] = value

    lis = sorted(list(processGRDic.keys()))

    for k in lis:
        # print(k, processGRDic[k])
        if len(k) > 12:
            FNGRCount += 1
        else:
            uniqueCount += 1

    print("Number of golden records", len(grDict))

    print("FNGR count: ", FNGRCount)
    print("FPGR count: ", FPGRCount)
    print("Unique count: ", uniqueCount)

    print(len(processGRDic))


def majorLabel(values):
    # find the majority of records per GR and choose the most common one as the label
    # if it is the same number of occurrences, then choose the first alphabetical/sequential one
    dic = {}
    for v in values:
        if v[:12] not in dic:
            dic[v[:12]] = 1
        else:
            dic[v[:12]] += 1

    tempLabel = ""
    tempMax = 0
    for k, v in dic.items():
        if v > tempMax:
            tempLabel = k
            tempMax = v
        elif v == tempMax:
            tempLabel = sorted([k, tempLabel])[0]  # just takes the first one alphabetically

    return tempLabel
