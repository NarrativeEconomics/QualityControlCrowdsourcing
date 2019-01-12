__author__ = 'Arwa Shaker'
from numpy import *
import numpy
from sklearn.metrics import jaccard_similarity_score

def create_jaccard_sim_matrix(jobs_profiles):
# extracting only skills columns "attribute"
    jobs_skills = []
    for job in jobs_profiles:
        jobs_skills.append(job[6:11])
   # print(jobs_skills)
    task_jaccard_sim_matrix = []  # creating the similarity matrix


    for job_skills in jobs_skills:
        jscount = sum(x is not "" for x in job_skills) # counting the skills
        for other_job in jobs_skills:
            oscount = sum(x is not "" for x in other_job)
            if jscount >= oscount:
                sim_score = jaccard_similarity_score(job_skills[:jscount], other_job[:jscount])
            else:
                sim_score = jaccard_similarity_score(job_skills[:oscount], other_job[:oscount])
            task_jaccard_sim_matrix.append(sim_score)

   # print("#values in the similarity matrix",len(task_jaccard_sim_matrix)) # |tasks|*|tasks|

    task_jaccard_sim_matrix = reshape(task_jaccard_sim_matrix, (len(jobs_profiles), len(jobs_profiles)))

    # print(task_jaccard_sim_matrix.shape)
    print(task_jaccard_sim_matrix)
    return task_jaccard_sim_matrix