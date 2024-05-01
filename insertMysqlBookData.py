import mysql.connector
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def create_connection():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    return conn

def insert_author(conn, author_data):
    """ Insert a new author into the author_author table """
    sql = """ INSERT INTO author_author(author_name, author_code) VALUES(%s, %s) """
    cursor = conn.cursor()
    try:
        cursor.execute(sql, author_data)
        conn.commit()
        print(f"Inserted author: {author_data[0]} ({author_data[1]})")
    except mysql.connector.Error as e:
        print(f"Error inserting author: {author_data[0]} ({author_data[1]}) - {e}")

def insert_book(conn, book_data):
    """ Insert a new book into the book_book table """
    sql = """ INSERT INTO book_book(controlno, title, author_code, edition, pagination, publisher, pubplace, copyright, isbn, subject1_code, subject2_code, subject3_code, series_title, aentrytitle, aeauthor1_code, aeauthor2_code, aeauthor3_code) 
              VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
    cursor = conn.cursor()
    try:
        cursor.execute(sql, book_data)
        conn.commit()
        print(f"Inserted book: {book_data[1]} by {book_data[2]}")
    except mysql.connector.Error as e:
        print(f"Error inserting book: {book_data[1]} by {book_data[2]} - {e}")

def main():
    conn = create_connection()
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