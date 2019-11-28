import pymysql

class myDB(object):
    def __init__(self, host, port, user, passwd, dbname, charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.charset = charset

    def connet(self):
        self.db = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.dbname,
            charset=self.charset
        )
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def select_one(self, sql):
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except pymysql.Error as e:
            print(e)
        return res

    def select_all(self, sql):
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except pymysql.Error as e:
            print(e)
        return res

    def insert(self, sql):
        return self.__edit(sql)
    
    def update(self, sql):
        return self.__edit(sql)
    
    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except pymysql.Error as e:
            print(e)
        return count

conn = myDB("2.2.2.200", 3306, "root", "123456", "mydb", "utf8")
conn.insert("insert into mydb.aaa (id ,name) values (1, 'tom')")
conn.insert("insert into mydb.aaa (id ,name) values (2, 'jerry')")
data = conn.select_all("select * from mydb.aaa")
for i in data:
    print(i)