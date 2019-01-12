_author__ = 'Arwa Shaker'

from sklearn import metrics
from sklearn.metrics import pairwise
from sklearn.cluster import spectral_clustering
from sklearn.feature_extraction import DictVectorizer
from editdistance import __all__
def tasks_spectral_clustring(jobs_profiles):
# extracting only skills columns "attribute"
    jobs_skills = {}

    for job in jobs_profiles:
       # jobs_skills.update({'s1':job[6], 's2':job[7], 's3':job[8], 's4':job[9], 's5':job[10]})
        jobs_skills = dict([('s1',job[6]), ('s2',job[7]), ('s3',job[8]), ('s4',job[9]), ('s5',job[10])])

    print(jobs_skills)
    vec = DictVectorizer()
    array = vec.fit_transform(jobs_skills).toarray()
    print(array)