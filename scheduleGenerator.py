import sqlite3
from time import strftime


def generateSchedule2(coursesTaken,noTaken):
    
    #for x in noTaken:
    #    print(x)
    # establish connection to database
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    
    # create empty list to store schedules that don't contain the courses taken this list will be the filtered data from passed lists
    deficiencyList = []
    filtered_list = []
    
    '''Will compare both passed lists and store into another list which will this 3rd list
        is the requirements still not met in the degree audit. The list will take into account
        the students GPA to Avoid giving them a extremely difficult semester. The courses will be stacked in ascending order
        when generating the schedule. And creating a schedule of 15 Credit Hours max or 5 courses.'''
    #begin filtering courses from lists
    for index, sublist in enumerate(noTaken):
        # stores the first iteratin of the enumerated noTaken list into courses
        
        #for each list of courses check each course individually
        for  element_in_sublist in sublist:
            #means this is just a one course
            if len(sublist) == 1:
                for taken_element in coursesTaken:
                    
                    if element_in_sublist == taken_element[0]:
                       #The course has already been processed by another requirement
                       if not sublist:
                        continue
                       #This is the first time we see the course process it
                       elif len(sublist) >= 1:
                        sublist.remove(taken_element[0])
                        

            if len(sublist) > 1:
                #This means this list has a tailing number and needs one or more requirements
                if sublist[-1] == 1 or sublist[-1] == 2:
                    
                    counter = sublist[-1]#store the last element as a counter
                    
                    sublist.pop()
                    for taken_element in coursesTaken:
                        if element_in_sublist == taken_element[0]:
                            counter -= 1
                        elif element_in_sublist != taken_element[0]:
                            continue
                        if counter == 0:# all requirements met erase the list
                            sublist.clear()
                elif sublist[-1] != 1 and sublist[-1] != 2:
                    for taken_element in coursesTaken:
                        
                        if element_in_sublist == taken_element[0]:
                            sublist.clear()# clean the list course matched
                            break
                        else:
                            continue
                else:
                    continue
            
    #print("**********Needed Courses**********")
    #to see the requirements list
    #for y in noTaken: 
    #    print(y)


    # return the deficiency list
    return noTaken
def processSchedule(filterd_List, takenCourses ,gpa ):
    for course in filterd_List:
        print(course) 
    for course in takenCourses:
        print(course)
    # establish connection to database
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()
    cursor2 = connection.cursor()

    #Get the current semester the student is attending
    current_month = strftime('%B')
    season= get_Season(current_month)

    #Create final schedule that is to be returned
    final_list= []

    
    #lets also check the semester
    if "SP" in season:
        #This will be for the Summer Semeters
        final_list.append("Summer")
    elif "SM" in season:
        #This will be for the Summer Semeters
        final_list.append("Fall")
    else: 
        #This will be for the Summer Semeters
        final_list.append("Spring") 
    #Evaluate GPA
    if float(gpa) >= 3.5:
        #We will pick 3 CS classes max for the student
        count = 3
        for course in filterd_List:
            if 'CS' in course:
                ...
    elif float(gpa) >= 3.0 and float(gpa) < 3.5 :
    #We will pick 2 CS classes max for the student
        count = 2
        pre = False 
        offered = False
        for sublist in filterd_List:
            for element in sublist:
                if element and element.startswith('CS'):
                    
                    cursor.execute("SELECT id, prereq, sem_offered FROM course_list WHERE id =?",(element,))
                    result = cursor.fetchone()
                    print(result)
                    if result:
                        req_number = 0
                        for pre_req in result[1].split(', '):
                            print(pre_req)
                            
                            for taken in takenCourses:
                                count_taken = len(result[1].split(', '))
                                print(count_taken)
                                print(pre_req, taken[0])
                                
                                if pre_req.strip() == taken[0].strip():
                                    print("taken True")
                                    req_number += 1
                                    print(req_number)
                                elif req_number == count_taken:
                                    pre = True
                                else:
                                    continue
                            for seasonIn_list in result[2].split(', '):
                                
                                if seasonIn_list.startswith(season):
                                    print("season True")
                                    offered = True
                        if pre and offered:
                            print("appended =", result)
                            final_list.append(result[0])

                    print(result)
                    print(final_list)
                else:
                    continue
    elif float(gpa) < 3:
    #We will pick 1 CS classes max for the student
        count =1
        ...
    print(final_list)    
    return final_list
def get_Season(month):
    seasons = {
    'FA': ['August','September', 'October', 'November', 'December'],
    'SP': ['January', 'February', 'March', 'April', 'May'],
    'SM': ['April', 'June', 'July']
    }
    for season in seasons:
        if month in seasons[season]:
            return season
    return 'Invalid input month'
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