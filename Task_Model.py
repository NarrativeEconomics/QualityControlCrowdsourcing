__author__ = 'Arwa Shaker'

"""send the task and and get the difficulty score then calculate the task cost"""

import pandas as pd
from GetTaskDiffAlgorithm3 import get_task_difficulty_algorithm3

#read Tasks dataset
task_dataset_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Jobs_dataset_tokenized_Ex2.csv')
# iterates over all tasks in the dataset

for i in range(0, len(task_dataset_df)):

    print(task_dataset_df.loc[i])
    task_df = task_dataset_df.loc[i]
    task_diff_score = get_task_difficulty_algorithm3(task_df)
    # store the score in the dataframe
    task_dataset_df.loc[i,'task_diff'] = task_diff_score
    # calculate the task cost using equation number ---
    # task_dataset_df.loc[i, 'task_cost'] = task_dataset_df.loc[i, ' Job_Budget']*

# print(task_dataset_df.loc[1,'Required_Skills 1':'Required_Skills 5'])
# task_diff_score = get_task_difficulty_algorithm3(task_dataset_df.loc[1])

task_dataset_df.to_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Jobs_dataset_diff_with_ave_Ex2.csv')