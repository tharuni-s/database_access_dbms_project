import mysql.connector as connector
class DBhelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='Srini@2006',database='DBproject')
        query='create table if not exists student(s_id int primary key,studentName varchar(20),phone int )'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    #insert
    def insert_stu(self,s_id,studentName,phone):
         query="insert into student(s_id,studentName,phone)values({},'{}',{})".format(s_id,studentName,phone)
         cur=self.con.cursor()
         cur.execute(query)
         self.con.commit()
         print("user saved to db")
#     #fetch all
    def fetch_all(self):
        query="select * from student"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("s_id:", row[0])
            print("studentName:",row[1])
            print("Phone no : ",row[2])
            print()
            print()
    def delete_stu(self,s_id):
        query="delete from user where s.id={}".format(s_id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted")

    #update

    def update_stu(self,s_id,studentName,phone):
        query="update student set studentName='{}',phone={} where s_id={}".format(studentName,phone,s_id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
helper=DBhelper()
#helper.insert_stu(1,'abi',

