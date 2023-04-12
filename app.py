import os
from werkzeug.utils import secure_filename
from flask import *
import scrapper
import htmlScraper
import staticFlowChart as flow
#from flask_wtf import *
#sfrom wtforms import *

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'uploads'
    
# Routes used to render a HTML file that can be edited in the templates folder.
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def index_redirect():
    return Flask.redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courseplanning')
def courseplanning():
    return render_template(
        'courseplanning.html')
    
@app.route('/degreeflow')
def degreeflow():
    return render_template("degreeflow.html")

@app.route('/course', methods=['GET'])
def findCourseInfo():

    courseName = request.args.get("id")
    print()
    print("course name: " + courseName)

    return flow.getCourseInfo(courseName)


#This route is used to handle the PDF upload from the client side
#The methods handled by the route are the GET and POST
@app.route('/upload-pdf', methods=['GET','POST'])
def upload_pdf():
    
    # Process the PDF file here
    if request.method == 'POST':
        # declare these as globals so we can use them wherever we need to
        global student_status 
        global student_major
        global student_audit
        
        student_status = request.form.get("status")
        student_major = request.form.get("major")
        
        #stores the PDF in a temp object for processing
        student_audit = request.files['audit']
        #if the file exists then lets process
        if student_audit:
            #sends to the scrapper and stores it in a variable
            #parsed = scrapper.pdf_from_App(student_audit)
            parsed = htmlScraper.htmlScraper(student_audit)
        return 'Student status is: ' + student_status + ' and major is: ' + student_major + ' and audit is uploaded'

    return render_template('upload-pdf.html')

if __name__ == '__main__':
    app.run(debug=True)
