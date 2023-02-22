from flask import Flask, render_template, url_for
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

    for i, pet in enumerate(pets.get(pet_type,[])):
        html += f'''<li><a href="{url_for('pet', pet_type=pet_type, pet_id=i)}"{pet['name']}</a></li>'''
        i += 1
    html += '</ul>'
    return html

@app.route('/data/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet_list = pets.get(pet_type)
    pet = pet_list[pet_id]
    first = " Is the pet number "
    end = " in the list."
    return f'''<h1>{pet['name']} {first} {pet_id} {end}</h1>
        <img src="{pet['url']}"><p>{pet['description']}</p><ul><li>{pet['breed']}</li><li>{pet['age']}</li></ul>'''



if __name__ == '__main__':
    app.run(debug= True)
