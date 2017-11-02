import csv
import pandas as pd
import numpy as np

def main():
    csv1 = loadCsvAsMatrix2('q01.csv')
    csv2 = loadCsvAsMatrix2('q2.csv')
    result = pd.concat([csv1, csv2], axis=1)
    print(result)

def loadCsvAsMatrix(filename):
    with open(filename, encoding="ISO-8859-1") as infile:
        reader = csv.reader(infile, delimiter=',')
        myrows = [rows[0:] for rows in reader]

    columns = []
    # iterate through number of columns
    for x in range(len(myrows[0])):
        # iterate through rows to get xth value to yth column
        column = []
        for y in range(len(myrows)):
            column.append(myrows[y][x])
        columns.append(column)

    # for every array in columns
    for x in range(1, len(columns)):
        # iterate through array and convert
        columns[x] = pd.get_dummies(columns[x])

    # separate ids
    myids = columns[0]
    columns.pop(0)
    print(len(columns[0]))
    print(len(myids))

    myIndices = {}
    # prepare dictionary for indexing
    for x in range(len(myids)):
        myIndices[x] = myids[x]

    print(myIndices)
    # reconcatenate columns into matrix
    # loop through every column to concatenate
    frame = []
    for x in range(len(columns)):
        frame.append(columns[x])

    result = pd.concat(frame, axis=1)
    result.rename(myIndices)
    print(result)
    return result

def mergeFiles(files):
    f1 = files[0]
    f2 = files[1]


def loadCsvAsMatrix2(filename):
    with open(filename, encoding="ISO-8859-1") as infile:
        reader = csv.reader(infile, delimiter=',')
        myrows = [rows[0:] for rows in reader]

    data = np.array(myrows)
    myframe = pd.DataFrame(data=data[1:,1:],
                            index=data[1:,0],
                            columns=data[0,1:])
    encodeMatrix(myframe)
    return myframe

def encodeMatrix(frame):
    # TODO: better understand
    df = pd.get_dummies(frame, columns='1')
    print(df)

    # columns = []
    # # iterate through number of columns
    # for x in range(len(myrows[0])):
    #     # iterate through rows to get xth value to yth column
    #     column = []
    #     for y in range(len(myrows)):
    #         column.append(myrows[y][x])
    #     columns.append(column)
    #
    # # for every array in columns
    # for x in range(1, len(columns)):
    #     # iterate through array and convert
    #     columns[x] = pd.get_dummies(columns[x])
    #
    # print(type(columns))
    # # reconcatenate columns into matrix
    # # loop through every column to concatenate
    # frame = []
    # for x in range(len(columns)):
    #     frame.append(columns[x])
    # print(type(columns))
    # result = pd.concat(frame, axis=1)



main()