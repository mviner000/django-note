import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='updateaeauthor1Code.log', level=logging.INFO)

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database {db_file}: {e}")
    return conn

def update_books_with_aeauthor1_code(db_file):
    """ Update books with aeauthor1_code containing '2' to new value '9999' in the 'book_book' table """
    conn = create_connection(db_file)
    if conn is not None:
        try:
            cur = conn.cursor()
            # Update rows where aeauthor1_code contains '3546' to new value '9999'
            cur.execute('''UPDATE book_book SET aeauthor1_code = '9999' WHERE aeauthor1_code = '2' ''')
            conn.commit()
            logging.info("Updated books successfully")
        except sqlite3.Error as e:
            logging.error(f"Error updating books: {e}")
        finally:
            conn.close()
    else:
        logging.error("Database connection failed")

# Example usage
if __name__ == '__main__':
    db_file = 'db19.sqlite3'
    # Update books with aeauthor1_code containing '3546' to '9999'
    update_books_with_aeauthor1_code(db_file)
