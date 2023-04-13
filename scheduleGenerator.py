import sqlite3

def generateSchedule(coursesTaken):
    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()


    result = cursor.execute("SELECT * FROM schedules")

    deficiencySet = set([])

    for row in result:
        for course in coursesTaken:
            if row[1] not in course[0]:
                deficiencySet.add(row[1])
            if row[2] not in course[0]:
                deficiencySet.add(row[2])
            if row[3] not in course[0]:
                deficiencySet.add(row[3])
            if row[4] not in course[0]:
                deficiencySet.add(row[4])

    print(coursesTaken)   
    print('\n-----------------\n')
    print(deficiencySet)


    #return (set(result.fetchall()) & set(coursesTaken))

    