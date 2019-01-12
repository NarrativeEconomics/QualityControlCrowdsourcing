__author__ = 'Arwa Shaker'
"""this function takes two tasks and return the similarity score based on 
concept similarities between their skills"""



from ConceptSimilarityMethod import concept_similarity_measure
from smallTaxonomy import create_small_taxonomy

def get_tasks_similarity_score(t1,t2):
    taxonomy = create_small_taxonomy()
    max_sim = []
    max_of_max = []
    
    # extract only skills from tasks profiles
    skills_t1 = t1[6:11]
    skills_t2 = t2[6:11]

    print('task 1 skills',skills_t1)
    print('task 2 skills', skills_t2)
    skill_t1_count = sum(x is not "" for x in skills_t1)  # counting the skills
    skills_t1 = skills_t1[:skill_t1_count]
    skill_t2_count = sum(x is not "" for x in skills_t2)  # counting the skills
    skills_t2 = skills_t2[:skill_t2_count]
    out_rounds = 0
    in_rounds = 0
    #-------------------------------------------------------------------------------
    for s1 in skills_t1:
        sim_list = []
        for s2 in skills_t2:

            in_rounds = in_rounds + 1
            print("in_round = ", in_rounds)
            if s1 == s2:
                #print("---------------------------------------------------")
                #print("similarity between ", s1, "and", s2, "is", 1)
                #print("---------------------------------------------------")
                sim_list.append(1) # gives the highest score which is the value of 1
                skills_t2.remove(s2)
                break
            else:
                sim_list.append(concept_similarity_measure(s1,s2,taxonomy))
        out_rounds = out_rounds + 1
        print("round = ", out_rounds)
        print("task 1 skills after round", skills_t1)
        print("task 2 skills after round", skills_t2)
        print("similarity between ", s1, "and all", "is", sim_list)
        max_sim.append(max(sim_list)) # in each comparison round tasks the maximum score
        print("---------------------------------------------------")
        print("max in    list ", max_sim)


    max_of_max.append(max(max_sim))# takes the max of the max score

    return max_of_max
