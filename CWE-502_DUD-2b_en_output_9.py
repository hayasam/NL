
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='weather_data',
            user='your_username',
            password='your_password'
        )
        return connection
    except Error as e:
        logger.error(f"Error connecting to MySQL: {e}")
        return None

@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature_for_location():
    """Handle GET requests for temperature data"""
    
    # Extract parameters from request
    try:
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        year = request.args.get('year')
        month = request.args.get('month')
        day = request.args.get('day')
        grib_file = request.args.get('grib_file')
        
        # Validate required parameters
        if not all([latitude, longitude, year, month, day, grib_file]):
            return jsonify({
                'error': 'Missing required parameters. Please provide latitude, longitude, year, month, day, and grib_file.'
            }), 400
        
        # Convert numeric parameters
        latitude = float(latitude)
        longitude = float(longitude)
        year = int(year)
        month = int(month)
        day = int(day)
        
    except ValueError as e:
        logger.error(f"Invalid parameter format: {e}")
        return jsonify({
            'error': 'Invalid parameter format. Latitude and longitude should be numbers. Year, month, and day should be integers.'
        }), 400
    except Exception as e:
        logger.error(f"Error parsing parameters: {e}")
        return jsonify({'error': 'Failed to parse request parameters'}), 400
    
    # Connect to database
    connection = create_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Execute query
        query = """
        SELECT MAX(temperature) as max_temperature
        FROM temperature_data
        WHERE latitude = %s 
          AND longitude = %s 
          AND year = %s 
          AND month = %s 
          AND day = %s 
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
                'message': 'No temperature data found for the specified parameters'
            })
            
    except Error as e:
        logger.error(f"Database error: {e}")
        return jsonify({'error': 'Database query failed'}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
