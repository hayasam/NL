
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_db_connection():
    """Create and return a database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='weather_db',
            user='your_username',
            password='your_password'
        )
        return connection
    except Error as e:
        logger.error(f"Error connecting to MySQL: {e}")
        return None

@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature_for_location():
    """Endpoint to get maximum temperature for given parameters."""
    
    # Extract parameters from request
    try:
        latitude = request.args.get('latitude', type=float)
        longitude = request.args.get('longitude', type=float)
        year = request.args.get('year', type=int)
        month = request.args.get('month', type=int)
        day = request.args.get('day', type=int)
        grib_file = request.args.get('grib_file', type=str)
        
        # Validate required parameters
        if None in (latitude, longitude, year, month, day, grib_file):
            return jsonify({'error': 'Missing required parameters'}), 400
            
    except ValueError as e:
        return jsonify({'error': f'Invalid parameter type: {str(e)}'}), 400
    
    connection = None
    cursor = None
    
    try:
        # Create database connection
        connection = create_db_connection()
        if connection is None:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        # Execute query
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
            
    except Error as e:
        logger.error(f"Database error: {e}")
        return jsonify({'error': 'Database query failed'}), 500
        
    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
