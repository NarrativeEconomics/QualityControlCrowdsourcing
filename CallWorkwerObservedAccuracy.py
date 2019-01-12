from GetWorkerObservedAccuracy import Get_Worker_Observed_Accuracy
from GetWorkerObservedAccuracyWithTaskDifficulty import Get_Worker_Observed_Accuracy_with_task_diff
import pandas as pd


worker_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Freelancer_dataset_Ex2.csv')
task_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Jobs_dataset_diff_with_ave_Ex2.csv')

# for i in range (0,len(task_df)):
#     for j in range (0, len(worker_df)):
#         worker_df.loc[j,task_df.loc[i, 'TaskID']] =\
#             Get_Worker_Observed_Accuracy(worker_df.loc[j],task_df.loc[i])
#
#         print('worker =', worker_df.loc[j,'name'],'q =',worker_df.loc[j, task_df.loc[i,'TaskID']])


workerObsAcc_df = pd.DataFrame()

for i in range (0,len(task_df)):
    for j in range (0, len(worker_df)):
        workerObsAcc_df.loc[worker_df.loc[j,'name'],task_df.loc[i, 'TaskID']] = \
            Get_Worker_Observed_Accuracy_with_task_diff(worker_df.loc[j],task_df.loc[i])


workerObsAcc_df.to_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Freelancer_dataset_Worker_observed_diff_with_ave_Ex2.csv')