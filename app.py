from flask import Flask, render_template, url_for
app = Flask(__name__)

# Routes used to render a HTML file that can be edited in the templates folder.
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courseplanning')
def courseplanning():
    return render_template("courseplanning.html")

@app.route('/degreeflow')
def degreeflow():
    return render_template("degreeflow.html")



if __name__ == '__main__':
    app.run(debug= True)
