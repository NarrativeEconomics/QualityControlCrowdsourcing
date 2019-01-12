__author__ = 'Arwa Shaker'
""" THIS METHOD IS ADOPTED FROM THIS WORK 
(A NEW SIMILARITY MEASURE FOR TAXONOMY BASED ON EDGE COUNTING)"""

import distance
import  ete3
from ete3 import TreeNode,Tree
import math


def concept_similarity_measure_stolen(C1, C2,taxonomy):
    #taxonomy.set_outgroup(taxonomy & "root")
    #print(taxonomy)

    print("C1",C1,"\n","C2",C2)

    L  = 0  # the shortest path between the tow concepts
    D  = 0 # the depth of the whole taxonomy tree
    N1 = 0 # the distance from root node to Concept 1
    N2 = 0 ## the distance from root node to Concept 2

    """ -----------------L   he shortest path between the tow concepts------------------------------"""

    node1 = taxonomy.search_nodes(name=C1)[0]
    node2 = taxonomy.search_nodes(name=C2)[0]
    common = node1.get_common_ancestor(node2)
   # print(common.is_root())
    #print("common is ",common.name)

    if common == node1 or common == node2:
        L = taxonomy.get_distance(node1,node2,topology_only=False)

    else:
     #   print("---------------------------------------------------")
        L1 = taxonomy.get_distance(node1,common,topology_only=False)
     #   print("distance between", node1.name, "and", common.name, "is", L1)

        L2 = taxonomy.get_distance(node2,common,topology_only=False)
    #    print("distance between", node2.name, "and", common.name, "is",L2)

        L = L1 + L2 + 1

    #print("\nL = distance between", node1.name, "and", node2.name, "is", L)

    """ ----------------------------D the depth of the whole taxonomy tree----------------------------"""
    farthest, D = taxonomy.get_farthest_node()
   # print("Farthest node is ", farthest.name,"\n")
   # print("D = Depth of the tree", D)

    """ ------------------------N the distance from root node to common ancestor------------------------"""
    root = taxonomy.get_tree_root()
    N = taxonomy.get_distance(common, root, topology_only=False)
   # print("N = the distance between the common ancestor", common.name, "AND  ROOT IS ", N)

    """ ----------------------------N1 the distance from root node to Concept 1-------------------------"""
    N1 = taxonomy.get_distance(C1, root, topology_only=False)
    #print("N1 = the distance between",C1,"AND  ROOT IS ",N1)

    """ ----------------------------N2 the distance from root node to Concept 2-------------------------"""
    N2 = taxonomy.get_distance(C2, root, topology_only=False)
    #print("N2 = the distance between",C2, "AND  ROOT IS ", N2)

    """ ---------lambda 1 FOR NEIGHBOURHOOD Concepts and 0 for concepts from the same hierarchy-----------"""
    if common.is_root():
        Lambda = 1
    else:
        Lambda = 0
    #print("Lambda = ",Lambda)
    """ -------------------------------COMPUTE THE MEASURE FORMULA----------------------------------------"""
    x = (-Lambda * L) / D
    e = math.exp(x)
    similarity = (2*N*e)/(N1+N2)

    print("similarity between ", C1,"and",C2, "is", similarity)
    #print("---------------------------------------------------")
    return similarity