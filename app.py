import psycopg2
import urllib.parse
from flask import Flask
app = Flask(__name__)

unencoded = "postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db"
encoded = urllib.parse.quote_plus(unencoded)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    unencoded = "postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db"
    encoded = urllib.parse.quote_plus(unencoded)
    conn = psycopg2.connect(encoded)
    
    conn.close()
    
    return "Database Connection Succesful"

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
        ''')
    
    conn.commit()
    conn.close()
    
    return "Basketball Table created succesfully"

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
     ''')
    
    conn.commit()
    conn.close()
    
    return "Basketball table succesfully populated"

@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    
    cur = conn.cursor()
    
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    
    records = cur.fetchall()
    
    conn.close()
    
    return records

@app.route('/db_drop')
def drop():
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    
    cur = conn.cursor()
    
    cur.execute('''
        DROP TABLE IF EXISTS Basketball;
    ''')
    
    return "Dropped Basketball Table"
    