import psycopg2

from flask import Flask
app = Flask(__name__)

#home page hello world route
@app.route('/')
def hello_world():
    return 'Hello, World!'

#route to test db connection
@app.route('/db_test')
def testing():
    #connect to render db and then close connection
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    conn.close()
    
    return "Database Connection Succesful"

#route to create table in db
@app.route('/db_create')
def create():
    #conncet to db and create cursor
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    cur = conn.cursor()
    #execute create table if it doesnt already exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
        ''')
    #commit and close db connection
    conn.commit()
    conn.close()
    
    return "Basketball Table created succesfully"

#route to insert data into db
@app.route('/db_insert')
def insert():
    #open connection and create cursor
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    cur = conn.cursor()
    #declare result string 
    result =""
    #try to execute insert into table of data
    try:
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            Values
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
         ''')
        #if succesful result = succesful
        result = "Basketball table succesfully populated"
    #if unable to insert result = not succuesful
    except:
        result = "Basketball table not populated"
    
    #close and commit changes
    conn.commit()
    conn.close()
    
    return result

#route to query data
@app.route('/db_select')
def select():
    #open db connection and create cursor
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    cur = conn.cursor()
    #create empty html var
    htmlRecord = ""
    #try to execute select query on table
    try:
        cur.execute('''
            SELECT * FROM Basketball;
        ''')

        records = cur.fetchall()
        #iterate over selected data and insert into html record in html table format
        htmlRecord += "<table>"
        for player in records:
            htmlRecord += "<tr>"
            for info in player:
                htmlRecord += "<td>{}</td>".format(info)
            htmlRecord += "<tr>"
        htmlRecord += "</table>"
    #if unable to select html = unsuccesful
    except:
        htmlRecord = "No data to select"
    #close connection
    conn.close()
    
    return htmlRecord
    
#route to drop table
@app.route('/db_drop')
def drop():
    #open connection and create cursor
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    cur = conn.cursor()
    #drop table if exists
    cur.execute('''
        DROP TABLE IF EXISTS Basketball;
    ''')
    #commit and close connection
    conn.commit()
    conn.close()
    
    return "Basketball Table Succesfully Dropped"
    