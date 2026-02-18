
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import pool
import os
from datetime import datetime

app = Flask(__name__)

# Database connection pool
db_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,
    host=os.getenv('DB_HOST', 'localhost'),
    database=os.getenv('DB_NAME', 'weather_db'),
    user=os.getenv('DB_USER', 'postgres'),
    password=os.getenv('DB_PASSWORD', ''),
    port=os.getenv('DB_PORT', '5432')
)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Get parameters from request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date_str = request.args.get('date')
    
    # Validate required parameters
    if not all([latitude, longitude, date_str]):
        return jsonify({'error': 'Missing required parameters: latitude, longitude, date'}), 400
    
    # Validate date format
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    
    # Validate latitude and longitude
    try:
        lat = float(latitude)
        lon = float(longitude)
        if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
            return jsonify({'error': 'Invalid latitude or longitude values'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid latitude or longitude format'}), 400
    
    conn = None
    try:
        # Get connection from pool
        conn = db_pool.getconn()
        cursor = conn.cursor()
        
        # Execute query
        query = """
            SELECT temperature 
            FROM temperature_data 
            WHERE latitude = %s 
            AND longitude = %s 
            AND date = %s
        """
        cursor.execute(query, (lat, lon, date_obj))
        
        result = cursor.fetchone()
        
        if result:
            temperature = result[0]
            return jsonify({
                'latitude': lat,
                'longitude': lon,
                'date': date_str,
                'temperature': float(temperature)
            })
        else:
            return jsonify({
                'error': 'No temperature data found for the specified location and date'
            }), 404
            
    except psycopg2.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500
    finally:
        if conn:
            cursor.close()
            db_pool.putconn(conn)

if __name__ == '__main__':
    app.run(debug=True)
