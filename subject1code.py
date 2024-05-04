import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='updateSubject1Code.log', level=logging.INFO)

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database {db_file}: {e}")
    return conn

def update_books_with_subject1_code_containing_zero(db_file):
    """ Update books with subject1_code containing '0' to new value '2' in the 'book_book' table """
    conn = create_connection(db_file)
    if conn is not None:
        try:
            cur = conn.cursor()
            # Update rows where subject1_code contains '0' to new value '2'
            cur.execute('''UPDATE book_book SET subject1_code = '2' WHERE subject1_code LIKE '%0%' ''')
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
    db_file = 'db17.sqlite3'
    update_books_with_subject1_code_containing_zero(db_file)
