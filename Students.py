import pymysql


class Database:
    def __init__(self):
        self.Connection = Connection = pymysql.connect(host='localhost', user='root', password='9479854532441919Lb')
        self.Cursor = Connection.cursor()

    def Create_Database(self, name):
        get = "CREATE DATABASE {}".format(name)
        self.Cursor.execute(get)


school = Database()
school.Create_Database('school')
