
import sqlite3
import psycopg2
import mysql.connector
from typing import Union, Optional

def check_username_exists(
    username: str,
    db_type: str = "sqlite",
    db_path: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[Union[int, str]] = None,
    database: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None
) -> bool:
    """
    Check if a username exists in the database.
    
    Parameters:
    - username: The username to check
    - db_type: Database type - "sqlite", "postgresql", or "mysql"
    - db_path: Path to SQLite database file (required for SQLite)
    - host, port, database, user, password: Connection parameters for PostgreSQL/MySQL
    
    Returns:
    - True if username exists, False otherwise
    """
    
    connection = None
    cursor = None
    
    try:
        # Establish database connection based on type
        if db_type == "sqlite":
            if not db_path:
                raise ValueError("db_path is required for SQLite")
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            
        elif db_type == "postgresql":
            if not all([host, database, user]):
                raise ValueError("host, database, and user are required for PostgreSQL")
            connection = psycopg2.connect(
                host=host,
                port=port or 5432,
                database=database,
                user=user,
                password=password
            )
            cursor = connection.cursor()
            
        elif db_type == "mysql":
            if not all([host, database, user]):
                raise ValueError("host, database, and user are required for MySQL")
            connection = mysql.connector.connect(
                host=host,
                port=port or 3306,
                database=database,
                user=user,
                password=password
            )
            cursor = connection.cursor()
            
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
        
        # Execute query to check if username exists
        # Assuming table name is 'users' and column name is 'username'
        query = "SELECT COUNT(*) FROM users WHERE username = %s"
        param_style = "%s"
        
        if db_type == "sqlite":
            query = "SELECT COUNT(*) FROM users WHERE username = ?"
            param_style = "?"
        
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        # Return True if count > 0, False otherwise
        return result[0] > 0 if result else False
        
    except Exception as e:
        print(f"Database error: {e}")
        return False
        
    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Alternative simplified version for SQLite only
def check_username_simple(username: str, db_path: str) -> bool:
    """Simplified version for SQLite databases."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except sqlite3.Error:
        return False
