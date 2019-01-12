__author__ = 'Arwa Shaker'
"""implementing the graph-based-accuracy estimation that was proposed in 
(iCrowd: An Adaptive Crowdsourcing Framework)- New Version """

import csv
from CreateJaccardMatrix import create_jaccard_sim_matrix
from CreateSimilarityGraph import create_similarity_graph
from WorkerObservedAccuracy import worker_observed_accuracy
import numpy
from numpy import *


def get_worker_estimated_accuracy_Ex1(freelancer):

    # reading jobs into a list
    with open('C:/Users/Arwa/Desktop/datasets/Example_jobs.csv') as csvfile:
        jobs_csvfile = csv.reader(csvfile, delimiter=',')
        jobs_profiles = []

        for row in jobs_csvfile:
            jobs_profiles.append(row)

        S = create_jaccard_sim_matrix(jobs_profiles) # S is the tasks similarity matrix
        G = create_similarity_graph(jobs_profiles) # G is the tasks similarity graph
        n = numpy.sqrt(S.size) # get S matrix size (float)
        n = int(n) # make it integer
        D = numpy.zeros((n,n)) # set array elements to zero

        # Computing the Diagonal matrix D
        for i in range(0,n):
            for j in range(0,n):
                D[i][i] = D[i][i] + S[i][j]

        # Computing the Normalized similarity
        Sdash = numpy.zeros((n,n))  # declaration
        D_tpomh = numpy.zeros((n,n))  # D to the power of minus 1/2

        """----the diagonal matrix to the power of -1/2-----"""
        """------ compute the inverse of D"""
        for i in range(0, n):
            for j in range(0, n):
                D_tpomh[i][i] = 1/numpy.sqrt(D[i][i])   # only diagonal elements

        """-----the normalized Similarity ------"""
        Sdash = D_tpomh @ S @ D_tpomh

       # print("Similarity Matrix",S)
       # print("Diagonal",D)
      #  print("Normalized similarity",Sdash)
      #   worker_observed_accuracies = worker_observed_accuracy(freelancer,jobs_profiles)
        worker_observed_accuracies = [0.2,0.1,0.1,1,0.5,1,0.3,0.1,0.1,0.02,0.2]
        worker_estimated_accuracies = []

        p = numpy.array(worker_estimated_accuracies)
        q = numpy.array(worker_observed_accuracies)

        p = q
        k = len(q)  # get q matrix size (float)
        k = int(k)  # make it integer
        z = numpy.zeros((k))  # set array elements to zero

        for i in range(0, k):
            z[i] = 0.0001  # when should we stop

        """print("\n p",p)
        print(p.dtype)
        print("\n q", q)
        print(p.dtype)
        print("\n z", z)
        print(p.dtype)"""

         # difference between the observed vector and the estimated vector
        # converge = 1
        # """ Equation (4)"""
        # while numpy.any(converge >= z):  # until reach convergence
        #     pOld = p
        #     p = ((1/(1+1.0)* p)  @ Sdash) + ((1.0/(1+1.0)) * q)
        #     converge = numpy.subtract(p, pOld)
        #     print("\n round",p)
        #
        # # print("\n worker_observed_accuracies",q)
        # # print("\n worker_estimated_accuracies", p)
        #
        # return p