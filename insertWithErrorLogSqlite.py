import logging
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

# Configure logging to write to a file
logging.basicConfig(level=logging.INFO,  # Set the logging level to INFO or your desired level
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='script.log',  # Specify the name of the log file
                    filemode='a')  # 'a' appends to the file if it already exists, 'w' would overwrite

def insert_author(conn, author_data):
    """ Insert a new author into the author_author table """
    sql = ''' INSERT INTO author_author(author_name, author_code) VALUES(?, ?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, author_data)
        conn.commit()
        logging.info(f"Inserted author: {author_data[0]} ({author_data[1]})")
    except sqlite3.Error as e:
        logging.error(f"Error inserting author: {author_data[0]} ({author_data[1]}) - {e}")

def insert_subject(conn, subject_data):
    """ Insert a new subject into the subject_subject table """
    sql = ''' INSERT INTO subject_subject(subject_name, subject_code) VALUES(?,?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, subject_data)
        conn.commit()
        logging.info(f"Inserted subject: {subject_data[0]} ({subject_data[1]})")
    except sqlite3.Error as e:
        logging.error(f"Error inserting subject: {subject_data[0]} ({subject_data[1]}) - {e}")

def insert_book(conn, book_data):
    """ Insert a new book into the book_book table """
    sql = ''' INSERT INTO book_book(controlno, title, author_code, edition, pagination, publisher, pubplace, copyright, isbn, subject1_code, subject2_code, subject3_code, series_title, aentrytitle, aeauthor1_code, aeauthor2_code, aeauthor3_code) 
              VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, book_data)
        conn.commit()
        logging.info(f"Inserted book: {book_data[1]} by {book_data[2]}")
    except sqlite3.Error as e:
        logging.error(f"Error inserting book: {book_data[1]} by {book_data[2]} - {e}")

def main():
    database = 'db18.sqlite3'
    conn = create_connection(database)
    if conn is not None:
        # create_tables(conn)

        # Process subjects from tblSubject.xml
        tree = ET.parse('tblSubject.xml')
        root = tree.getroot()
        for subject in root.findall('tblSubject'):
            subject_name = subject.find('subject')
            if subject_name is not None:
                subject_name = subject_name.text
            else:
                logging.warning("Subject element not found in tblSubject node")
                continue
            subject_code = subject.find('SubjectCode').text
            subject_data = (subject_name, subject_code)
            insert_subject(conn, subject_data)
            
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
        logging.info("Data insertion completed successfully.")

if __name__ == '__main__':
    main()
