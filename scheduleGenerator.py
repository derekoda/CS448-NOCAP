import sqlite3

def generateSchedule(coursesTaken):
    # establish connection to database
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()

    # create empty set to store courses that are not in the database
    deficiencySet = []

    # iterate through courses taken, find schedules that don't contain those courses
    for course in coursesTaken:
        cursor.execute(f"SELECT * FROM schedules WHERE course1 = \'{course[0]}\' OR course2 = \'{course[0]}\' OR course3 = \'{course[0]}\' OR course4 = \'{course[0]}\'")
        if cursor.fetchone() is not None:
            print(cursor.fetchall())
            deficiencySet.append(cursor.fetchone())
    
    print(deficiencySet)
    # return the set of schedules that don't contain the courses taken
    return str(deficiencySet)

    