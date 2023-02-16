from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    par = "<p>This is a simple paragraph with text that will be rendered to a page <br> with out an html file</p>"
    button = '''<button onclick="/">Press Me to go Back</button><script>function myFunction() {
        location.replace("https://www.w3schools.com")
        }</script>'''

    combined = par + button
    return combined


if __name__ == '__main__':
    app.run(debug= True)
