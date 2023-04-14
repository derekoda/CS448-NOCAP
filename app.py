import os
from werkzeug.utils import secure_filename
from flask import *
import htmlScraper
from jinja2 import * #Template framework for Flask to manipulate html data client side.
import staticFlowChart as flow
import scheduleGenerator as scheduleGen
#from flask_wtf import *
#sfrom wtforms import *

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.html']
app.config['UPLOAD_PATH'] = 'uploads'
    
# Routes used to render a HTML file that can be edited in the templates folder.
@app.route('/')
def index():
    name = "Manny"#Example jinja2 varaible passed to html via the return statement
    return stream_template('index.html', name = name)# Here you have two arguments the template being passed and the variable, 
                                                     # name = <- addresses the name in app while ->  = name in html template. 

@app.route('/index')
def index_redirect():
    name = "Manny"
    return Flask.redirect(url_for('index',name))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courseplanning')
def courseplanning():
    return render_template('courseplanning.html')
    
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
@app.route('/coursemenu', methods=['GET','POST'])
def upload_html():
    
    # Process the HTML file here
    if request.method == 'POST':
        # declare these as globals so we can use them wherever we need to
        global student_status 
        global student_major
        global student_audit
        
        student_status = request.form.get("status")
        student_major = request.form.get("major")
        
        # stores the HTML doc in a temp object for processing
        student_audit = request.files['audit']
        # if the file exists then process it
        if student_audit:
            #sends to the scraper and stores it in a variable
            global course_list
            course_list = htmlScraper.htmlScraper(student_audit)
        scheduleList = scheduleGen.generateSchedule(course_list)

    # call generateSchedule function with list of courses taken
    deficiencySet = scheduleGen.generateSchedule(course_list)
    
    print (deficiencySet)
    # render deficiency set in template
    return render_template('schedule.html', deficiencySet=deficiencySet)

@app.route('/schedule', methods=['GET','POST'])
def schedule():

    return render_template('schedule.html')

if __name__ == '__main__':
    app.run(debug=True)
