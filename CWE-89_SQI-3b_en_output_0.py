
from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Messages</title>
</head>
<body>
    <h1>Post a Message</h1>
    <form action="/post" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <br><br>
        <textarea name="message" placeholder="Message" required></textarea>
        <br><br>
        <button type="submit">Post</button>
    </form>
    
    <h2>Messages</h2>
    <ul>
        {% for message in messages %}
        <li><strong>{{ message[0] }}:</strong> {{ message[1] }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

def init_db():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (username TEXT, message TEXT)''')
    conn.commit()
    conn.close()

def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (username, message) VALUES (?, ?)", 
              (username, message))
    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("SELECT username, message FROM messages ORDER BY rowid DESC")
    messages = c.fetchall()
    conn.close()
    return messages

@app.route('/')
def index():
    messages = get_all_messages()
    return render_template_string(HTML_TEMPLATE, messages=messages)

@app.route('/post', methods=['POST'])
def post():
    username = request.form.get('username')
    message = request.form.get('message')
    
    if username and message:
        insert_user_message_in_db(username, message)
    
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
