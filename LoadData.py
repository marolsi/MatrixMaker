import csv
import pandas as pd
import numpy as np

def main():
    # TODO: figure out how to get CSV file that compiles properly
    files = ['q01.csv', 'q2.csv']
    compiled_files = compile_csvs(files)
    renamed_files = simplify_column_names(compiled_files)
    matrix = encode_to_matrix(renamed_files)
    print(matrix)

def compile_csvs(files):
    # load first csv for reference
    with open(files[0], encoding="ISO-8859-1") as infile:
        reader = csv.reader(infile, delimiter=',')
        myrows = [rows[0:] for rows in reader]

    data = np.array(myrows)
    quiz = pd.DataFrame(data=data[1:, 0:],
                         columns=data[0, 0:])

    # get list with the rest of the csvs
    my_files = []
    for x in range(1, len(files)):
        with open(files[x], encoding="ISO-8859-1") as infile:
            reader = csv.reader(infile, delimiter=',')
            my_rows = [rows[0:] for rows in reader]
            # transfer to data frame
            data = np.array(my_rows)
            new_frame = pd.DataFrame(data=data[0:, 0:],
                                    columns=data[0, 0:])
            # add data frame to array
            my_files.append(newFrame)

   # loop through list of CSVs and merge
    for f in my_files:
        quiz = pd.merge(quiz, f, how='inner', on='id')

    # set id column as index
    quiz = quiz.set_index('id', drop=True)

    return quiz

def simplify_column_names(df):
    # create array of names
    cols = list(df.columns.values)
    new_cols = cols
    # create new array of adjusted column names
    for x in range(len(cols)):
        if (cols[x][0:2] == '1_'):
            new_cols[x] = cols[x] + '_' + str(x)
        else:
            new_cols[x] = cols[x].split(':')[0]

    # set column names to array of adjusted names
    df.columns = new_cols
    return df

def encode_to_matrix(df):
    # get list of column keys to iterate through
    my_columns = list(df.columns.values)
    # create data frame with id indices
    matrix = pd.DataFrame(data=[],
                          index=df.index.values)
    # iterate through each column and create dummy columns
    for x in range(len(my_columns)):
        key = my_columns[x]
        # don't include correct/incorrect columns, because they're already binary
        if (key[0:2] != '1_'):
            dummiedFrame = pd.get_dummies(df[key])
            matrix = pd.concat([matrix, dummiedFrame], axis=1)
        else:
            matrix = pd.concat([matrix, df[key]], axis=1)

    return matrix

main()