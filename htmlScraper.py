from bs4 import BeautifulSoup
import html5lib
import re #used for matching any number or text on the html 

# htmlScraper takes in a string of html and returns a string of text
def htmlScraper(html):
    soup = BeautifulSoup(html, 'html5lib')

    #Regex matches any class with the string matching the html class
    regex = re.compile(r'requirement\s+S(.*)')

    # find all elements with class 'takenCourse' and store them in a list
    course_elements = soup.find_all('tr', class_='takenCourse')
    course_req_ele = soup.find_all('div', class_=regex)
    # create a list of lists to store the course, description, and grade
    global course_list 
    course_list = []
    course_req = []
    # iterate through the list of course elements and print the course and description
    for course_element in course_elements:
        course = course_element.find('td', class_='course')
        grade = course_element.find('td', class_='grade')
        description = course_element.find('td', class_='description')
        
        # append the course, description,    course_elements = soup.find_all('tr', class_='takenCourse')
        course_list.append([course.text.strip().replace(' E', '').replace(' ', ''), description.text.strip().split('CONVERTED',1)[0].strip(), grade.text.strip()])
        
    #Iterate through the degree requirements    
    for element in course_req_ele:
        #Getting the header of the div for course credit hours purposes
        requiredHeader = element.find('div', class_='reqTitle')
        
        print(requiredHeader)
      
        #Any already taken courses that have been passed
        completed_Course = element.find('tr', class_='takenCourse')
        print(completed_Course)
        #Now within the taken course check if the courseID was changed and set it to a variable
        if completed_Course != None: 
            for element2 in completed_Course:
                print("IN Loop 2")
                print(element2)
                completed_Description= element2.find('td', class_='descLine')
                #If completed_Description matches string "CONVERTED TO: swap names"
                if "CONVERTED TO:" in completed_Description:
                    new_course_name = element2.find('td', class_='course')
                    new_course_name = completed_Description
        else:
            continue
        not_take_Course = element.find('span', class_='subreqTitle')
        print(requiredHeader) 
        print(completed_Course)
        print(not_take_Course)
    # this is just to verify that the list is being populated correctly
    #print(*course_list, sep = '\n')   
    #print(course_req_ele, sep ='\n')
    return course_list
        
   
