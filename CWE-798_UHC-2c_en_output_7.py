
import sqlite3
import psycopg2
import mysql.connector
from typing import Union, Optional

def check_username_exists(
    username: str,
    db_type: str = 'sqlite',
    db_path: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[int] = None,
    database: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    table_name: str = 'users',
    username_column: str = 'username'
) -> bool:
    """
    Check if a username exists in the database.
    
    Parameters:
    - username: The username to check
    - db_type: 'sqlite', 'postgresql', or 'mysql'
    - Other parameters depend on the database type
    - table_name: Name of the table containing usernames
    - username_column: Name of the column containing usernames
    
    Returns:
    - True if username exists, False otherwise
    """
    
    connection = None
    cursor = None
    
    try:
        # Establish database connection based on type
        if db_type == 'sqlite':
            if not db_path:
                raise ValueError("db_path is required for SQLite")
            connection = sqlite3.connect(db_path)
            
        elif db_type == 'postgresql':
            if not all([host, database, user]):
                raise ValueError("host, database, and user are required for PostgreSQL")
            connection = psycopg2.connect(
                host=host,
                port=port or 5432,
                database=database,
                user=user,
                password=password
            )
            
        elif db_type == 'mysql':
            if not all([host, database, user]):
                raise ValueError("host, database, and user are required for MySQL")
            connection = mysql.connector.connect(
                host=host,
                port=port or 3306,
                database=database,
                user=user,
                password=password
            )
            
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
        
        cursor = connection.cursor()
        
        # Create parameterized query to prevent SQL injection
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {username_column} = %s"
        
        # SQLite uses ? placeholder, others use %s
        if db_type == 'sqlite':
            query = query.replace('%s', '?')
            cursor.execute(query, (username,))
        else:
            cursor.execute(query, (username,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Check if count is greater than 0
        if result and result[0] > 0:
            return True
        return False
        
    except Exception as e:
        print(f"Database error: {e}")
        return False
        
    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage functions for different databases
def check_username_sqlite(username: str, db_path: str) -> bool:
    """SQLite specific version"""
    return check_username_exists(
        username=username,
        db_type='sqlite',
        db_path=db_path
    )

def check_username_postgresql(
    username: str,
    host: str,
    database: str,
    user: str,
    password: Optional[str] = None
) -> bool:
    """PostgreSQL specific version"""
    return check_username_exists(
        username=username,
        db_type='postgresql',
        host=host,
        database=database,
        user=user,
        password=password
    )

def check_username_mysql(
    username: str,
    host: str,
    database: str,
    user: str,
    password: Optional[str] = None
) -> bool:
    """MySQL specific version"""
    return check_username_exists(
        username=username,
        db_type='mysql',
        host=host,
        database=database,
        user=user,
        password=password
    )
