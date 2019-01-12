import pandas as pd
from GetTaskSimilarityAlgorithm1 import Algorithm1_Get_task_to_task_similarity



task_df =  pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Jobs_dataset_tokenized_Ex2.csv')
# task_df = task_df.fillna('')

similarity_matrix = pd.DataFrame()

similarity_matrix_df = pd.DataFrame()

# for i in range (0,len(task_df)):
#      for j in range (0,len(task_df)):
#         Sim = Algorithm1_Get_task_to_task_similarity(task_df.loc[i],task_df.loc[j])
#         similarity_matrix_df.loc[task_df.loc[i, 'TaskID'], task_df.loc[j, 'TaskID']] = Sim
#
# similarity_matrix_df.to_csv('C:/Users/Arwa/Desktop/datasets/Ex1/Jobs_similarity_matrix_Ex1.csv')

Sim = Algorithm1_Get_task_to_task_similarity(task_df.loc[0],task_df.loc[9])
print('sim(t3,t9) = ', Sim)
Sim = Algorithm1_Get_task_to_task_similarity(task_df.loc[9],task_df.loc[0])
print('sim(t9,t3) = ', Sim)