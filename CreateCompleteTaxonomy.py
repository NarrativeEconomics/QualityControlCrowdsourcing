__author__ = 'Arwa Shaker'

""" THIS METHOD TAKES A CSV FILE (complete_skills_categories_frequencies.csv)
                        AND CREATE A TAXONOMY """

"""Using ETE Environment Tree Exploration"""

import csv

from ete3 import Tree
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def create_complete_taxonomy():
    record = []
    # --- reading the complete file into record
    with open('complete_skills_categories_frequencies.csv') as file:
        file = csv.reader(file, delimiter=',')
        for row in file:
            record.append(row)


    # extracting the categories
        categories = []
        for i in range(0, len(record)):
            category = record[i][0]
            categories.append(category)
        # without repetition
        category_set = set(categories)

        # Creating the Taxonomy Tree --------------------------------------------
        # ---------Level Zero ---Root
        taxonomy = Tree()
        # ---------Level One --- Categories
        for category in category_set:
            taxonomy.add_child(name=category)


        # ---------Level Two --- Skills
        j=1
        for catNode in taxonomy:
            for i in range(0, len(record)):
                if similar(catNode.name, record[i][0]) >= 0.9:
                    catNode.add_child(name=record[i][1])
                    j = j+1
        # ---------Level Three --- Skills


    # add a level score to each skill

    taxonomy.write(format=2, outfile="skills_taxonomy_tree_1.nw")

    print(taxonomy.get_ascii(attributes=["name"]))
    taxonomy.show()
    return taxonomy

create_complete_taxonomy()