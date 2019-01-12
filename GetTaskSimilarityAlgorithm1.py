__author__ = 'Arwa Shaker'
"""this Algorithm takes two tasks and return the similarity score """
import numpy as np
from ConceptSimilarityMethod_Ex1 import concept_similarity_measure_ex1
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def is_nan(x):
    return (x is np.nan or x != x)
def Algorithm1_Get_task_to_task_similarity(task1,task2):

    # Calculate similarity between titles of the tasks L^(t_1 ) and L^(t_2 ) using cosine similarity

    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    print("task1.loc['Job_Title']",task1.loc['Job_Title'])
    print("task2.loc['Job_Title']", task2.loc['Job_Title'])
    if task1.loc['Job_Title']!= '' and task2.loc['Job_Title']!= '':
        data = [
            task1.loc['Job_Title'],
            task2.loc['Job_Title']
                ]

        # Vectorise the data
        vec = TfidfVectorizer()

        X = vec.fit_transform(data)  # `X` will now be a TF-IDF representation of the data, the first row of `X` corresponds to the first sentence in `data`

        # Calculate the pairwise cosine similarities (depending on the amount of data that you are going to have this could take a while)
        S = cosine_similarity(X)
        Title_Sim = S[0,1]
    else:
        Title_Sim = 0
    print('similarity of titles:', Title_Sim)
    #----------------------------------------------------------------------------------------------------------
    ####Data Cleaning------------------------------------------------------------------------------------------


    skills_t1 = task1.loc['Required_Skills 1':'Required_Skills 5']
    skills_t2 = task2.loc['Required_Skills 1':'Required_Skills 5']
    print(skills_t1,'skills_t1')
    print(skills_t2,'skills_t2')
    # Keep the task with the loser number of skills first


    i = 0


    sim_df = pd.DataFrame()

    for s1 in skills_t1:

        sim_list = []
        if not is_nan(s1):

            for s2 in skills_t2:

                if not is_nan(s2):
                    print("s1", s1)
                    print("s2", s2)
                    sim, l1, l2 = concept_similarity_measure_ex1(s1, s2)  # this function returns a tuple (sim, l1,l2)
                    sim = float(sim)  # convert to floats
                    sim_df.loc[s1, s2] = sim

                    sim_list.append(sim)
            print('sim_list of round #', i, "is  ", sim_list)
            print("____________________________________________________________________________________________")
            i = i + 1

    sim_vec_df = pd.DataFrame()
    for s in skills_t1:
        if not is_nan(s):
            sim_vec_df.loc['t1', s] = 0.0
    for s in skills_t2:
        if not is_nan(s):
            sim_vec_df.loc['t1', s] = 0.0
    for s in skills_t1:
        if not is_nan(s):
            sim_vec_df.loc['t2', s] = 0.0
    for s in skills_t2:
        if not is_nan(s):
            sim_vec_df.loc['t2', s] = 0.0

    # set the skills of t1 to 1 in v1
    for skill in skills_t1:
        if not is_nan(skill):
            sim_vec_df.loc['t1', skill] = 1.0

    # set the skills of t2 to 1 in v2
    for skill in skills_t2:
        if not is_nan(skill):
            sim_vec_df.loc['t2', skill] = 1.0

        # set the skills of t2 to the max in v1
    for skill in skills_t2:
        if not is_nan(skill):
            sim_vec_df.loc['t1', skill] = sim_df[skill].max()

    # set the skills of t1 to t2 in v2

    for skill in skills_t1:
        if not is_nan(skill):
            sim_vec_df.loc['t2', skill] = sim_df.loc[skill].max()


    v1 = sim_vec_df.loc['t1'].values
    v1 = v1.reshape(1, -1)
    v2 = sim_vec_df.loc['t2'].as_matrix()
    v2 = v2.reshape(1, -1)

    print('V1',v1)
    print('V2', v2)
    skill_similarity = cosine_similarity(v1, v2)

    C1 = 0.3
    C2 = 0.7
    task_2_task_similarity_score = C1*Title_Sim + C2*skill_similarity
    # task_2_task_similarity_score = round(task_2_task_similarity_score, 1)


    return task_2_task_similarity_score