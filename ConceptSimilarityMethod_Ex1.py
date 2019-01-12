__author__ = 'Arwa Shaker'
""" THIS METHOD IS ADOPTED FROM THIS WORK 
(VERB SEMANTICS AND LEXICAL SELECTION)
WHICH IS AN IMPLEMENTATION TO THE Wu AND PALMER MEASURE """


from ete3 import TreeNode,Tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def concept_similarity_measure_ex1(C1, C2):

    taxonomy = Tree("skills_taxonomy_tree_level_score.nw")
    # print("C1",C1,"\n","C2",C2)
    #taxonomy.show()

    N1 = 0 # the distance from Concept 1 to the least common subsumer
    N2 = 0 # the distance from Concept 2 to the least common subsumer
    N = 0  # the distance from  the least common subsumer to the root
    """ -----------------L   he shortest path between the tow concepts------------------------------"""


    node1 = taxonomy.search_nodes(name=C1)
    node2 = taxonomy.search_nodes(name=C2)
    # print('node1', node1)
    # print('node2', node2)
    # if the skill is not found in the taxonomy
    if node1 == [] or node2 == []:
        # print('skills not in taxonomy')
        # print(C1, C2)
        data = [C1, C2]

        # Vectorise the data
        vec = TfidfVectorizer()

        X = vec.fit_transform(
            data)  # `X` will now be a TF-IDF representation of the data, the first row of `X` corresponds to the first sentence in `data`

        # Calculate the pairwise cosine similarities (depending on the amount of data that you are going to have this could take a while)
        S = cosine_similarity(X)
        similarity = S[0, 1]


        # print('simmmms',similarity)
        l1 = l2 = 1.0  # how much should it be

    else:
        node1 = node1[0]
        node2 = node2[0]
        common = node1.get_common_ancestor(node2)
        # print(common.is_root())
        # print("common is ",common.name)

        """ ------------------N the distance from root node to the least common subsumer-------------------"""
        root = taxonomy.get_tree_root()
        N = taxonomy.get_distance(common, root, topology_only=False)
        # print("N = the distance between the common ancestor", common.name, "AND  ROOT IS ", N)

        """ ----------------N1 the distance from Concept 1 to the least common subsumer--------------------"""
        N1 = taxonomy.get_distance(C1, common, topology_only=False)
        # print("N1 = the distance between",C1,"AND  ROOT IS ",N1)

        """ ----------------N1 the distance from Concept 2 to the least common subsumer--------------------"""
        N2 = taxonomy.get_distance(C2, common, topology_only=False)
        # print("N2 = the distance between",C2, "AND  ROOT IS ", N2)

        """ -------------------------------COMPUTE THE MEASURE FORMULA----------------------------------------"""

        similarity = (2*N)/(N1+N2+(2*N))

        # print("similarity between ", C1,"and",C2, "is", similarity)
        # print("---------------------------------------------------")
        l1 = node1.level_score
        l2 = node2.level_score

    return similarity,l1,l2


