from scipy.stats import lognorm
import matplotlib.pyplot as plt
import numpy as np
import csv
from fitter import Fitter
from math import exp

""" lognorm distribution """

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
    freelancers_ratings[3769] = float(freelancers_ratings[5])

    print(len(freelancers_ratings))

    for freelancer in freelancers_ratings:
        if freelancer  == 1:
            freelancers_ratings.remove(freelancer)


    #---------------------------------------------------------------------
    f = Fitter(freelancers_ratings, distributions=['lognorm'])
    f.fit()
    f.summary()
    mean, sigma, shape = f.fitted_param['lognorm']
    plt.show()
    print('mean = ',mean, 'sigma =',sigma,'shape = ',shape)
    #----------------Generate Random Numbers Correlated with this distribution
    s = sigma
    scale = exp(mean)
