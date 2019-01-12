import csv


from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def create_complete_skill_cat_freq_file():
    record_1 = []  # contains skills and categories
    record_2 = []  # contains  skills and frequencies


    # --- reading skills categories into record 1 // column 0 = skills , column 1 = category
    with open('C:/Users/Arwa/Desktop/Skills_Categories-8-April-csv.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            record_1.append(row)
    # --- reading skills frequencies into record 2 // column 0 = skills , column 1 = frequency
    with open('jobs_skills_frequency.csv') as freq_file:
        freq_file = csv.reader(freq_file, delimiter=',')
        for row in freq_file:
            record_2.append(row)

        print(type(record_1[0][1]))
        print(type(record_2[0][1]))


    # --- writing skills, categories and corresponding frequencies into record 3
    with open('complete_skills_categories_frequencies.csv', 'w') as file:

        for i in range(0, len(record_1)):
            print("outer round # //////////////////",i,record_1[i][0])
            for j in range(0,len(record_2)):
                print("inner round # --------",j,record_1[j][0])
                if similar(record_1[i][0], record_2[j][0])>=0.95:
                #if record_1[i][0]== record_2[j][0]:
                    print(record_1[i][1], ',', record_1[j][0],',',record_2[j][1], file=file)
                    break
            print(record_1[i][1], ',', record_1[i][0], ',', 0, file=file)


create_complete_skill_cat_freq_file()