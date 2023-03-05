#importing needed modules for PDF scrapper
from PyPDF2 import PdfReader as reader

#creating object
pdfR = reader("/home/hiddenhentai/Documents/Senior/CS448-NOCAP/CS448-NOCAP/audit_2023-03-04_14 45 05.0_Sat_Mar_04_15 26 30_MST_2023.pdf")


#create a reader
page = reader.pages[0]

#lets practice print out number of pages on the pdf
print(page.extract_text())

# create a page object
#pageObj = pdfR.getPage(0)

#extract the text
#print(pageObj.extractText())

#close the file object
#pdfObject.close()
