import sqlite3

def generateSchedule2(coursesTaken,noTaken):
    #print(coursesTaken)
    print("***************")
    for x in noTaken:
        print(x)
    # establish connection to database
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    
    # create empty list to store schedules that don't contain the courses taken this list will be the filtered data from passed lists
    deficiencyList = []
    filtered_list = []
    indices_to_remove = []
    count = 0
    '''Will compare both passed lists and store into another list which will this 3rd list
        is the requirements still not met in the degree audit. The list will take into account
        the students GPA to Avoid giving them a extremely difficult semester. The courses will be stacked in ascending order
        when generating the schedule. And creating a schedule of 15 Credit Hours max or 5 courses.'''
    #begin filtering courses from lists
    for index, sublist in enumerate(noTaken):
        courses = sublist
    
        for  not_taken_course in courses:
            
            if isinstance(courses,list) and len(courses) > 1:
                    last_element = courses[-1]
                    if isinstance(last_element, int) and 1 <= last_element <= 2:
                        print("The courses =", courses)
                        count = courses.pop()
                       
                
            for secondList_course in coursesTaken:
                    if count > 0:
                        
                        if not_taken_course == secondList_course[0]:
                            
                            count = count - 1
                            
                            if count == 0:
                               
                                for i in range(len(sublist)):
                                    sublist[i] = []
                                sublist = [item for item in sublist if item]
                                sublist = [[]] if not sublist else sublist

                            
                        
                    else:
                            #if len(sublist) > 1:
                                
                            if not_taken_course == secondList_course[0]:
                                sublist.remove(not_taken_course)
                    
    print("**********Needed Courses**********")
    
    for y in noTaken: 
        print(y)


    # return the deficiency list
    return filtered_list
def generateSchedule(coursesTaken):
 # establish connection to database
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    
    # create empty list to store schedules that don't contain the courses taken this list will be the filtered data from passed lists
    deficiencyList = []
    prereqList = []
    '''Lets try something different we are getting a list with such elements
        ['ENGL111G', 'RHETORIC/COMPOSITION', 'B-'],
        Lets make a new list that compares with the degree plan if the course is already taken
        then lets not add it to the list, else if the course has a failing grade add to list, else add to list.
        Once the none taken courses are added to the list we can being creating the courses.
    '''
    #Retreive the data from the db
    cursor2.execute("SELECT * FROM course_list")
    rows = cursor2.fetchall()
    
    #In theory all the data from the db which is not going to be large should be stored in the rows element
    # No we append it to the plans list with the format we had wanted to 
    #Making a list of none taken and retaking courses from the degree audit.
    plan = []
    #for row in rows:
     #   plan.append([row[0]])

    #Begining list comparisons, this will check rows list with the coursestaken list if
    # the Course does not exist in the taken then append to plan list also if the course exists check grade
    # if the grade is D then add to plan list as this is a failure and will need to be retaken. 
    for course in rows:
        #print(course)
        if course[0] not in [c[0] for c in coursesTaken]:
            plan.append(course)
        else:
            for c in coursesTaken:
                if c[0] == course[0]:
                    if c[2] == 'D' and not c[1].startswith('IP'):
                        plan.append(course)
                        break
   #print("Did it work?")
    #print(coursesTaken)
    #print(plan)

    # build the SQL query dynamically based on the number of courses taken
    query = "SELECT * FROM schedules WHERE "
    for i, course in enumerate(coursesTaken):
        if i == len(coursesTaken) - 1:
            query += f"course1 != '{course[0]}' AND course2 != '{course[0]}' AND course3 != '{course[0]}' AND course4 != '{course[0]}'"
        else:
            query += f"course1 != '{course[0]}' AND course2 != '{course[0]}' AND course3 != '{course[0]}' AND course4 != '{course[0]}' AND "

    # execute the query and add the results to the deficiency list
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        schedule = {
            'course1': result[1],
            'course2': result[2],
            'course3': result[3],
            'course4': result[4]
        }
        
        if schedule not in deficiencyList:
            deficiencyList.append(schedule)
    
    # return the deficiency list
    return deficiencyList