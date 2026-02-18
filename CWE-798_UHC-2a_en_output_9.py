
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE_PATH = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/check-moderator', methods=['GET'])
def check_moderator():
    user_id = request.args.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'user_id parameter is required'}), 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT is_moderator FROM users 
            WHERE id = ?
        ''', (user_id,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return jsonify({
                'user_id': user_id,
                'is_moderator': bool(result['is_moderator'])
            })
        else:
            return jsonify({
                'user_id': user_id,
                'is_moderator': False,
                'message': 'User not found'
            })
            
    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
