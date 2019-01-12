__author__ = 'Arwa Shaker'
""" THIS FUNCTION TAKES A WORKER AND CALCULATE THE WORKER REPUTATION BASED ON THE FORMULA IN CHAPTER 3
with the number of reviewas"""

import pandas as pd

def trimAllColumns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trimStrings = lambda x: x.strip() if type(x) is str else x
    return df.applymap(trimStrings)
#---------------------------------------------------------------------------------------------

def Get_Worker_Reputation_with_review(Worker):
    worker_no_of_reviews = Worker.loc['number_of_reviews']
    workers_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Freelancer_dataset_Ex2.csv')

    workers_df = trimAllColumns(workers_df)

    Rmax = workers_df['number_of_reviews'].max()

    sum_rates = Worker.loc['job_completion_rate'] + \
                Worker.loc['on_budget_rate'] + \
                Worker.loc['on_time_rate'] + \
                Worker.loc['repeat_hire_rate']

    rep = (sum_rates/4) * (worker_no_of_reviews / Rmax)

    return  rep