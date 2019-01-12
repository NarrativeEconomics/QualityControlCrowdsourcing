
from ete3 import Tree

taxonomy =  Tree()
def create_small_taxonomy():
    node1 = taxonomy.add_child()
    node1.name = "Websites, IT & Software development"

    node2 = node1.add_child()
    node2.name = "Database Development"
    node3 = node2.add_child()
    node3.name = "SQL"

    node2 = node1.add_child()
    node2.name = "Website Development"
    node3 = node2.add_child()
    node3.name = "Website Design"
    node4 = node3.add_child()
    node4.name = "HTML"
    node5 = node4.add_child()
    node5.name = "CSS"

    node4 = node3.add_child()
    node4.name = "PHP"
    node5 = node4.add_child()
    node5.name = "WordPress"
    node6 = node5.add_child()
    node6.name = "Plgin"

    node2 = node1.add_child()
    node2.name = "programming languages"

    node3 = node2.add_child()
    node3.name = "Visual Basic"

    node3 = node2.add_child()
    node2.name="c"
    node4 = node3.add_child()
    node4.name ="Objective C"
    node4 = node3.add_child()
    node4.name="C++ Programming"
    node4 = node3.add_child()
    node4.name = "C# Programming"

    node3 = node2.add_child()
    node2.name ="Java"
    node4 = node3.add_child()
    node4.name="Java ME"
    node4 = node3.add_child()
    node4.name="Java Spring"
    node4 = node3.add_child()
    node4.name ="JavaFX"

    node3 = node2.add_child()
    node3.name = "Linux"
    node4 = node3.add_child()
    node4.name = "Android"
    node5 = node4.add_child()
    node5.name = "Samsung"


    node3 = node2.add_child()
    node3.name = "iPhone"
    node4 = node3.add_child()
    node4.name = "Swift"




    node2 = taxonomy.add_child()
    node2.name = "Translation & Languages"
    node3 = node2.add_child()
    node3.name = "English(UK)"
    node3 = node2.add_child()
    node3.name = "English Spelling"
    node4 = node3.add_child()
    node4.name = "Proofreading"
    node3 = node2.add_child()
    node3.name = "English Grammar"



    node2 = taxonomy.add_child()
    node2.name = "Writing & Content"
    node3 = node2.add_child()
    node3.name = "Research Writing"
    node3 = node2.add_child()
    node3.name = "Academic Writing"
    node3 = node2.add_child()
    node3.name = "Academic Writing"
    node3 = node2.add_child()
    node3.name = "Article Writing"
    node4 = node3.add_child()
    node4.name = "Article Rewriting"

    node2 = taxonomy.add_child()
    node2.name = "Engineering & Science"
    node3 = node2.add_child()
    node3.name = "Engineering"

    node4 = node3.add_child()
    node4.name = "Petroleum Engineering"

    node4 = node3.add_child()
    node4.name = "Mechanical Engineering"
    node5 = node4.add_child()
    node5.name = "Aeronautical Engineering"
    node6 = node5.add_child()
    node6.name = "Aerospace Engineering"

    node4 = node3.add_child()
    node4.name = "Civil Engineering"

    print(taxonomy.get_ascii(attributes=["name"]))
    taxonomy.show()

    print("yes")
    print(taxonomy.get_ascii(attributes=["name"]))
    taxonomy.show()
    taxonomy.write(features=[],format=2, outfile="small_skills_taxonomy_tree.nw")


