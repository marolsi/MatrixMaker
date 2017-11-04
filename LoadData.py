import csv
import pandas as pd
import numpy as np


def main():
    # TODO: make more automatic by making a single command with the following params:
        # directory that contains files they want to convert
        # use_correctness, use_answer_input booleans
        # desired filename of output
    # code should take care of removing the names column

    files = ['t2', 't3', 't5', 't4', 'q1', 'q2', 'q3']
    result = convert_files_to_matrix(files, use_correctness=True, use_answer_input=True)
    saveMatrix(result, 'finishedMatrix')


def saveMatrix(matrix, filename):
    matrix.to_csv(filename + '.csv', encoding='utf-8', index=True)


def convert_files_to_matrix(files, use_correctness, use_answer_input):
    """ Takes an array of CSV files, removes inconsistent IDs and converts to matrix.

            Requirements for CSV files:
            - name column should have been previously removed
            - column names follow Canvas default naming conventions

            Paramaters:
            - string of filenames
            - whether to include actual text answers
            - whether to include right/wrong
    """
    compiled_files = compile_csvs(files)
    cleaned_files = cleanup_csvs(compiled_files)
    matrix = encode_to_matrix(cleaned_files, use_correctness, use_answer_input)
    return matrix


def compile_csvs(files):
    # create array of data frames, one frame for each quiz
    my_files = []
    for x in range(len(files)):
        with open(files[x] + ".csv", encoding="ISO-8859-1") as infile:
            reader = csv.reader(infile, delimiter=',')
            my_rows = [rows[0:] for rows in reader]
            # find index of 'attempt' column (could vary, based on teacher's settings)
            attempt_index = my_rows[0].index('attempt')
            for r in my_rows:
                if (r[attempt_index] == '2'): # remove rows with second attempts
                    my_rows.pop(my_rows.index(r))
            # myrows is a 2d array, with each index in the array holding a row of data
            # first row contains column rows
            # following rows each contain data associated with a single student id
            data = np.array(my_rows)
            new_frame = pd.DataFrame(data=data[1:, 0:],
                                     columns=data[0, 0:])
            # add data frame to array
            my_files.append(new_frame)

    # get first quiz so we have an id column to merge on
    quiz = my_files[0]
    # loop through list of quizzes and merge together
    for x in range(1, len(my_files)):
        my_files[x].columns.values[0] = "id"  # make sure id column is named properly
        quiz = pd.merge(quiz, my_files[x], how='inner', on='id')

    # set id column as index, simultaneously dropping id column from dataset
    quiz = quiz.set_index('id', drop=True)
    return quiz


def cleanup_csvs(df):
    # create array of current column names
    cols = list(df.columns.values)
    new_cols = cols
    # create new array of adjusted column names
    for x in range(len(cols)):
        curr = cols[x]
        # make correct/incorrect columns unique
        if ((curr[0] == '1') and (len(curr) < 4)):  # works whether name is '1' or '1_x'
            new_cols[x] = curr + '_' + new_cols[x - 1][3:]  # append associated question id (previous column), without 'q: '
        elif (':' in curr):
            # delete question text, leaving only question id number
            # this will still include columns we don't want, such as attempt number
            new_cols[x] = 'q: ' + curr.split(':')[0]

    # set column names to array of adjusted names
    df.columns = new_cols
    return df


def encode_to_matrix(df, use_correctness, use_answer_input):
    # get list of column keys to iterate through
    my_columns = list(df.columns.values)
    # create data frame with id index to use for appending
    matrix = pd.DataFrame(data=[],
                          index=df.index.values)
    # iterate through each column key and append only the columns we want
    for x in range(len(my_columns)):
        key = my_columns[x]
        if use_answer_input:
            if 'q:' in key:
                dummied_frame = pd.get_dummies(df[key])  # dummify into frame of multiple binary variables
                matrix = pd.concat([matrix, dummied_frame], axis=1)
        if use_correctness:
            if (key[0:2] == '1_'):
                matrix = pd.concat([matrix, df[key]], axis=1)  # don't dummify; already binary
    return matrix


main()
