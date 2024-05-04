import sqlite3
import logging

# configure logging
logging.basicConfig(filename='updatedSubjectCode.log', level=logging.INFO)

def update_zero_values(db_file, subject2_code):
    """ Update all '607' values in 'subject2_code' column of 'book_book' table to the specified subject2_code value and log the updated records and any errors to a file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute('''SELECT id FROM book_book WHERE subject2_code = '607' ''')
        ids = [row[0] for row in cur.fetchall()]
        num_updated = 0
        num_errors = 0
        for id_ in ids:
            try:
                cur.execute('''UPDATE book_book SET subject2_code = ? WHERE id = ?''', (subject2_code, id_))
                num_updated += 1
                logging.info(f'Updated subject2_code from "607" to "{subject2_code}" for id {id_}' )
            except sqlite3.Error as e:
                num_errors += 1
                logging.error(f'Error updating subject2_code for id {id_}: {e}', exc_info=True)
        conn.commit()
    except sqlite3.Error as e:
        num_errors += 1
        logging.error(f'Error connecting to database: {e}', exc_info=True)
    finally:
        if conn:
            conn.close()
    return num_updated, num_errors

if __name__ == '__main__':
    db_file = 'db17.sqlite3'  # replace with your database file name
    subject2_code = input('Enter the desired subject2_code value: ')
    num_updated, num_errors = update_zero_values(db_file, subject2_code)
    print(f'Updated {num_updated} records with subject2_code = "607" to "{subject2_code}"')
    if num_errors > 0:
        print(f'Encountered {num_errors} errors during the update process')