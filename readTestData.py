import pandas as pd


def readTest(fileName):

    df = pd.read_csv("/home/bruced/Desktop/TestData/" + fileName)

    return df[[col for col in df.columns[:8]]]
