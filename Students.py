import pymysql


class Database:
    def __init__(self):
        self.Connection = Connection = pymysql.connect(host='localhost', user='root', password='9479854532441919Lb')
        self.Cursor = Connection.cursor()

    def Create_Database(self, name):
        get = "CREATE DATABASE {}".format(name)
        self.Cursor.execute(get)


class Tables:
    def __init__(self):
        self.Connection = Connection = pymysql.connect(host='localhost', user='root', password='9479854532441919Lb', db='school')
        self.Cursor = Connection.cursor()

    def Create_Table_students(self, name):
        get = "CREATE TABLE {}(id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(100));".format(name)
        self.Cursor.execute(get)

    def Create_Table_papers(self, name):
        get = "CREATE TABLE {}(title VARCHAR(100), grade INT, student_id INT, FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE);".format(name)
        self.Cursor.execute(get)

    def Insert_Many_Into_students(self, content):
        datas = []
        insert = "INSERT INTO students(first_name) VALUES(%s);"
        for element in content:
            datas.append(element)
        self.Cursor.executemany(insert, datas)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Many_Into_papers(self, content):
        datas = []
        insert = "INSERT INTO papers(student_id, title, grade) VALUES(%s, %s, %s);"
        for element in content:
            datas.append(element)
        self.Cursor.executemany(insert, datas)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def students_table(self):
        get = "SELECT first_name, IFNULL(title, 'MISSING'), IFNULL(grade, 0) FROM students LEFT JOIN papers ON students.id = papers.student_id;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def Grade_Average(self):
        get = "SELECT first_name, IFNULL(AVG(grade), 0) AS average FROM students LEFT JOIN papers ON students.id = papers.student_id GROUP BY students.id ORDER BY average DESC;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def Status(self):
        get = " SELECT first_name, Ifnull(Avg(grade), 0) AS average, CASE WHEN Avg(grade) IS NULL THEN 'FAILING' WHEN Avg(grade) >= 75 THEN 'PASSING' ELSE 'FAILING' end AS passing_status FROM students LEFT JOIN papers ON students.id = papers.student_id GROUP  BY students.id ORDER  BY average DESC;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)


school = Tables()
school.Grade_Average()