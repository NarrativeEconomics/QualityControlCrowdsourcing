import csv
from PyQt5 import QtGui, QtCore
from ete3 import Tree


def create_taxonomy():
    with open('C:/Users/Arwa/Desktop/Skills_Categories-25-Feb.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        record = []

        for row in readCSV:
            record.append(row)

        # extracting the categories

        categories = []
        for i in range(0, len(record)):
            category = record[i][1]
            categories.append(category)


        category_set = set(categories)  # without repeation
        i = 1
        taxonomy = Tree()
        for category in category_set:
            taxonomy.add_child(name=category)

        j=1
        for catNode in taxonomy:
            for i in range(0, len(record)):
                if catNode.name == record[i][1]:
                    catNode.add_child(name=record[i][0])
                    j = j+1

        taxonomy.write(format=2, outfile="skills_taxonomy_tree.nw")
        """    ts.show_leaf_name = True
    ts.mode = "c"
    ts.arc_start = -180  # 0 degrees = 3 o'clock
    ts.arc_span = 180
    taxonomy.show(tree_style=ts)"""
        print(taxonomy.get_ascii(attributes=["name"]))
        taxonomy.show()
    return taxonomy

create_taxonomy()