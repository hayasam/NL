
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
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                is_moderator BOOLEAN DEFAULT FALSE
            )
        ''')
        conn.commit()
        conn.close()

@app.route('/check_moderator', methods=['GET'])
def check_moderator():
    username = request.args.get('username')
    
    if not username:
        return jsonify({'error': 'Username parameter is required'}), 400
    
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT is_moderator FROM users WHERE username = ?',
            (username,)
        )
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            is_moderator = bool(result[0])
            return jsonify({
                'username': username,
                'is_moderator': is_moderator
            })
        else:
            return jsonify({
                'username': username,
                'is_moderator': False,
                'message': 'User not found'
            }), 404
            
    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
