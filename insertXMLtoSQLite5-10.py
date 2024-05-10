import sqlite3
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def create_connection(db_file):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error creating connection: {e}")
    return conn

def create_tables(conn):
    """ Create necessary tables in the database if they do not exist """
    sql_create_authors_table = """CREATE TABLE IF NOT EXISTS author_author (
                                    id INTEGER PRIMARY KEY,
                                    author_name TEXT NOT NULL,
                                    temp_id INTEGER,
                                    author_code TEXT NOT NULL UNIQUE
                                );"""
    sql_create_subject_table = """CREATE TABLE IF NOT EXISTS subject_subject (
                                    id INTEGER PRIMARY KEY,
                                    subject_name TEXT NOT NULL,
                                    temp_id INTEGER,
                                    subject_code TEXT NOT NULL UNIQUE
                                );"""
    sql_create_book_table = """CREATE TABLE IF NOT EXISTS book_book (
                                    id INTEGER PRIMARY KEY,
                                    controlno TEXT NOT NULL,
                                    title TEXT NOT NULL,
                                    author_code TEXT NOT NULL,
                                    edition TEXT,
                                    pagination TEXT,
                                    publisher TEXT,
                                    pubplace TEXT,
                                    copyright TEXT,
                                    isbn TEXT,
                                    subject1_code TEXT,
                                    subject2_code TEXT,
                                    subject3_code TEXT,
                                    series_title TEXT,
                                    aentrytitle TEXT,
                                    aeauthor1_code TEXT,
                                    aeauthor2_code TEXT,
                                    aeauthor3_code TEXT,
                                    FOREIGN KEY (author_code) REFERENCES authors (author_code)
                                );"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_authors_table)
        cursor.execute(sql_create_subject_table)
        cursor.execute(sql_create_book_table)
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")

def insert_author(conn, author_data):
    """ Insert a new author into the author_author table """
    sql = ''' INSERT INTO author_author(author_name, author_code, temp_id) VALUES(?, ?, ?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, author_data)
        conn.commit()
        logging.info(f"Inserted author: {author_data[0]} ({author_data[1]})")
    except sqlite3.Error as e:
        logging.error(f"Error inserting author: {author_data[0]} ({author_data[1]}) - {e}")


def insert_subject(conn, subject_data):
    """ Insert a new subject into the subject_subject table """
    sql = ''' INSERT INTO subject_subject(subject_name, subject_code, temp_id) VALUES(?, ?, NULL) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, subject_data)
        conn.commit()
        logging.info(f"Inserted subject: {subject_data[0]} ({subject_data[1]})")
    except sqlite3.Error as e:
        logging.error(f"Error inserting subject: {subject_data[0]} ({subject_data[1]}) - {e}")


def insert_book(conn, book_data):
    """ Insert a new book into the book_book table """
    sql = ''' INSERT INTO book_book(id, controlno, title, author_code, edition, pagination, publisher, pubplace, copyright, isbn, subject1_code, subject2_code, subject3_code, series_title, aentrytitle, aeauthor1_code, aeauthor2_code, aeauthor3_code) 
              VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, book_data)
        conn.commit()
        logging.info(f"Inserted book: {book_data[1]} by {book_data[2]}")
    except sqlite3.Error as e:
        logging.error(f"Error inserting book: {book_data[1]} by {book_data[2]} - {e}")

def copy_author_table_with_temp_id(conn):
    """ Create a new table with temp_id as primary key and copy data from original author_author table """
    cursor = conn.cursor()
    
    try:
        # Create a new temporary table with the necessary schema
        cursor.execute("""
            CREATE TABLE temp_author_author (
                temp_id INTEGER PRIMARY KEY,
                author_name TEXT NOT NULL,
                author_code TEXT NOT NULL UNIQUE
            )
        """)
        
        # Copy data from author_author to temp_author_author
        cursor.execute("""
            INSERT INTO temp_author_author (temp_id, author_name, author_code)
            SELECT author_code, author_name, author_code
            FROM author_author
        """)
        
        conn.commit()
        logging.info("Created and copied data to temp_author_author table successfully")
    except sqlite3.Error as e:
        logging.error(f"Error creating and copying data to temp_author_author: {e}")

def copy_subject_table_with_temp_id(conn):
    """ Create a new table with temp_id as primary key and copy data from original subject_subject table """
    cursor = conn.cursor()
    
    try:
        # Create a new temporary table with the necessary schema
        cursor.execute("""
            CREATE TABLE temp_subject_subject (
                temp_id INTEGER PRIMARY KEY,
                subject_name TEXT NOT NULL,
                subject_code TEXT NOT NULL UNIQUE
            )
        """)
        
        # Copy data from subject_subject to temp_subject_subject
        cursor.execute("""
            INSERT INTO temp_subject_subject (temp_id, subject_name, subject_code)
            SELECT subject_code, subject_name, subject_code
            FROM subject_subject
        """)
        
        conn.commit()
        logging.info("Created and copied data to temp_subject_subject table successfully")
    except sqlite3.Error as e:
        logging.error(f"Error creating and copying data to temp_subject_subject: {e}")

def rename_and_modify_subject_table(conn):
    """ Rename the temp_subject_subject table to subject_subject and modify its schema """
    cursor = conn.cursor()
    
    try:
        # Drop the original subject_subject table
        cursor.execute("DROP TABLE IF EXISTS subject_subject")
        
        # Rename temp_subject_subject to subject_subject
        cursor.execute("ALTER TABLE temp_subject_subject RENAME TO subject_subject")
        
        # Modify the subject_subject table by setting id as primary key
        cursor.execute("ALTER TABLE subject_subject RENAME COLUMN temp_id TO id")
        
        # Add primary key constraint on id column
        cursor.execute("CREATE UNIQUE INDEX idx_subject_subject_id ON subject_subject (id)")
        
        conn.commit()
        logging.info("Renamed and modified subject_subject table successfully")
    except sqlite3.Error as e:
        logging.error(f"Error renaming and modifying subject_subject table: {e}")


def rename_and_modify_author_table(conn):
    """ Rename the temp_author_author table to author_author and modify its schema """
    cursor = conn.cursor()
    
    try:
        # Drop the original author_author table
        cursor.execute("DROP TABLE IF EXISTS author_author")
        
        # Rename temp_author_author to author_author
        cursor.execute("ALTER TABLE temp_author_author RENAME TO author_author")
        
        # Modify the author_author table by setting id as primary key
        cursor.execute("ALTER TABLE author_author RENAME COLUMN temp_id TO id")
        
        # Add primary key constraint on id column
        cursor.execute("CREATE UNIQUE INDEX idx_author_author_id ON author_author (id)")
        
        conn.commit()
        logging.info("Renamed and modified author_author table successfully")
    except sqlite3.Error as e:
        logging.error(f"Error renaming and modifying author_author table: {e}")


def main():
    database = 'db19.sqlite3'
    conn = create_connection(database)
    if conn is not None:
        create_tables(conn)

        # Process subjects from tblSubject.xml
        tree = ET.parse('tblSubject.xml')
        root = tree.getroot()
        for subject in root.findall('tblSubject'):
            subject_name = subject.find('subject')
            if subject_name is not None:
                subject_name = subject_name.text
            else:
                print("Warning: Subject element not found in tblSubject node")
                continue
            subject_code = subject.find('SubjectCode').text
            subject_data = (subject_name, subject_code)
            insert_subject(conn, subject_data)

        copy_subject_table_with_temp_id(conn)
        rename_and_modify_subject_table(conn)

        # Process authors from tblAuthor.xml
        tree = ET.parse('tblAuthor.xml')
        root = tree.getroot()
        for author in root.findall('tblAuthor'):
            author_name = author.find('Author').text
            author_code = author.find('AuthorCode').text
            author_data = (author_name, author_code, author_code)
            insert_author(conn, author_data)

        copy_author_table_with_temp_id(conn)
        rename_and_modify_author_table(conn)

        # Process books from tblCat.xml
        tree = ET.parse('tblCat.xml')
        root = tree.getroot()
        for record in root.findall('tblCat'):
            controlno = record.find('controlno').text
            title = record.find('Title').text
            author_code = record.find('AuthorCode').text
            edition = record.find('Edition').text
            pagination = record.find('Pagination').text
            publisher = record.find('Publisher').text
            pubplace = record.find('Pubplace').text
            copyright = record.find('Copyright').text
            isbn = record.find('ISBN').text
            subject1_code = record.find('Subject1Code').text
            subject2_code = record.find('Subject2Code').text
            subject3_code = record.find('Subject3Code').text
            series_title = record.find('SeriesTitle').text
            aentrytitle = record.find('AEntryTitle').text
            aeauthor1_code = record.find('AEAuthor1Code').text
            aeauthor2_code = record.find('AEAuthor2Code').text
            aeauthor3_code = record.find('AEAuthor3Code').text
            book_data = (controlno, title, author_code, edition, pagination, publisher, pubplace, copyright, isbn, subject1_code, subject2_code, subject3_code, series_title, aentrytitle, aeauthor1_code, aeauthor2_code, aeauthor3_code)
            insert_book(conn, book_data)

        conn.close()
        logging.info("Data insertion completed successfully.")

if __name__ == '__main__':
    main()