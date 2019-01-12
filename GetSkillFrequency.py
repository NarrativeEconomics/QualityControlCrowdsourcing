""" This method takes a list of skill sets and return a file of each skill and the frequency
which is the number of lists that contained that skill --- in other words the number of workers
or tasks"""



def get_skills_frequency(skills):

        # compute the frequencies of skills
        def map_skills(skills):
            hash_map = {}

            for skills_row in skills:
                if skills_row is not None:
                    for skill in skills_row:
                        if skill is not '':
                            # skill Exist?

                            if skill in hash_map:

                                hash_map[skill] = hash_map[skill] + 1
                            else:
                                hash_map[skill] = 1


            return hash_map


        # Create a Hash Map (Dictionary)
        map = map_skills(skills)

        # write it to a text file

        with open('jobs_skills_frequency.csv', 'w') as file:
            for skill in map:
                print(skill,',', map[skill], file=file)

        # Show skill Information
      #  for skill in map:
     #      print('skill: [' + skill + '] Frequency: ' , map[skill])

        percentage =  {}
        # compute the total number of skills
        total  = 0
        for skill in map:
            total  = total  + map[skill]


        # compute the percentage of each skill
        for skill in map:
            percentage[skill] = (map[skill]/total) * 100

        # Show skill Information
       # for skill in map:
         #   print('skill: [' + skill + '] Percentage: ' ,percentage[skill])







