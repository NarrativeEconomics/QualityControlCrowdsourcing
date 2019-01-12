__author__ = 'Arwa Shaker'
"""This algorithm tries to assign the most difficult tasks first. As they require skills 
that are rare in the crowd. i.e. trying to save the workers who have rare skills from 
being assigned to easy tasks leaving the difficult tasks unassigned. The set of incoming
tasks is sorted in descending order using the value of the difficulty function dif(t). 
For each task in the ordered list the worker pool is searched for the fitted workers based 
on the value of the fitness function.Then a top k worker is elected to the task and the task
will be assigned. """
import csv
from numpy import *
from GetTaskDifficulty import get_task_difficulty
from GetWorkerEstimatedAccuracy import get_worker_estimated_accuracy

# reading freelancers into a list
with open('C:/Users/Arwa/Desktop/freelancers.csv') as csvfile:
    freelancers_csvfile = csv.reader(csvfile, delimiter=',')
    freelancer_profiles = []

    for row in freelancers_csvfile:
        freelancer_profiles.append(row)

# reading jobs into a list
with open('C:/Users/Arwa/Desktop/jobs.csv') as csvfile:
    jobs_csvfile = csv.reader(csvfile, delimiter=',')
    jobs_profiles = []

    for row in jobs_csvfile:
        jobs_profiles.append(row)

# getting the task difficulties for incoming tasks t2,t4,t12
    T = []
    for job in jobs_profiles:
        if job[2] == "":
            T.append(job)

    # Get Task Difficulty -------------------------------------------------
    Tdif = []
    for t in T:
        Tdif.append(t[0])
        Tdif.append(get_task_difficulty(t))
    Tdif = reshape(Tdif,(len(T),2))
    # Sort Tasks By Difficulty in a Descending - most Difficult tasks first
    Tdif = sorted(Tdif,key=lambda x: x[1],reverse=True)

    # getting the estimated accuracies of active (available) workers-------
    estimated_accuracy = []
    for freelancer in freelancer_profiles:
        estimated_accuracy.append(freelancer[4])
        estimated_accuracy.append(get_worker_estimated_accuracy(freelancer))

    for accuracy in estimated_accuracy:
        print("\n",accuracy)

    # IDENTIFY THE TOP K WORKERS FOR A GIVEN TASK--------------------------




