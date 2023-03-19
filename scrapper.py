#importing needed modules for PDF scrapper
from PyPDF2 import PdfReader as reader
import string

#creating object
pdfR = reader("/home/hiddenhentai/Documents/Senior/CS448-NOCAP/CS448-NOCAP/audit_2023-03-04_14 45 05.0_Sat_Mar_04_15 26 30_MST_2023.pdf")

i =0
#create a reader Reads page number 1 from the stack
page = pdfR.pages[i]

##Flag tells app to print text or not##
flag = False

for page in pdfR.pages: 

#lets practice print out number of pages on the pdf

    #The string will hold each page individually
    ####################This will allow for PDF manipulation and scraping############
    string = page.extract_text()
    onString = "CreditsGradeTitle"
    offString = "TermCourse"
    ###For each line if substring exist print next line
    for line in string: 
        if string[0].isdigit():
            flag = True
            print("hello")

        if offString in line:
            flag = False
        
        if flag == True:
            print(string)

        else:
            continue

    i +=1 
# create a page object
#pageObj = pdfR.getPage(0)

#extract the text
#print(pageObj.extractText())

#close the file object
#pdfObject.close()
