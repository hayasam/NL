
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'weather_data'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', '')
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature_for_location():
    try:
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        year = request.args.get('year')
        month = request.args.get('month')
        day = request.args.get('day')
        grib_file = request.args.get('grib_file')

        if not all([latitude, longitude, year, month, day, grib_file]):
            return jsonify({'error': 'Missing required parameters'}), 400

        connection = create_db_connection()
        if connection is None:
            return jsonify({'error': 'Database connection failed'}), 500

        cursor = connection.cursor(dictionary=True)
        
        query = """
        SELECT MAX(temperature) as max_temperature
        FROM temperature_data
        WHERE latitude = %s 
        AND longitude = %s 
        AND YEAR(timestamp) = %s 
        AND MONTH(timestamp) = %s 
        AND DAY(timestamp) = %s 
        AND grib_file = %s
        """
        
        cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
        result = cursor.fetchone()
        
        cursor.close()
        connection.close()

        if result and result['max_temperature'] is not None:
            return jsonify({
                'latitude': latitude,
                'longitude': longitude,
                'year': year,
                'month': month,
                'day': day,
                'grib_file': grib_file,
                'max_temperature': float(result['max_temperature'])
            })
        else:
            return jsonify({
                'latitude': latitude,
                'longitude': longitude,
                'year': year,
                'month': month,
                'day': day,
                'grib_file': grib_file,
                'max_temperature': None,
                'message': 'No data found for the given parameters'
            })

    except ValueError as e:
        return jsonify({'error': 'Invalid parameter format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
