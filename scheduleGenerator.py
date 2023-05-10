import sqlite3
from time import strftime
from itertools import cycle

def generateSchedule2(coursesTaken,noTaken):
    
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    
    # create empty list to store schedules that don't contain the courses taken this list will be the filtered data from passed lists
    
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
                    #match the courses if theres a match reduce the counter meaning at least one requirement has been met
                    for taken_element in coursesTaken:
                        if element_in_sublist == taken_element[0]:
                            counter -= 1
                        elif element_in_sublist != taken_element[0]:
                            continue
                        if counter == 0:# all requirements met erase the list
                            sublist.clear()
                #if the tailing number is not a 1 or 2 then this only requires to take one course.
                elif sublist[-1] != 1 and sublist[-1] != 2:
                    for taken_element in coursesTaken:
                        
                        if element_in_sublist == taken_element[0]:
                            sublist.clear()# clean the list course matched
                            break
                        else:
                            continue
                else:
                    continue
            
    #Return the list of not taken courses
    return noTaken

#This function compares two lists the filtered data returned from generateschedule2 and Taken courses from the html scraper
#as well as the students GPA
def processSchedule(filterd_List, takenCourses ,gpa ):
    #For presentation purposes
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
    seasons_order = ['SP', 'SM', 'FA']
    #Create final schedule that is to be returned
    final_list= []
    optional = []
    index = 1 #one iteration per semester
    #lets also check the semester
    
    while index <=2:  
        if index == 2:
            current_index = seasons_order.index(season)
            next_index = (current_index + 1) % len(seasons_order)  # Wrap around to the beginning if reached the end
            season = seasons_order[next_index] 

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
            semester_credits = 0
            pre = False 
            offered = False
            for sublist in filterd_List:
                for element in sublist:
                    if element and element.startswith('CS'):
                        
                        cursor.execute("SELECT id, prereq, sem_offered, credits FROM course_list WHERE id =?",(element,))
                        result = cursor.fetchone()
                        
                        if result:
                            req_number = 0
                            for pre_req in result[1].split(', '):
                                
                                
                                for taken in takenCourses:
                                    count_taken = len(result[1].split(', '))
                                    
                                    
                                    if pre_req.strip() == taken[0].strip():
                                        
                                        req_number += 1
                                        
                                    elif req_number == count_taken:
                                        pre = True
                                    else:
                                        continue
                                for seasonIn_list in result[2].split(', '):
                                    
                                    if seasonIn_list.startswith(season):
                                        
                                        offered = True
                            if pre and offered and count != 0:
                            
                                final_list.append(result[0])
                                semester_credits += result[3]
                                count -= 1
                            else:
                                break

                    elif element and not element.startswith('CS'):
                        
                        cursor.execute("SELECT id, prereq, sem_offered, credits FROM course_list WHERE id =?",(element,))
                        result = cursor.fetchone()
                        
                        if result:
                            
                            for pre_req in result[1].split(', '):
                                print("List of elements",sublist)
                                req2_number = 0
                                for taken in takenCourses:
                                    count_taken = len(result[1].split(', '))
                                    
                                    
                                    if pre_req.strip() == taken[0].strip():
                                        
                                        req2_number += 1
                                        
                                    elif req2_number == 1:
                                        pre = True
                                        
                                    else:
                                        break
                                for seasonIn_list in result[2].split(', '):
                                    
                                    if seasonIn_list.startswith(season):
                                        
                                        offered = True
                                    
                            if pre and offered:
                                
                                
                                if semester_credits >= 15:
                                    break
                                else:
                                    final_list.append(result[0])
                                    semester_credits += result[3]
                                    optional.append(sublist.copy())
                                    sublist.clear()
                                    optional = [list(set(sublist)) for sublist in optional]

                                    #Set of elements in the Season list for lookup
                                    season_set = set(final_list)

                                    # Iterate over each sublist in optional
                                    for sublist in optional:
                                        # Filter out elements from sublist that are already in summer
                                        sublist[:] = [course for course in sublist if course not in season_set]
                                    
                            #No element in results
                            else:
                                print("no element")
                                break
                    #Credits met break out of loop        
                    elif semester_credits >= 15:
                        break

                        
                #Credits met break out of loop   
                if semester_credits >= 15:
                    break
                
        elif float(gpa) >= 3.0 and float(gpa) < 3.5 :
        #We will pick 2 CS classes max for the student
            count = 2
            semester_credits = 0
            pre = False 
            offered = False
            for sublist in filterd_List:
                for element in sublist:
                    
                    if element and element.startswith('CS'):
                        
                        cursor.execute("SELECT id, prereq, sem_offered, credits FROM course_list WHERE id =?",(element,))
                        result = cursor.fetchone()
                        
                        if result:
                            req_number = 0
                            for pre_req in result[1].split(', '):
                                
                                
                                for taken in takenCourses:
                                    count_taken = len(result[1].split(', '))
                                    
                                    if pre_req.strip() == taken[0].strip():
                                        
                                        req_number += 1
                                        
                                    elif req_number == count_taken:
                                        pre = True
                                    else:
                                        continue
                                for seasonIn_list in result[2].split(', '):
                                    #Override to test other semeters my Audit
                                    #season = 'FA'
                                    if seasonIn_list.startswith(season):
                                        
                                        offered = True
                            if pre and offered:
                                
                                final_list.append(result[0])
                                semester_credits += result[3]
        
                    #Add courses that are not in the CS requirements    
                    elif element and not element.startswith('CS'):
                        
                        cursor.execute("SELECT id, prereq, sem_offered, credits FROM course_list WHERE id =?",(element,))
                        result = cursor.fetchone()
                        
                        if result:
                            
                            for pre_req in result[1].split(', '):
                                print("List of elements",sublist)
                                req2_number = 0
                                for taken in takenCourses:
                                    count_taken = len(result[1].split(', '))
                                    
                                    
                                    if pre_req.strip() == taken[0].strip():
                                        
                                        req2_number += 1
                                        
                                    elif req2_number == 1:
                                        pre = True
                                        
                                    else:
                                        break
                                for seasonIn_list in result[2].split(', '):
                                    
                                    if seasonIn_list.startswith(season):
                                        
                                        offered = True
                                    
                            if pre and offered:
                                
                                
                                if semester_credits >= 15:
                                    break
                                else:
                                    final_list.append(result[0])
                                    semester_credits += result[3]
                                    optional.append(sublist.copy())
                                    sublist.clear()
                                    optional = [list(set(sublist)) for sublist in optional]

                                    #Set of elements in the Season list for lookup
                                    season_set = set(final_list)

                                    # Iterate over each sublist in optional
                                    for sublist in optional:
                                        # Filter out elements from sublist that are already in summer
                                        sublist[:] = [course for course in sublist if course not in season_set]
                                    
                            #No element in results
                            else:
                                print("no element")
                                break
                    #Credits met break out of loop        
                    elif semester_credits >= 15:
                        break

                        
                #Credits met break out of loop   
                if semester_credits >= 15:
                    break
                        
                
        elif float(gpa) < 3:
        #We will pick 1 CS class max for the student
            count =1
            #keeps count of the credits per semeter to avoid going over 15
            semester_credits = 0
            pre = False #append flag 1/2
            offered = False #append flag 2/2
            #iterate through the filtered list
            for sublist in filterd_List:
                
                for element in sublist:
                    #Is the element is a CS course begin eval make sure count is in the allowed range otherwise
                    #student can no longer take CS courses this semester.
                    if element and element.startswith('CS') and count == 1 :
                        #pull course that matched the sublist element from the db
                        cursor.execute("SELECT id, prereq, sem_offered, credits FROM course_list WHERE id =?",(element,))
                        result = cursor.fetchone()
                        #If not None then can be eval
                        if result:
                            #Stores the number of requirements met for CS classes
                            req_number = 0
                            #Splits the course requirements in the db for iteration 
                            for pre_req in result[1].split(', '):
                                
                                
                                for taken in takenCourses:
                                    #per courses in result at index 1 split and take length for eval exp(CS478, CS484) would be (CS478) (CS484)
                                    count_taken = len(result[1].split(', '))

                                    #If there is a match add to req_number this means student met a course requirement
                                    if pre_req.strip() == taken[0].strip():
                                        #increment number if its a match 
                                        req_number += 1
                                    #If the number of requirements met equals req_number it means student met the course requirements 
                                    #Course can be added to schedule    
                                    elif req_number == count_taken:
                                        pre = True# set flag 1 of 2 to true for adding to schedule
                                    else:
                                        continue
                                #Here we check the season the course is available to take if it is available flip last flag
                                for seasonIn_list in result[2].split(', '):
                                    
                                    if seasonIn_list.startswith(season):
                                        
                                        offered = True
                            #If both flags are True append course to Schedule
                            if pre and offered:
                                
                                final_list.append(result[0])
                                #Reduce the CS courses allowed count
                                count -=1 
                                #increment credits
                                semester_credits += result[3]

                            #Student GPA restrictions met break out of CS loop
                            if count == 0 or semester_credits == 15:
                                break
                        
                    #Add courses that are not in the CS requirements    
                    elif element and not element.startswith('CS'):
                        #pull element from db
                        cursor.execute("SELECT id, prereq, sem_offered, credits FROM course_list WHERE id =?",(element,))
                        result = cursor.fetchone()
                        
                        if result:
                            #Splits the course requirements in the db for iteration 
                            for pre_req in result[1].split(', '):
                                #number flag for requirements
                                req2_number = 0

                                for taken in takenCourses:
                                    count_taken = len(result[1].split(', '))
                                    
                                    #If a requirement is met add one
                                    if pre_req.strip() == taken[0].strip():
                                        
                                        req2_number += 1
                                    #If number is 1 then flip the flag
                                    elif req2_number == 1:
                                        pre = True
                                        
                                    else:
                                        break
                                #Check the season for availablity
                                for seasonIn_list in result[2].split(', '):
                                    #if a match flip the last flag
                                    if seasonIn_list.startswith(season):
                                        
                                        offered = True
                            #If both flags true Append
                            if pre and offered:
                                
                                
                                if semester_credits >= 15:
                                    break
                                #This section appends the sublist from the required courses to an optional list
                                #which the student can take instead of the pre determined courses. Then to avoid 
                                #repeated courses the sublist is copied and cleared.
                                else:
                                    final_list.append(result[0])
                                    semester_credits += result[3]
                                    optional.append(sublist.copy())
                                    sublist.clear()
                                    optional = [list(set(sublist)) for sublist in optional]

                                    #Set of elements in the Season list for lookup
                                    season_set = set(final_list)

                                    # Iterate over each sublist in optional
                                    for sublist in optional:
                                        # Filter out elements from sublist that are already in summer
                                        sublist[:] = [course for course in sublist if course not in season_set]
                                    
                            #No element in results
                            else:
                                print("no element")
                                break
                    #Credits met break out of loop        
                    elif semester_credits >= 15:
                        break

                        
                #Credits met break out of loop   
                if semester_credits >= 15:
                    break
                
        #This will add courses when there are no more CS or difficult courses specifically VWW
        else:
            if semester_credits < 15:
                final_list.append('VWW Course 3 Credits')
                semester_credits += 3
    
        print("Final List")
        print(final_list)
        final_list.append("optional")
        print("Optional Courses")
        print(optional)    
        final_list.append(optional)
        print(final_list)
        return final_list
    index += 1#Change the semester
#Seasons function for selecting the semester
def get_Season(month):
    seasons = {
    'SP': ['January', 'February', 'March', 'April', 'May'],
    'SM': ['April', 'June', 'July'],
    'FA': ['August','September', 'October', 'November', 'December']
    }
    for season in seasons:
        if month in seasons[season]:
            return season
    return 'Invalid input month'






###########################FUNCTION NOT USED PROTOTYPE############################################################
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