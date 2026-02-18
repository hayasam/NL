
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Sensor',
            user='your_username',
            password='your_password'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No payload provided'}), 400
    
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    date_str = data.get('date')
    
    if not all([latitude, longitude, date_str]):
        return jsonify({'error': 'Missing required parameters'}), 400
    
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    
    connection = create_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT temperature 
            FROM temperature_data 
            WHERE latitude = %s 
            AND longitude = %s 
            AND DATE(timestamp) = %s
            LIMIT 1
        """
        cursor.execute(query, (latitude, longitude, date_obj))
        result = cursor.fetchone()
        
        if result:
            return jsonify({'temperature': result['temperature']}), 200
        else:
            return jsonify({'error': 'No temperature data found for the given location and date'}), 404
            
    except Error as e:
        return jsonify({'error': f'Database error: {e}'}), 500
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
