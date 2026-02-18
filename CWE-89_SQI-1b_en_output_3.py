
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                subscribed BOOLEAN DEFAULT 1
            )
        ''')
        conn.commit()
        conn.close()

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')
    
    if not email:
        return jsonify({'error': 'Email parameter is required'}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        
        if user:
            cursor.execute('DELETE FROM users WHERE email = ?', (email,))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Successfully unsubscribed and removed from database'}), 200
        else:
            conn.close()
            return jsonify({'message': 'User is not subscribed'}), 404
            
    except Exception as e:
        conn.close()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
