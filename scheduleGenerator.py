import sqlite3

def generateSchedule(coursesTaken):
    # establish connection to database
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()

    # create empty list to store schedules that don't contain the courses taken
    deficiencyList = []
    prereqList = []

    # build the SQL query dynamically based on the number of courses taken
    query = "SELECT * FROM schedules WHERE "
    for i, course in enumerate(coursesTaken):
        if i == len(coursesTaken) - 1:
            query += f"course1 != '{course[0]}' AND course2 != '{course[0]}' AND course3 != '{course[0]}' AND course4 != '{course[0]}'"
        else:
            query += f"course1 != '{course[0]}' AND course2 != '{course[0]}' AND course3 != '{course[0]}' AND course4 != '{course[0]}' AND "

    # execute the query and add the results to the deficiency list
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        schedule = {
            'course1': result[1],
            'course2': result[2],
            'course3': result[3],
            'course4': result[4]
        }
        
        if schedule not in deficiencyList:
            deficiencyList.append(schedule)
        
    # return the deficiency list
    return deficiencyList