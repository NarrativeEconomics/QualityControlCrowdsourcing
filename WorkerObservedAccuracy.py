__author__ = 'Arwa Shaker'

"""calculate worker observed accuracy
for the pefromed tasks from user feedback and from uniform distribution for unperformed tasks"""


import numpy


def worker_observed_accuracy(worker, jobs_profiles):
    with open('UiformDistributionFile.txt', 'r') as unifile:
        uniform_dis = []
        for line in unifile:
            uniform_dis.append(line)

        q = numpy.zeros(len(jobs_profiles))

        i = 0
        for job in jobs_profiles:

            if worker[4] == job[2]:
                q[i] = (job[14])
            else:
                q[i] = uniform_dis[i]
            i = i + 1

        print("\n q before send",q)
        return q

