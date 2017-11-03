import csv
import pandas as pd
import numpy as np

def main():
    # TODO: figure out how to get CSV file that compiles properly
    myCsvs = ['q01.csv', 'q2.csv', 'q2.csv']
    result = loadCsvsAsMatrix(myCsvs)

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
    for x in range(1, len(files)):
        with open(files[x], encoding="ISO-8859-1") as infile:
            reader = csv.reader(infile, delimiter=',')
            myrows = [rows[0:] for rows in reader]
            # transfer to data frame
            data = np.array(myrows)
            newFrame = pd.DataFrame(data=data[0:, 0:],
                                    columns=data[0, 0:])
            # add data frame to array
            myFiles.append(newFrame)

   # loop through list of CSVs and merge
    for f in myFiles:
        quiz = pd.merge(quiz, f, how='inner', on='id')

    # set id column as index
    quiz = quiz.set_index('id', drop=True)
    print(quiz.shape)

    return quiz


def encodeMatrix(frame):
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