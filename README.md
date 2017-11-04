### MatrixMaker
This python progam converts quizzes and tests from canvas into matrices that can be processed by machine learning algorithms.

## Using MatrixMaker
- Download quiz/tests from Canvas by selecting a quiz and exporting "student results." 
- Open CSV and manually anonymize (remove names columns) from each quiz/test you'd like to use.
- Create array with the names of your quiz csvs.
- Pass array in as parameter to convert_files_to_matrix.
  - if you'd like your matrix to include data about whether the student got question right/wrong, set use_correctness to True.
  - if you'd like your matrix to include actual multiple choice responses, set use_answer_input to True.
- Save your result to CSV by passing it along with your desired filename into saveMatrix.
