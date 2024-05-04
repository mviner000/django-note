import sqlite3

def update_data(conn):
    # Update the author_code with id 9999 to 2
    update_author_code(conn, 9999, '0')

    # Update the subject_code with id 9998 to 3
    update_subject_code(conn, 9998, '0')

def update_author_code(conn, id, author_code):
    """ Update the author_code of the author with the given id """
    sql = ''' UPDATE author_author SET author_code = ? WHERE id = ? '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (author_code, id))
        conn.commit()
        print(f"Updated author_code of author with id {id} to {author_code}")
    except sqlite3.Error as e:
        print(f"Error updating author_code of author with id {id} - {e}")

def update_subject_code(conn, id, subject_code):
    """ Update the subject_code of the subject with the given id """
    sql = ''' UPDATE subject_subject SET subject_code = ? WHERE id = ? '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (subject_code, id))
        conn.commit()
        print(f"Updated subject_code of subject with id {id} to {subject_code}")
    except sqlite3.Error as e:
        print(f"Error updating subject_code of subject with id {id} - {e}")

if __name__ == '__main__':
    # Create a connection to the database
    conn = sqlite3.connect('db17.sqlite3')

    # Update data in the database
    update_data(conn)

    # Close the connection
    conn.close()