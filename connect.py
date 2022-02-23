import sqlite3

class movies:

    def __init__(self):
        self.con=sqlite3.connect("mulesoft.db")
        print('Database Created')

        self.con.execute('create table if not exists movies(id int not null,moviesname text,actor text,actross text,director text,yearofrelease int)')
        print('table created')

    def insertdata(self,id,moviesname,actor,actross,director,yearofrelease):

        self.con.execute("insert into Movies values(?,?,?,?,?,?)",(id,moviesname,actor,actross,director,yearofrelease))


        print('Data inserted')
        self.con.commit()



    #result=self.con.execute("select * from Movies")
    # for row in data:
    #     print("id id:{},moviesname:{},ActorName:{},Actressname:{},Director:{},yearofrelase:{}")

obj=movies()
obj.insertdata(1,"bahubali","prabhas","Anushka Shetty","S. S. Rajamouli","2015")