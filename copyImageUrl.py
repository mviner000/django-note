import os
import sqlite3
import logging
from datetime import datetime

# SQLite database path
DB_PATH = 'db19.sqlite3'

# Initialize logging
logging.basicConfig(filename='copyingImageUrl.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def copy_thumbnail_to_image_url():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch all records from the Book table
        cursor.execute("SELECT id, thumbnail_url FROM book_book")
        rows = cursor.fetchall()

        for row in rows:
            book_id, thumbnail_url = row

            # Update image_url with thumbnail_url
            cursor.execute("UPDATE book_book SET image_url = ? WHERE id = ?", (thumbnail_url, book_id))

        # Commit the transaction
        conn.commit()

        # Log success message
        logging.info("Successfully copied thumbnail_url to image_url for all records.")

    except Exception as e:
        # Log error message
        logging.error(f"Error occurred: {str(e)}")

    finally:
        # Close the database connection
        if conn:
            conn.close()

if __name__ == "__main__":
    start_time = datetime.now()
    copy_thumbnail_to_image_url()
    end_time = datetime.now()
    # Calculate execution time
    execution_time = end_time - start_time
    # Log execution time
    logging.info(f"Execution time: {execution_time}")
