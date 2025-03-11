from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App is Running"

@app.route('/db')
def test_db():
    try:
        conn = psycopg2.connect("dbname=flaskdb user=admin password=password host=postgres-service")
        return "Database Connected"
    except:
        return "Database Connection Failed"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
