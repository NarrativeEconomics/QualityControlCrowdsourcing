from ete3 import Tree
taxonomy =  Tree("skills_taxonomy_tree_1.nw")

#find the depth of the tree
node,  depth =  taxonomy.get_farthest_leaf()
print(depth)

root = taxonomy.get_tree_root()
depth = int(depth)
for i in range (0,depth+1):
    for node in taxonomy.traverse("postorder"):
        j= i
        j = float(j)
        if node.get_distance(node,root)== j:
            l = j/depth
            node.add_feature('level_score', l)