import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='subject2Code.log', level=logging.INFO)

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database {db_file}: {e}")
    return conn

def update_value(db_file):
    """ Update the value from 1234 to 2 in the 'subject1_code' column of the 'book_book' table """
    conn = create_connection(db_file)
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute('''UPDATE book_book SET subject1_code = 2 WHERE subject1_code = 1234''')
            conn.commit()
            logging.info("Value updated successfully")
        except sqlite3.Error as e:
            logging.error(f"Error updating value: {e}")
        finally:
            conn.close()
    else:
        logging.error("Database connection failed")

# Example usage
if __name__ == '__main__':
    db_file = 'db17.sqlite3'
    update_value(db_file)
