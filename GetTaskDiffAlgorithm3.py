__author__ = 'Arwa Shaker'
from numpy import *
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


"""computing task difficulty as that, Using Algorithm 3  """
""" This function takes a task as input and return the task difficulty score based on algorithm number 3 """
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# data cleaning
def trimAllColumns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trimStrings = lambda x: x.strip() if type(x) is str else x
    return df.applymap(trimStrings)

def get_task_difficulty_algorithm3(task_df):
    # read skill percentile dataset
    percentage_df = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Ex1/Freelancer_skills_frequency_percent_Ex1.csv')

    percentage_df = trimAllColumns(percentage_df)
    skills_t = task_df.loc['Required_Skills 1':'Required_Skills 5']
    skills_t.fillna('')

    percent = []

    for skill in skills_t:
        for j in range(0, len(percentage_df)):
            if not pd.isna(skill):
                if similar(skill, percentage_df.loc[j, 'skill']) > 0.9:
                    percent.append(percentage_df.loc[j, 'percentile'])
                    print(skill, '', percentage_df.loc[j, 'percentile'])
                    print(percentage_df.loc[j, 'skill'])

    # print(percent)
    if len(percent) != 0  :
        # minmium = min(percent)
        no_skills = skills_t.count()

        sum_of_perce = sum(percent)

        diff = sum_of_perce / no_skills
        diff = 1-diff

        return diff
    else:
        return 0




