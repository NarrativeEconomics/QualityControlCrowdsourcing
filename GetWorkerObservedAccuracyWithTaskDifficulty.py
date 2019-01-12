__author__ = 'Arwa Shaker'
""" THIS FUNCTION TAKES A WORKER AND CALCULATE THE WORKER OBSERVED ACCURACY CHAPTER 3"""


#---------------------------------------------------------------------------------------------

def Get_Worker_Observed_Accuracy_with_task_diff(Worker,task):

    # ----- Give the value of Zero for unperformed tasks
    if Worker.loc['name'] != task.loc['Freelancer_username']:
        return 0

    else:
        rating = Worker.loc['rating']
        task_diff = task.loc['task_diff']

        q = (rating/5) * task_diff
        return q