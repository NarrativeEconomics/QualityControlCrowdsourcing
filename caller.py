
import  csv
from GetTaskDifficulty import get_task_difficulty
from CreateJaccardMatrix import create_jaccard_sim_matrix
from CreateSimilarityGraph import create_similarity_graph
from GetWorkerEstimatedAccuracy import get_worker_estimated_accuracy
import numpy
from sklearn.metrics import jaccard_similarity_score
from Taxonomy import create_taxonomy
from ConceptSimilarityMethod import concept_similarity_measure
from smallTaxonomy import create_small_taxonomy
from TaskClustering import tasks_spectral_clustring
from GetTasksSimilarityScore import get_tasks_similarity_score
from SkillFitnessFunction import skill_fitness_function
from GetSkillFrequency import get_skills_frequency

#reading jobs into a list
with open('C:/Users/Arwa/Desktop/jobs.csv') as csvfile:
    jobs_csvfile = csv.reader(csvfile, delimiter=',')
    jobs_profiles = []

    for row in jobs_csvfile:
        jobs_profiles.append(row)


# reading freelancers into a list
with open('C:/Users/Arwa/Desktop/freelancers.csv') as csvfile:
    freelancers_csvfile = csv.reader(csvfile, delimiter=',')
    freelancers_profiles = []

    for row in freelancers_csvfile:
        freelancers_profiles.append(row)

#taxonomy1   = create_taxonomy()


# taxonomy2= create_small_taxonomy()
#print(taxonomy2)

#print("task difficulty score is : ", get_task_difficulty(jobs_profiles[1]))
# print("similarity1",concept_similarity_measure("Websites, IT & Software", "Translation & Languages",taxonomy2))
#print("similarity1",  concept_similarity_measure("JavaFX","Civil Engineering",taxonomy2))
#print("similarity = ", similarity2)
# create_jaccard_sim_matrix(jobs_profiles
create_similarity_graph(jobs_profiles)
#tasks_spectral_clustring(jobs_profiles)
#get_worker_estimated_accuracy(freelancers_profiles[1]) # checks one worker at a time

#print("task_similarity_score",get_tasks_similarity_score(jobs_profiles[13],jobs_profiles[14]))
#print("fitness between worker",freelancers_profiles[0][4],"and task",jobs_profiles[11][0]," is",skill_fitness_function(freelancers_profiles[0],jobs_profiles[11]))

"""takes lists of sets of skills as input and return a file with each skill and it frequencies

#reading all jobs into a list
with open('C:/Users/Arwa/Desktop/jobs_data_final.csv') as csvfile:
    all_jobs_csvfile = csv.reader(csvfile, delimiter=',')

    all_jobs_profiles = []
    for row in all_jobs_csvfile:
        all_jobs_profiles.append(row)

# FROM jobs
jobs_skills = []
for job in all_jobs_profiles:
    jobs_skills.append(job[5:10])
for skill_list in jobs_skills:
    i = 0
    for skill in skill_list:
        skill_list[i] = skill.strip()
        i = i + 1
# this method create a (jobs_skills_frequency.csv) csv file that contains the skills and their frequencies
get_skills_frequency(jobs_skills)"""