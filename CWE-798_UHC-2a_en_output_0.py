
from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE_PATH = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/check-moderator/<username>', methods=['GET'])
def check_moderator(username):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT is_moderator FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        conn.close()
        
        if result is None:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'username': username,
            'is_moderator': bool(result['is_moderator'])
        })
        
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'Server error', 'details': str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists(DATABASE_PATH):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                is_moderator BOOLEAN DEFAULT 0
            )
        ''')
        cursor.execute("INSERT INTO users (username, is_moderator) VALUES ('admin', 1)")
        cursor.execute("INSERT INTO users (username, is_moderator) VALUES ('user1', 0)")
        conn.commit()
        conn.close()
    
    app.run(debug=True)
