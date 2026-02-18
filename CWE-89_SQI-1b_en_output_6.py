
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        conn.execute('''
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
    
    conn = get_db_connection()
    
    try:
        # Check if email exists in database
        user = conn.execute(
            'SELECT * FROM users WHERE email = ?', 
            (email,)
        ).fetchone()
        
        if user is None:
            return jsonify({'message': 'User is not subscribed'}), 404
        
        # Delete user from database
        conn.execute('DELETE FROM users WHERE email = ?', (email,))
        conn.commit()
        
        # Here you would typically call your mailing list service API
        # Example: mailchimp_api.unsubscribe(email)
        
        return jsonify({
            'message': 'Successfully unsubscribed',
            'email': email
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
