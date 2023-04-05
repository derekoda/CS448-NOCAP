from bs4 import BeautifulSoup
import html5lib


# htmlScraper takes in a string of html and returns a string of text
def htmlScraper(html):
    soup = BeautifulSoup(html, 'html5lib')
    
    # find all elements with class 'takenCourse' and store them in a list
    course_elements = soup.find_all('tr', class_='takenCourse')
    
    # iterate through the list of course elements and print the course and description
    for course_element in course_elements:
        course = course_element.find('td', class_='course')
        grade = course_element.find('td', class_='grade')
        description = course_element.find('td', class_='description')
        print(course.text.strip() + ' ' + description.text.strip().split('CONVERTED',1)[0] + ' ' + grade.text.strip())
        
        
   
