import sqlite3



def getCourseInfo(courseNum):

    print("courseNum input: " + courseNum)

    connection = sqlite3.connect('courselist.db')
    cursor = connection.cursor()

    result = cursor.execute(f"SELECT description FROM course_list WHERE id = \'CS{courseNum}\'")


   # print(result.fetchone())

    return str(result.fetchone())




# result = cursor.execute("SELECT id FROM course_list WHERE prereq LIKE '%CS272%'")
# print(result.fetchall())



# connection.close()