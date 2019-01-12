__author__ = 'Arwa Shaker'
""" THIS FUNCTION COMPUTE THE WORKER SKILL CONFIDENCE SCORE BASE ON THE WORKER WORK HISTORY AS SUCH : 
IF THE WORKER HAD PERFORMED A TASK REQUIRES THAT SKILL THE WORKER GETS 1 AND 0.5 OTHER WISE IN CHAPTER 3"""
import pandas as pd
import ast

def trimAllColumns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trimStrings = lambda x: x.strip() if type(x) is str else x
    return df.applymap(trimStrings)

#---------------------------------------------------------------------------------------------------
worker_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Freelancer_dataset_Ex2.csv')
print(len(worker_df))
worker_df = worker_df.drop_duplicates(subset = 'name')
print(len(worker_df))
worker_df = worker_df.reset_index()
worker_df = worker_df.fillna('')


##------------------- adding confident value to each skill ---------------------------
for i in range (0, len(worker_df)):
    if worker_df.loc[i, 'skilks 1'] != '':
        worker_df.loc[i, 'conf_skill_1'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_1'] = ''

    if worker_df.loc[i, 'skilks 2'] != '':
        worker_df.loc[i, 'conf_skill_2'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_2'] = ''

    if worker_df.loc[i, 'skilks 3'] != '':
        worker_df.loc[i, 'conf_skill_3'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_3'] = ''

    if worker_df.loc[i, 'skilks 4'] != '':
        worker_df.loc[i, 'conf_skill_4'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_4'] = ''

    if worker_df.loc[i, 'skilks 5'] != '':
        worker_df.loc[i, 'conf_skill_5'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_5'] = ''

    if worker_df.loc[i, 'skilks 6'] != '':
        worker_df.loc[i, 'conf_skill_6'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_6'] = ''

    if worker_df.loc[i, 'skilks 7'] != '':
        worker_df.loc[i, 'conf_skill_7'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_7'] = ''

    if worker_df.loc[i, 'skilks 8'] != '':
        worker_df.loc[i, 'conf_skill_8'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_8'] = ''

    if worker_df.loc[i, 'skilks 9'] != '':
        worker_df.loc[i, 'conf_skill_9'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_9'] = ''

    if worker_df.loc[i, 'skilks 10'] != '':
        worker_df.loc[i, 'conf_skill_10'] = 0.5
    else:
        worker_df.loc[i, 'conf_skill_10'] = ''



worker_df.to_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Freelancer_dataset_with_conf_Ex2.csv')
#-----------------------------------------------------------------------------------------------------


combined_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/jobs_and_freelancers_combined_Ex2.csv')
worker_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Freelancer_dataset_with_conf_Ex2.csv')

worker_df = worker_df.fillna('')

combined_df = trimAllColumns(combined_df)
worker_df = trimAllColumns(worker_df)

# LOOP ALL WORKERS
for i in range (0, len(worker_df)):
    # take the worker history  -------------------
    worker_his_df = combined_df.loc[combined_df['name'] == worker_df.loc[i,'name']]
    #select the skills for the worker and the task
    skills_t = worker_his_df.loc[:, 'Required_Skills 1':'Required_Skills 5']
    skills_w = worker_his_df.loc[:, 'skilks 1':'skilks 10']

    skills_t = skills_t.melt()
    skills_t = skills_t.loc[:, 'value']
    skills_t = skills_t.drop_duplicates()
    skills_t = skills_t.dropna()

    skills_w = skills_w.melt()
    skills_w = skills_w.loc[:, 'value']
    skills_w = skills_w.drop_duplicates()
    skills_t = skills_t.dropna()

    for s1 in skills_w:
        for s2 in skills_t:
            # print('s1',s1,'------','s2',s2)
            if s1 == s2:
                # print('YESSSSSS')
                if s1 in worker_df.loc[i,'skilks 1']:
                    worker_df.loc[i, 'conf_skill_1'] = 1.0

                if s1 in worker_df.loc[i,'skilks 2']:
                    worker_df.loc[i, 'conf_skill_2'] = 1.0


                if s1 in worker_df.loc[i,'skilks 3']:
                    worker_df.loc[i, 'conf_skill_3'] = 1.0

                if s1 in worker_df.loc[i,'skilks 4']:
                    worker_df.loc[i, 'conf_skill_4'] = 1.0

                if s1 in worker_df.loc[i,'skilks 5']:
                    worker_df.loc[i, 'conf_skill_5'] = 1.0

                if s1 in worker_df.loc[i,'skilks 6']:
                    worker_df.loc[i, 'conf_skill_6'] = 1.0

                if s1 in worker_df.loc[i,'skilks 7']:
                    worker_df.loc[i, 'conf_skill_7'] = 1.0

                if s1 in worker_df.loc[i,'skilks 8']:
                    worker_df.loc[i, 'conf_skill_8'] = 1.0

                if s1 in worker_df.loc[i,'skilks 9']:
                    worker_df.loc[i, 'conf_skill_9'] = 1.0

                if s1 in worker_df.loc[i,'skilks 10']:
                    worker_df.loc[i, 'conf_skill_10'] = 1.0



#------- combine each skill with the confident value in a tuple -------
worker_df['skill_1_tuple'] = worker_df[['skilks 1','conf_skill_1']].apply(tuple, axis=1)
worker_df['skill_2_tuple'] = worker_df[['skilks 2','conf_skill_2']].apply(tuple, axis=1)
worker_df['skill_3_tuple'] = worker_df[['skilks 3','conf_skill_3']].apply(tuple, axis=1)
worker_df['skill_4_tuple'] = worker_df[['skilks 4','conf_skill_4']].apply(tuple, axis=1)
worker_df['skill_5_tuple'] = worker_df[['skilks 5','conf_skill_5']].apply(tuple, axis=1)
worker_df['skill_6_tuple'] = worker_df[['skilks 6','conf_skill_6']].apply(tuple, axis=1)
worker_df['skill_7_tuple'] = worker_df[['skilks 7','conf_skill_7']].apply(tuple, axis=1)
worker_df['skill_8_tuple'] = worker_df[['skilks 8','conf_skill_8']].apply(tuple, axis=1)
worker_df['skill_9_tuple'] = worker_df[['skilks 9','conf_skill_9']].apply(tuple, axis=1)
worker_df['skill_10_tuple'] = worker_df[['skilks 10','conf_skill_10']].apply(tuple, axis=1)


worker_df.to_csv('C:/Users/Arwa/Desktop/datasets/Ex2/Freelancer_dataset_with_apply_conf_Ex2.csv')

