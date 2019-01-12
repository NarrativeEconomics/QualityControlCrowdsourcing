__author__ = 'Arwa Shaker'

""" this function compute the skill matching score between a worker and a task """

from ConceptSimilarityMethod import concept_similarity_measure
from smallTaxonomy import create_small_taxonomy

def skill_fitness_function(w,t):


    # extract skills from worker and task profiles
    skills_t = t[6:11]
    print(skills_t)
    skills_w = w[12:22]
    print(skills_w)
    # ignore the empty cells in task skills
    count = sum(x is not '' for x in  skills_t)
    skills_t = skills_t[:count]
    print(skills_t)

    # ignore the empty cells in task skills
    count = sum(x is not '' for x in skills_w)
    skills_w = skills_w[:count]
    print(skills_w)
    #------------------Fitness Function----------
    fit = []

    # for exact skills
    for skill_w in skills_w:
        for skill_t in skills_t:
            if skill_w == skill_t:
                fit.append(1)   # the score is the highest
                skills_t.remove(skill_t)# remove the skill that was found


    # for inexact skills
    print("skills tasks after 1st check", skills_t)
    if skills_t != None:
        taxonomy = create_small_taxonomy()
        for skill_t in skills_t:
            fit_round = []
            for skill_w in skills_w:
                fit_round.append(concept_similarity_measure(skill_t,skill_w,taxonomy))
            print("similarity between", skill_t,"and all is", fit_round)
            fit.append(max(fit_round))


    print("fitness", fit)
    print(skills_w)
    fit = (sum(fit)/len(fit))
    print("fitness ", fit)
    return fit

