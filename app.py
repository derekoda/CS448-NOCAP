import os
from werkzeug.utils import secure_filename
from flask import *
import htmlScraper
from jinja2 import * #Template framework for Flask to manipulate html data client side.
import staticFlowChart as flow
import scheduleGenerator as scheduleGen
import sqlite3
#from flask_wtf import *
#sfrom wtforms import *

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.html']
app.config['UPLOAD_PATH'] = 'uploads'
    
# Routes used to render a HTML file that can be edited in the templates folder.
@app.route('/')
def index():
    secret = '<a onclick="setTimeout(function(){location.href=\'https://wallpapercave.com/wp/wp5280203.png\';},1000);"><img src="static/img/tentacles-removebg-preview.png" alt="Example"></a>'

    name = "Manny"#Example jinja2 varaible passed to html via the return statement
    return render_template('index.html', page='index', secret=secret)# Here you have two arguments the template being passed and the variable, 
                                                     # name = <- addresses the name in app while ->  = name in html template. 

@app.route('/index')
def index_redirect():
    secret = '<a href="https://wallpapercave.com/wp/wp5280203.png"><img src="static/img/tentacles-removebg-preview.png" alt="Example"></a>'

    return redirect(url_for('index',page='index',secret=secret))

@app.route('/about')
def about():
    return render_template("about.html",page='about')

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courseplanning')
def courseplanning():
    return render_template('courseplanning.html',page='courseplanning')
    
@app.route('/degreeflow')
def degreeflow():
    return render_template("degreeflow.html",page='degreeflow')

@app.route('/course', methods=['GET'])
def findCourseInfo():

    courseName = request.args.get("id")
    print()
    print("course name: " + courseName)

    return flow.getCourseInfo(courseName)

#Route for course info pulling from DB when client hovers over courses.
@app.route('/get_course_info')
def get_course_info():
    #gets the course id from the parameters in the query
    course_id = request.args.get('course_id')
    #db connection
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()
    #Query command to pull data from db
    cursor.execute('SELECT name, description, prereq FROM course_list WHERE id = ?', (course_id,))
    #get the first result from the query and store it.
    row = cursor.fetchone()
    connection.close()
    #If it exists toss it at the client else barf undefined
    if row:
        name, description, prereq = row
        return jsonify({'name':name,'description': description, 'prereq': prereq})
    else:
        return jsonify({'error': f'Course with id {course_id} not found'})


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
        #scheduleList = scheduleGen.generateSchedule(course_list)

    # call generateSchedule function with list of courses taken
    deficiencySet = course_list#scheduleGen.generateSchedule(course_list)
    
    #print (deficiencySet)
    # render deficiency set in template
    return render_template('schedule.html', deficiencySet=deficiencySet, page='coursemenu')

@app.route('/schedule', methods=['GET','POST'])
def schedule():

    return render_template('schedule.html',page='schedule')

if __name__ == '__main__':
    app.run(debug=True)
