""" This Code is for Solving the worker-task assignment Problems as
an Optimization Problem Using PuLP/Python """

import pulp
from pulp import *
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from IPython.display import Image


# read the freelancers data set as pandas dataframe
freelancers_profiles = pd.read_csv('C:/Users/Arwa/Desktop/datasets/Freelancers_Data_final.csv')
# read the jobs data set as pandas dataframe
jobs_profiles = pd.read_csv('C:/Users/Arwa/Desktop/datasets/jobs_data_final.csv')


# Instantiate our problem class
model = pulp.LpProblem("global task value maximization problem", pulp.LpMaximize)
# Construct our decision variable lists

