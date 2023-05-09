from bs4 import BeautifulSoup
import html5lib
import re #used for matching any number or text on the html 
import scheduleGenerator as gene

# htmlScraper takes in a string of html and returns a string of text
def htmlScraper(html):
    soup = BeautifulSoup(html, 'html5lib')

    #Regex matches any class with the string matching the html class
    regex = re.compile(r'requirement\s+Status_OK(.*)')#Regex used to capture completed requirements
    regex2 = re.compile(r'requirement\s+Status_NO(.*)')#Regex used to capture the none completed requirements


    # find all elements with class 'takenCourse' and store them in a list
    course_elements = soup.find_all('tr', class_='takenCourse')#To find all courses taken
    course_req_Completed = soup.find_all('div', class_=regex)#To find blocks with completed requirements
    course_req_not_completed = soup.findAll('div', class_=regex2)#To find blocks for incomplete requirements

    # create a list of lists to store the course, description, and grade
    global course_list 
    course_list = []

    #List for storing incomplete requirements
    course_req_list = []
    
    # iterate through the list of course elements and print the course and description
    for course_element in course_elements:
        course = course_element.find('td', class_='course')
        grade = course_element.find('td', class_='grade')
        description = course_element.find('td', class_='description').text
        
        if "IP" in grade.text:
        
            course_list.append([course.text.strip().replace(' E', '').replace(' ', ''), description.strip().split('CONVERTED', 1)[0].strip(), grade.text.strip()])

        elif grade.text >= 'D' and grade.text != 'IP':
            continue
        else:
            if description is not None:  # Check if description is not None
                # Process description if it exists
                if "CONVERTED TO:" in description:
                    temp = []
                    temp = description.split(':')
                    course_new = temp[1].strip()
                    course_list.append([course_new.strip().replace(' E', '').replace(' ', ''), description.replace('\t', "").replace('\n',""), grade.text.strip()])
                else:
                    course_list.append([course.text.strip().replace(' E', '').replace(' ', ''), description.strip().split('CONVERTED', 1)[0].strip(), grade.text.strip()])


    #This piece of code will iterate through the block that have unmet requirements and 
    #    attach them to the course_req_list which will then be passed to the scheduler
    #    to process the potential schedule for the student.
    for not_complete in course_req_not_completed:
        check_for_VWW = not_complete.find('div',class_='reqTitle').text

    #This if statement well check the VWW block if there is a course completed it add it to the list of completed
    #Else it is assumed this block is not complete and has no courses to add.
        if 'Viewing a Wider World Requirement' in check_for_VWW:
            not_VWW_Completed_name = not_complete.find('td',class_='course').text
            not_VWW_Completed_Credits = not_complete.find('td', class_='credit').text
            not_VWW_Completed_Description = not_complete.find('td',class_='description').text

            #If in the description block the course name is change this statement will change the course name
            if "CONVERTED TO:" in not_VWW_Completed_Description:
                temp =[]
                temp = not_VWW_Completed_Description.split(':')
                not_VWW_Completed_name = temp[1]
            #Now store in the non completed requirements array and add a second one for the missing req
            course_req_list.append([not_VWW_Completed_name.replace(' E', '').replace(' ', '')])
            course_req_list.append(["MISSING One VWW Course 3 Credits"])
        else:
            #This is not the VWW Block and follows a different pattern
            #Check for all none taken courses in the block
            courses_not_Taken_In_Block = not_complete.find_all('span', class_='subreqTitle')
            #Now for each of these courses not taken in the block store them in the array
            for m in courses_not_Taken_In_Block:
                m=m.text
                if "Take two of" in m:
                    flag = True
                    #Strips the empty space from the CS courses
                    if "C S" in m:
                        m = m.replace("C S", "CS")
                    #Strips everything else from the texts and only captures the courseID
                    regexPattern= r'\b[A-Z]+ ?\d{3,}[A-Z]?\b'
                    #Remove white space
                    matches = [x.replace(' ', '') for x in re.findall(regexPattern, m)]
                    matches.append(2)
                    
                    course_req_list.append(matches)
                    
                 #If the requirements need two courses to complete
                elif "Take two courses from the following:" in m:
                    take = not_complete.find('td',class_='fromcourselist').text
                    #Split into a list
                    take =[cls.strip() for cls in take.split(',') if cls.strip()]
                    #Remove all white space and remove odd C S format
                    take= [course.replace("C S ", "") for course in take]
                    #Add CS to courses for eval
                    take = ['CS'+ x if x != take else x for x in take]
                    take.append(2)
                   
                    course_req_list.append(take)
                else:
                    #Strips the empty space from the CS courses
                    if "C S" in m:
                        m = m.replace("C S", "CS")
                    #Strips everything else from the texts and only captures the courseID
                    regexPattern= r'\b[A-Z]+ ?\d{3,}[A-Z]?\b'
                    #Remove all white space
                    matches = [x.replace(' ', '') for x in re.findall(regexPattern, m)]

                    
                    course_req_list.append(matches)
                
    #print("Taken Courses")         
    # this is just to verify that the list is being populated correctly
    print(*course_list, sep = '\n')   
    print("***********************")
 
    #Clean the course requirements list
    course_req_list_reduced = [item for item in course_req_list if item]

    final_schedule = gene.generateSchedule2(course_list, course_req_list_reduced)
    return final_schedule
        
   
