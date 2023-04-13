from bs4 import BeautifulSoup
import html5lib


# htmlScraper takes in a string of html and returns a string of text
def htmlScraper(html):
    soup = BeautifulSoup(html, 'html5lib')
    
    # find all elements with class 'takenCourse' and store them in a list
    course_elements = soup.find_all('tr', class_='takenCourse')
    
    # create a list of lists to store the course, description, and grade
    global course_list 
    course_list = []
    
    # iterate through the list of course elements and print the course and description
    for course_element in course_elements:
        course = course_element.find('td', class_='course')
        grade = course_element.find('td', class_='grade')
        description = course_element.find('td', class_='description')
        
        # append the course, description, and grade to the course_list
        course_list.append([course.text.strip().replace(' E', '').replace(' ', ''), description.text.strip().split('CONVERTED',1)[0].strip()]) #, grade.text.strip()])
        
    # this is just to verify that the list is being populated correctly
    print(*course_list, sep = '\n')   
    return course_list
        
   
