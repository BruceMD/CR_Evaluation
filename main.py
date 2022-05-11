import calcFN
import evaluate
import expectedMatches
import readTestData
import readSanteFile
import viewGold
import weirdFPs

data_files = {0: "data-test-32-d-001000-004000-dcab.csv",
              1: "data-10000-05000-dcab.csv",
              2: "data-30000-15000-dcab.csv",
              3: "data-test-32-d-020000-080000-dcab.csv",
              4: "data-test-32-d-005000-095000-dcab.csv",
              5: "data-test-32-d-060000-240000-dcab.csv",
              6: "data-test-32-d-050000-950000-dcab.csv"}

santeFiles = {0: "1500_matches_full.csv",
              1: "15k_matches_full.csv",
              2: "45k_matches_full.csv",
              3: "100k_1_4_matches_full_golden_id.csv",
              4: "100k_1_20_ratio_matches_full_golden_id.csv",
              5: "300k_matches_full_golden_id.csv"}

result_files = ["32-d-001000-004000-sorted.csv", "32-d-001000-004000-unsorted.csv",
                "32-d-020000-080000-sorted.csv", "32-d-020000-080000-unsorted.csv",
                "32-d-060000-240000-sorted.csv", "32-d-060000-240000-unsorted.csv",
                "32-d-050000-950000-sorted.csv", "32-d-050000-950000-unsorted.csv"]


def main(ind):
    if ind < 3:
        col = "source_system_id"
    else:
        col = "ID"

    santeDF = readSanteFile.readIn(santeFiles[ind])  # sante results loaded to a pd df
    testDF = readTestData.readTest(data_files[ind]). \
        sort_values(by=col, ignore_index=True)  # test data results loaded to a pd df

    # # visualise as graphs
    # expectedMatches.printDPlot(testDF)
    # expectedMatches.printPlot(testDF)

    expectedMatches.calc(testDF)
    tpList = evaluate.evaluate(santeDF)     # returns true positive list
    calcFN.calc(testDF[col], tpList)        # calculate the number of false negatives

    weirdFPs.findWeird(santeDF, 0.9)

    viewGold.main(santeDF)


if __name__ == '__main__':
    main(3)
