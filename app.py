from flask import Flask, render_template
from pets import pets
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    par = "<p>This is a simple paragraph with text that will be rendered to a page <br> with out an html file</p>"
    button = '''<button onclick="/">Press Me to go Back</button><script>function myFunction() {
        location.replace('{/templates/index.html}')
        }</script>'''

    combined =  par + button
    return combined

@app.route('/data/<pet_type>')
def datapage(pet_type):

    html = f'<h1>List of {pet_type}</h1>'
    html += "<ul>"
    for pet in pets.get(pet_type,[]):
        html += f"<li>{pet['name']}</li>"
    html += '</ul>'


    return html

if __name__ == '__main__':
    app.run(debug= True)
