import pandas as pd


def readIn(fileName):
    df = pd.read_csv("/home/bruced/Desktop/SanteMPIResults/" + fileName)

    return splitCol(df)


def splitCol(df):
    for h in ["a", "b"]:
        rec = []
        nid = []
        for row in df[h + "_id_val"]:
            temp = row.split(",")
            if len(temp) == 1:
                rec.append(row)
                nid.append("")
            else:
                if "rec" not in temp[1]:
                    nid.append(temp[1])
                    rec.append(temp[0])
                else:
                    rec.append(temp[1])
                    nid.append(temp[0])

        df[h + "_rec"] = rec
        df[h + "_nid"] = nid

    df.drop(columns="a_id_val", inplace=True)
    df.drop(columns="b_id_val", inplace=True)

    return df
