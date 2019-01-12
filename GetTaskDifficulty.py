__author__ = 'Arwa Shaker'

"""computing task difficulty as that, tasks require skills 
that are rare in the crowd considered more difficult """

from numpy import *
import csv


def get_task_difficulty(job):
    # reading freelancers into a list
    with open('C:/Users/Arwa/Desktop/Freelancers_all.csv') as csvfile:
        freelancers_csvfile = csv.reader(csvfile, delimiter=',')
        freelancers_profiles = []

        for row in freelancers_csvfile:
            freelancers_profiles.append(row)
    # extracting only skills columns "attribute"
    # FROM TASKS
    job_skills = job[6:11]

    # FROM WORKERS
    freelancers_skills = []
    for freelancer in freelancers_profiles:
        freelancers_skills.append(freelancer[9:19])
    # compute the frequencies of skills
    def map_skills(freelancers_skills):
        hash_map = {}

        for freelancer_skills in freelancers_skills:
            if freelancer_skills is not None:
                for skill in freelancer_skills:
                    if skill is not '':
                        # skill Exist?
                        if skill in hash_map:
                            hash_map[skill] = hash_map[skill] + 1
                        else:
                            hash_map[skill] = 1

        return hash_map


    # Create a Hash Map (Dictionary)
    map = map_skills(freelancers_skills)

    # Show skill Information
    for skill in map:
      print('skill: [' + skill + '] Frequency: ' , map[skill])

    percentage =  {}
    # compute the total number of skills
    total  = 0
    for skill in map:
        total  = total  + map[skill]


    # compute the percentage of each skill
    for skill in map:
        percentage[skill] = (map[skill]/total) * 100

    # Show skill Information
    for skill in map:
       print('skill: [' + skill + '] Percentage: ' ,percentage[skill])
    # write it to a text file
    with open('workers_skills_frequency.csv', 'w') as file:
        for skill in map:
            print(skill,',',map[skill], file=file)


    # ignore empty cells [count only the skills of the task]
    count = sum(x is not "" for x in job_skills)
    act_skills = job_skills[:count]

    task_difficulty = (1- min(percentage[skill] for skill in act_skills )) # IS THIS CORRECT
    return task_difficulty

