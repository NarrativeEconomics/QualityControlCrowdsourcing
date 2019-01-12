import pandas as pd
import ast
from GetWorkerSkillMatchAlgorithm2 import Algorithm2_Get_task_to_worker_skill_matching

task_df =  pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Jobs_dataset_tokenized_Ex2.csv')
worker_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Freelancer_dataset_with_apply_conf_Ex2.csv',
                        converters={"skill_1_tuple": ast.literal_eval,
                                    "skill_2_tuple": ast.literal_eval,
                                    "skill_3_tuple": ast.literal_eval,
                                    "skill_4_tuple": ast.literal_eval,
                                    "skill_5_tuple": ast.literal_eval,
                                    "skill_6_tuple": ast.literal_eval,
                                    "skill_7_tuple": ast.literal_eval,
                                    "skill_8_tuple": ast.literal_eval,
                                    "skill_9_tuple": ast.literal_eval,
                                    "skill_10_tuple": ast.literal_eval, })


skill_match_matrix_df = pd.DataFrame()
for i in range (0,1):
    for j in range (0, 3):
        score = Algorithm2_Get_task_to_worker_skill_matching(task_df.loc[i], worker_df.loc[j])
        skill_match_matrix_df.loc[worker_df.loc[j,'name'],task_df.loc[i,'TaskID']] = round(score,1)


# skill_match_matrix_df.to_csv('C:/Users/Arwa/Desktop/datasets/Ex2/worker_task_skill_match_Ex2.csv')