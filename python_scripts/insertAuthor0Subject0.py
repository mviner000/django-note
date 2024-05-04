import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def insert_data(conn):
    # Define the author data
    author_data = ('macabagdal', '9998')

    # Insert the author
    insert_author(conn, author_data)

    # Define the subject data
    subject_data = ('computeran', '9998')

    # Insert the subject
    insert_subject(conn, subject_data)

def insert_author(conn, author_data):
    """ Insert a new author into the author_author table """
    sql = ''' INSERT INTO author_author(author_name, author_code) VALUES(?, ?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, author_data)
        conn.commit()
        print(f"Inserted author: {author_data[0]} ({author_data[1]})")
    except sqlite3.Error as e:
        print(f"Error inserting author: {author_data[0]} ({author_data[1]}) - {e}")

def insert_subject(conn, subject_data):
    """ Insert a new subject into the subject_subject table """
    sql = ''' INSERT INTO subject_subject(subject_name, subject_code) VALUES(?,?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, subject_data)
        conn.commit()
        print(f"Inserted subject: {subject_data[0]} ({subject_data[1]})")
    except sqlite3.Error as e:
        print(f"Error inserting subject: {subject_data[0]} ({subject_data[1]}) - {e}")

if __name__ == '__main__':
    # Create a connection to the database
    conn = create_connection('db17.sqlite3')

    # Insert data into the database
    insert_data(conn)

    # Close the connection
    conn.close()