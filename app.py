import os
from werkzeug.utils import secure_filename
from flask import *
import scrapper
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

# gets student status, major, and audit from the form in courseplanning.html
@app.route('/courseplanning', methods=['GET', 'POST'])
def courseplanning_upload():
    if request.method == 'POST':
        
        # declare these as globals so we can use them wherever we need to
        global student_status 
        global student_major
        global student_audit
        
        student_status = request.form.get("status")
        student_major = request.form.get("major")
        
        student_audit = request.files['audit']
        filename = secure_filename(student_audit.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                os.abort(400)
            student_audit.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            return "Your file has been uploaded successfully." + student_status + student_major
        return redirect(url_for('courseplanning'))
    
@app.route('/degreeflow')
def degreeflow():
    return render_template("degreeflow.html")

#This route is used to handle the PDF upload from the client side
#The methods handled by the route are the GET and POST
@app.route('/upload-pdf', methods=['GET','POST'])
def upload_pdf():
    
    # Process the PDF file here
    if request.method == 'POST':
        #stores the PDF in a temp object for processing
        pdf_file = request.files['pdf_file']
        #if the file exists then lets process
        if pdf_file:
            #sends to the scrapper and stores it in a variable
            parsed = scrapper.pdf_from_App(pdf_file)
            
        return 'PDF file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
