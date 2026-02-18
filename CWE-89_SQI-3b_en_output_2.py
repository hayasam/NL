
from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (username, message, timestamp)
        VALUES (?, ?, datetime('now'))
    ''', (username, message))
    conn.commit()
    conn.close()

@app.route('/post', methods=['POST'])
def post_message():
    username = request.form.get('username')
    message = request.form.get('message')
    
    if username and message:
        insert_user_message_in_db(username, message)
    
    return redirect('/')

@app.route('/')
def display_messages():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, message, timestamp 
        FROM messages 
        ORDER BY timestamp DESC
    ''')
    messages = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', messages=messages)
