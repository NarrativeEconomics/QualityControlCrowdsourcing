__author__ = 'Arwa Shaker'
"""this Algorithm takes a task and a worker and return the match score """

from ConceptSimilarityMethod_Ex1 import concept_similarity_measure_ex1
import numpy as np
def is_nan(x):
    return (x is np.nan or x != x)

def Algorithm2_Get_task_to_worker_skill_matching(task,worker):

    skills_t = task.loc['Required_Skills 1':'Required_Skills 5']
    skills_w = worker.loc['skill_1_tuple':'skill_10_tuple']
    skills_t.fillna('')
    skills_w.fillna('')
    print('task skills ', skills_t)
    print('worker skills ', skills_w)


    max_sim_list = []
    weight_list = []
    for s1 in skills_w:
        sim_list = []
        if s1[0] != '':
            for s2 in skills_t:
                if not is_nan(s2):
                    sim,l1,l2 = concept_similarity_measure_ex1(s2,s1[0])
                    if sim != 0 :
                        sim_list.append(sim)


        if sim_list != []:
            print("sim list", sim_list)
            max_sim = max(sim_list)
            max_sim= max_sim * float(s1[1])  # multiply by the confident score
            max_sim_list.append(max_sim)
            weight_list.append(s1[1])

    print('max list', max_sim_list)
    print('max_sim',sum(max_sim_list))
    print('sum(weight_list)', sum(weight_list))
    sum_max = sum(max_sim_list)
    sum_weight = sum(weight_list)

    if sum_weight != 0:
        skill_match_score = sum_max / sum_weight
    else:
        skill_match_score = 0.0
    print('skill_match_score',skill_match_score)
    return skill_match_score