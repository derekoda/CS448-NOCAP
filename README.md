# CS448-NOCAP
Update---4/12--4.1.MH
    Added comments for jinja2 use had to remodify index.html and app.py
        example snip of jinja code for html templates for expression {% for items in list %}
        
Update---4/8--3.1.DO
    HTML scraper now adds all courses with proper formatting to a global list that can be accessed by the program. Created course menu page with options to see potential schedules, see list of all courses, and search for a course.
    
Update---3/26--2.2.DO
    Added an HTML scraper that gives only course number, name, and description. Manny solved the document upload issue.
    
Update---3/26--2.1.DO
    Added the NOCAP logo to the navbar and fixed database issue. Currently working on sending PDF from form to scraper.
    
Update---3/5-- 1.4.MR
    Added the base degree flowchart. Open to suggestions for overall appearance and styles. Tons of styles were added to css file. Footer blocks bottom of the Junior branch in the chart. This chart is represented by the reccommended path from the CS department. Will add buttons to switch to BA major, along with information on each class later.

Update---3/5-- 1.3.DO
    Implemented the 'About Us' page. Implemented the 'Contact Us' page. Added a footer to base page. Worked on receiving file objects from POST request. Working through how to retrieve them so Manny can scrape them.
    
Update---3/4-- 1.2.MH 
    Created a base.html: here holds the top nav along with title, scripts, opening and closing tags. So 
    technically all the header and footer. Thus the only things that will need to be editied in the pages 
    will be the body content make sure that any HMTL you put in the pages is in between the block tags example below:
    
    {% block content %}

        //your html here
    
    {% endblock %}

Update---3/4-- 1.1MH
To keep a live development environment when building the site use the following commands on terminal
export FLASK_DEBUG=development **switched from DEV to DEBUG as dev is deprecated and tosses errors
export FLASK_APP=app.py
then run 
flask --debug run





