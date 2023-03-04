# CS448-NOCAP
Note: *****install script in progress*****
To begin the project first create a python venv

Then activate it using your path to folder
source /<path>/CS448-NOCAP/bin/activate

To install project download flask

Update---3/4--
To keep a live development environment when building the site use the following commands on terminal
export FLASK_DEBUG=development **switched from DEV to DEBUG as dev is deprecated and tosses errors
export FLASK_APP=app.py
then run 
flask --debug run

Update2.1 3-4 
    Created a base.html: here holds the top nav along with title, scripts, opening and closing tags. So 
    technically all the header and footer. Thus the only things that will need to be editied in the pages 
    will be the body content make sure that any HMTL you put in the pages is in between the block tags example below:
    
    {% block content %}

        //your html here
    
    {% endblock %}



