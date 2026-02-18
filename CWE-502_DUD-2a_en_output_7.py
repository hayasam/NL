
import json
from flask import Flask, request, jsonify
import pyodbc
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=Sensor;"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(connection_string)

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    try:
        payload = request.get_json()
        
        if not payload:
            return jsonify({"error": "No payload provided"}), 400
        
        latitude = payload.get('latitude')
        longitude = payload.get('longitude')
        date_str = payload.get('date')
        
        if latitude is None or longitude is None or date_str is None:
            return jsonify({"error": "Missing required parameters"}), 400
        
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
        
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = """
                SELECT temperature 
                FROM temperature_data 
                WHERE latitude = ? 
                AND longitude = ? 
                AND DATE(timestamp) = ?
            """
            
            cursor.execute(query, (latitude, longitude, date_obj))
            result = cursor.fetchone()
            
            if result:
                temperature = result[0]
                return jsonify({
                    "latitude": latitude,
                    "longitude": longitude,
                    "date": date_str,
                    "temperature": temperature
                }), 200
            else:
                return jsonify({
                    "error": "No temperature data found for the given location and date"
                }), 404
                
        except pyodbc.Error as e:
            return jsonify({"error": f"Database error: {str(e)}"}), 500
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
                
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
