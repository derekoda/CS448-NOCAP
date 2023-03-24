import sqlite3

connection = sqlite3.connect('courselist.db')
cursor = connection.cursor()


result = cursor.execute("SELECT id FROM course_list")
print(result.fetchall())



connection.close()