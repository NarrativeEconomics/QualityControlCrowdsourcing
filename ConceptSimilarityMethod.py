__author__ = 'Arwa Shaker'
""" THIS METHOD IS ADOPTED FROM THIS WORK 
(VERB SEMANTICS AND LEXICAL SELECTION)
WHICH IS AN IMPLEMENTATION TO THE Wu AND PALMER MEASURE """


import distance
import  ete3
from ete3 import TreeNode,Tree
import math


def concept_similarity_measure(C1, C2,taxonomy):
    #taxonomy.set_outgroup(taxonomy & "root")
    #print(taxonomy)

    print("C1",C1,"\n","C2",C2)


    N1 = 0 # the distance from Concept 1 to the least common subsumer
    N2 = 0 # the distance from Concept 2 to the least common subsumer
    N = 0  # the distance from  the least common subsumer to the root
    """ -----------------L   he shortest path between the tow concepts------------------------------"""

    node1 = taxonomy.search_nodes(name=C1)[0]
    node2 = taxonomy.search_nodes(name=C2)[0]
    common = node1.get_common_ancestor(node2)
    print(common.is_root())
    print("common is ",common.name)

    """ ------------------N the distance from root node to the least common subsumer-------------------"""
    root = taxonomy.get_tree_root()
    N = taxonomy.get_distance(common, root, topology_only=False)
   # print("N = the distance between the common ancestor", common.name, "AND  ROOT IS ", N)

    """ ----------------N1 the distance from Concept 1 to the least common subsumer--------------------"""
    N1 = taxonomy.get_distance(C1, common, topology_only=False)
    #print("N1 = the distance between",C1,"AND  ROOT IS ",N1)

    """ ----------------N1 the distance from Concept 2 to the least common subsumer--------------------"""
    N2 = taxonomy.get_distance(C2, common, topology_only=False)
    #print("N2 = the distance between",C2, "AND  ROOT IS ", N2)

    """ -------------------------------COMPUTE THE MEASURE FORMULA----------------------------------------"""

    similarity = (2*N)/(N1+N2+(2*N))

    print("similarity between ", C1,"and",C2, "is", similarity)
    #print("---------------------------------------------------")

    return similarity