__author__ = 'Arwa Shaker'
""" THIS FUNCTION TAKES A WORKER AND CALCULATE THE WORKER REPUTATION BASED ON THE FORMULA IN CHAPTER 3"""

import pandas as pd

def trimAllColumns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trimStrings = lambda x: x.strip() if type(x) is str else x
    return df.applymap(trimStrings)
#---------------------------------------------------------------------------------------------

def Get_Worker_Reputation(Worker):
    worker_no_task_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/worker_number_of_task.csv',
                        names=['Freelancer_name','no_of_tasks'])

    worker_no_task_df = trimAllColumns(worker_no_task_df)


    sum_rates = Worker.loc['job_completion_rate'] + \
                Worker.loc['on_budget_rate'] + \
                Worker.loc['on_time_rate'] + \
                Worker.loc['repeat_hire_rate']

    Tw = 0
    for i in range (0,len(worker_no_task_df)):
        if worker_no_task_df.loc[i,'Freelancer_name'] == Worker.loc['name']:
            Tw = worker_no_task_df.loc[i,'no_of_tasks']

    Tmax = worker_no_task_df['no_of_tasks'].max()

    rep = (sum_rates/4) * (Tw / Tmax)

    return  rep