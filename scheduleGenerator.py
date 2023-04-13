import sqlite3

def generateSchedule(coursesTaken):
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()


    result = cursor.execute("SELECT * FROM schedules")
    print(set(result.fetchall()) & set(coursesTaken))
    return (set(result.fetchall()) & set(coursesTaken))

    