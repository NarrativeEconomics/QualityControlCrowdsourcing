__author__ = 'Arwa Shaker'
""" THIS FUNCTION TAKES A WORKER AND CALCULATE THE WORKER OBSERVED ACCURACY CHAPTER 3"""

import pandas as pd

def trimAllColumns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trimStrings = lambda x: x.strip() if type(x) is str else x
    return df.applymap(trimStrings)
#---------------------------------------------------------------------------------------------

def Get_Worker_Observed_Accuracy(Worker,task):

    # ----- Give the value of Zero for unperformed tasks
    if Worker.loc['name'] != task.loc['Freelancer_username']:
        return 0

    else:
        combined_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/jobs_and_freelancers_combined_Ex2.csv')
        combined_df = trimAllColumns(combined_df)
        #take the worker history  -------------------
        worker_his_df = combined_df.loc[combined_df['name'] == Worker.loc['name']]

        # the number of performed tasks in the same category as t in worker profile
        worker_cat_no_task = worker_his_df.groupby('Job_Category').size()
        TwCat = worker_cat_no_task[task.loc['Job_Category']]

        # the number of tasks in the task performed task category  -------------------
        task_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex1/Jobs_dataset_tokenized_Ex1.csv')
        task_df.fillna('')


        cat_no_task = task_df.groupby('Job_Category').size()

        Tcat = cat_no_task[task.loc['Job_Category']]
        print('task category', task.loc['Job_Category'])
        rating = Worker.loc['rating']




        if Tcat == 0:
            Tcat = 1

        print('Tcat =', Tcat, 'Tw =', TwCat)
        q = (rating/5) * (TwCat / Tcat)

        return q