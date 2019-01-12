__author__ = 'Arwa Shaker'

import csv
import matplotlib.pyplot as plt
import scipy.stats
from fitter import Fitter
from scipy.stats import halfcauchy,powernorm
from pylab import linspace, plot
import  numpy as np
import pandas as pd
import plotly.plotly as py

with open('C:/Users/Arwa/Desktop/Freelancers_all - Copy.csv') as csv_file:
    freelancers_csv_file = csv.reader(csv_file, delimiter=',')

    freelancer_profiles = []
    for row in freelancers_csv_file:
        freelancer_profiles.append(row)

    # extracting only the ratings
    freelancers_ratings = []

    for freelancer in freelancer_profiles:
        freelancers_ratings.append(freelancer[4])

    for i in range(0,3769):
        freelancers_ratings[i] = float(freelancers_ratings[i])

    freelancers_ratings[3769] =  float(freelancers_ratings[5])

    print(freelancers_ratings)
    # --- plotting the dataset ---------
    plt.hist(freelancers_ratings)
   # plt.show()
    #------fitting the dataset ---------
    dist = 'halfcauchy'
    # after running >>>f = Fitter(freelancers_ratings)
    f = Fitter(freelancers_ratings, distributions=[dist] )
    f.fit()
    # may take some time since by default, all scipy.stats.halfcauchys are tried
    # but you call manually provide a smaller set of scipy.stats.halfcauchys
    f.summary()
    print(f.fitted_param[dist])  # (1.2399422931421155e-05, -0.15101111649750565, 0.0008105405858818151)
    scale = 0.029174867465985424
    loc = -3.102052154197483e-09
    c = 4.45  # shape parameter
    powernorm.pdf(freelancers_ratings, c, loc, scale)
    plt.show()