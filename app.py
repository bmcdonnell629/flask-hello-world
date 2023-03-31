from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://lab_10_db_user:6wuRbvayRIPNjpQmYCwgAsqpnsyKh9Mh@dpg-cgjj66pmbg59uqh99sfg-a/lab_10_db")
    
    conn.close()
    
    return "Database Connection Succesful"
