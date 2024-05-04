import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='updateAuthorCode.log', level=logging.INFO)

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database {db_file}: {e}")
    return conn

def find_books_with_author_code_containing_zero(db_file):
    """ Find all books with author_code containing '0' in the 'book_book' table """
    conn = create_connection(db_file)
    if conn is not None:
        try:
            cur = conn.cursor()
            # Use LIKE operator to find author_code containing '0'
            cur.execute('''SELECT * FROM book_book WHERE author_code LIKE '%0%' ''')
            rows = cur.fetchall()
            if rows:
                logging.info(f"Found {len(rows)} books with author_code containing '0'")
                return rows
            else:
                logging.info("No books found with author_code containing '0'")
                return []
        except sqlite3.Error as e:
            logging.error(f"Error querying database: {e}")
            return []
        finally:
            conn.close()
    else:
        logging.error("Database connection failed")
        return []

def update_author_code_for_books(rows, new_author_code, db_file):
    """ Update author_code for the specified books to a new value in the 'book_book' table """
    conn = create_connection(db_file)
    if conn is not None:
        try:
            cur = conn.cursor()
            for row in rows:
                book_id = row[0]  # Assuming the first column is the book_id
                cur.execute('''UPDATE book_book SET author_code = ? WHERE id = ?''', (new_author_code, book_id))
            conn.commit()
            logging.info("Updated author_code for books successfully")
        except sqlite3.Error as e:
            logging.error(f"Error updating author_code: {e}")
        finally:
            conn.close()
    else:
        logging.error("Database connection failed")

# Example usage
if __name__ == '__main__':
    db_file = 'db17.sqlite3'
    rows_with_author_code_zero = find_books_with_author_code_containing_zero(db_file)
    if rows_with_author_code_zero:
        update_author_code_for_books(rows_with_author_code_zero, '2', db_file)
