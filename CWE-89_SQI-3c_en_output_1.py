
from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
    conn.commit()
    conn.close()

@app.route('/post', methods=['POST'])
def post():
    username = request.form.get('username')
    message = request.form.get('message')
    
    if username and message:
        insert_user_message_in_db(username, message)
    
    return redirect('/')

@app.route('/')
def main_page():
    return render_template('index.html')
