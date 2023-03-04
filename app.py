import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = ['pdf']

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
    return render_template("courseplanning.html")

# gets student status, major, and audit from the form in courseplanning.html
@app.route('/courseplanning', methods=['GET', 'POST'])
def courseplanning_upload():
    if request.method == 'POST':
        
        # declare these as globals so we can use them wherever we need to
        global student_status 
        global student_major
        
        student_status = request.form.get("status")
        student_major = request.form.get("major")
        if 'audit' in request.form:
            student_audit = request.files['audit']
        
        # once i grab the file, i want to pass it to the scraping function
        # thisIsTheScrapingFunction(student_audit)

        return render_template("courseplanning.html")
    
    elif request.method == 'GET':
        return render_template("courseplanning.html")
    
@app.route('/degreeflow')
def degreeflow():
    return render_template("degreeflow.html")

if __name__ == '__main__':
    app.run(debug= True)
