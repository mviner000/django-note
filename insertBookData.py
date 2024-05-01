import sqlite3
import xml.etree.ElementTree as ET

def create_connection(db_file):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# def create_tables(conn):
#     """ Create necessary tables in the database if they do not exist """
#     sql_create_authors_table = """CREATE TABLE IF NOT EXISTS authors (
#                                     id INTEGER PRIMARY KEY,
#                                     author_name TEXT NOT NULL,
#                                     author_code TEXT NOT NULL UNIQUE
#                                 );"""
#     sql_create_book_table = """CREATE TABLE IF NOT EXISTS book_book (
#                                     id INTEGER PRIMARY KEY,
#                                     controlno TEXT NOT NULL,
#                                     title TEXT NOT NULL,
#                                     author_code TEXT NOT NULL,
#                                     edition TEXT,
#                                     pagination TEXT,
#                                     publisher TEXT,
#                                     pubplace TEXT,
#                                     copyright TEXT,
#                                     isbn TEXT,
#                                     subject1_code TEXT,
#                                     subject2_code TEXT,
#                                     subject3_code TEXT,
#                                     series_title TEXT,
#                                     aentrytitle TEXT,
#                                     aeauthor1_code TEXT,
#                                     aeauthor2_code TEXT,
#                                     aeauthor3_code TEXT,
#                                     FOREIGN KEY (author_code) REFERENCES authors (author_code)
#                                 );"""
#     try:
#         cursor = conn.cursor()
#         cursor.execute(sql_create_authors_table)
#         cursor.execute(sql_create_book_table)
#     except sqlite3.Error as e:
#         print(e)

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

def insert_book(conn, book_data):
    """ Insert a new book into the book_book table """
    sql = ''' INSERT INTO book_book(controlno, title, author_code, edition, pagination, publisher, pubplace, copyright, isbn, subject1_code, subject2_code, subject3_code, series_title, aentrytitle, aeauthor1_code, aeauthor2_code, aeauthor3_code) 
              VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, book_data)
        conn.commit()
        print(f"Inserted book: {book_data[1]} by {book_data[2]}")
    except sqlite3.Error as e:
        print(f"Error inserting book: {book_data[1]} by {book_data[2]} - {e}")

def main():
    database = 'localDB.sqlite3'
    conn = create_connection(database)
    if conn is not None:
        # create_tables(conn)

        # Process authors from tblAuthor.xml
        tree = ET.parse('tblAuthor.xml')
        root = tree.getroot()
        for author in root.findall('tblAuthor'):
            author_name = author.find('Author').text
            author_code = author.find('AuthorCode').text
            author_data = (author_name, author_code)
            insert_author(conn, author_data)

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
        print("Data insertion completed successfully.")

if __name__ == '__main__':
    main()
