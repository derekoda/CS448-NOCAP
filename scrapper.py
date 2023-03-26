#importing needed modules for PDF scrapper
from PyPDF2 import PdfReader as reader
import string
import re
import app

def pdf_from_App(file):
    #creating object
    pdfR = reader(file)

    i = 0
    #create a reader Reads page number 1 from the stack
    page = pdfR.pages[i]

    ##Flag tells app to print text or not##
    flag = False
    new_string= ""

    for page in pdfR.pages: 
        print("***************PAGE: " + str(i))
    #lets practice print out number of pages on the pdf

        #The string will hold each page individually
        ####################This will allow for PDF manipulation and scraping############
        string = page.extract_text()
        onString = "CreditsGradeTitle"
        offString = "TermCourse"
        lines = string.split('\n')
    
        ###For each line if substring exist print next line
        for line in lines: 
            if line[0].isdigit():
                if 'TermCourse' in line:
                    line = line.replace('TermCourse', '')
                    if 'CreditsGradeTitle' in line:
                        line = line.replace('CreditsGradeTitle', '') 
                    #print(line)
                else:
                    #remove the first word in each line 
                    space_index = line.find(' ') 
                    new_string += line[space_index:] + '\n'
                    print(new_string)
    #print(new_string)

                    #REGEX pattern to parse information
                    pattern = r"(.+?)(?=\s\d\.\d)(?:\s\d\.\d)([A-Za-z\+\-]{2})"
                    #Find if it matches store in matches
                    matches = re.findall(pattern, new_string)

                    #print Output to terminal
                    #Note implent return to app perhaps store in a var that can be returned to App.
                    for match in matches:
                        course, grade = match
                        #formatting for app and terminal display.
                        print(f"Course: {course.replace(' ','')} Grade: {grade.strip()}")  
        i += 1

    # create a page object
    #pageObj = pdfR.getPage(0)

    #extract the text
    #print(pageObj.extractText())

    #close the file object
    #pdfObject.close()
