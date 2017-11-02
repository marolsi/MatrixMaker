import csv
import pandas as pd
import numpy as np

def main():
    myCsvs = ['q01.csv', 'q01.csv', 'q01.csv']
    result = loadCsvsAsMatrix(myCsvs)
    print(result)

def loadCsvsAsMatrix(files):

    # load first csv for reference
    with open(files[0], encoding="ISO-8859-1") as infile:
        reader = csv.reader(infile, delimiter=',')
        myrows = [rows[0:] for rows in reader]

    data = np.array(myrows)
    quiz = pd.DataFrame(data=data[1:, 0:],
                         columns=data[0, 0:])

    # get list with the rest of the csvs
    myFiles = []
    for f in files:
        with open(f, encoding="ISO-8859-1") as infile:
            reader = csv.reader(infile, delimiter=',')
            myrows = [rows[0:] for rows in reader]
        data = np.array(myrows)
        newFrame = pd.DataFrame(data=data[1:, 0:],
                                columns=data[0, 0:])
        myFiles.append(newFrame)

   # loop through list of CSVs and merge
    for f in myFiles:
        quiz = pd.merge(quiz, f, how='inner', on='id')

    quiz.set_index('id')
    return quiz

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