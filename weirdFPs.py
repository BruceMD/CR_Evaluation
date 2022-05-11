import pandas as pd


def findWeird(df, level):
    weirdMatches = []

    for row in df.itertuples():
        if row.confidence > level and row.a_rec[:12] != row.b_rec[:12]:
            weirdMatches.append(row[1:])

#    print(weirdMatches)

    weirdDF = pd.DataFrame(data=weirdMatches, columns=df.columns)
    weirdDF.to_csv("/home/bruced/Desktop/file.csv")

    print("wFPs:", len(weirdDF))

    return weirdDF
