import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='updateSubject2Code.log', level=logging.INFO)

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database {db_file}: {e}")
    return conn

def count_books_with_subject3_code_containing_zero(db_file):
    """ Count books where subject2_code contains '0' in the 'book_book' table """
    conn = create_connection(db_file)
    count = 0
    if conn is not None:
        try:
            cur = conn.cursor()
            # Count rows where subject3_code contains '0'
            cur.execute('''SELECT COUNT(*) FROM book_book WHERE subject2_code LIKE '%0%' ''')
            count = cur.fetchone()[0]
            logging.info(f"Found {count} books with subject2_code containing '0'")
        except sqlite3.Error as e:
            logging.error(f"Error counting books: {e}")
        finally:
            conn.close()
    else:
        logging.error("Database connection failed")
    return count

def update_books_with_subject1_code_containing_zero(db_file):
    """ Update books with subject2_code containing '0' to new value '2' in the 'book_book' table """
    conn = create_connection(db_file)
    if conn is not None:
        try:
            cur = conn.cursor()
            # Update rows where subject3_code contains '0' to new value '2'
            cur.execute('''UPDATE book_book SET subject2_code = '1' WHERE subject3_code LIKE '%0%' ''')
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
    db_file = 'db18.sqlite3'
    # Count and log the number of books with subject3_code containing '0'
    count = count_books_with_subject3_code_containing_zero(db_file)
    # Update books with subject3_code containing '0' to '2'
    update_books_with_subject1_code_containing_zero(db_file)
