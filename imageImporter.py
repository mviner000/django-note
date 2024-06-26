import os
import sqlite3
from PIL import Image
import logging
from datetime import datetime

# SQLite database path
DB_PATH = 'db19.sqlite3'

# Folder containing images
IMAGE_FOLDER = 'assets/book_images'

# Setup logging
logging.basicConfig(filename='imageImporter.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def update_database_with_image_info():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # List all image files in the IMAGE_FOLDER
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]

    for filename in image_files:
        # Extract controlno from the image filename
        controlno = os.path.splitext(filename)[0]

        # Query the database for the corresponding record
        cursor.execute("SELECT * FROM book_book WHERE controlno=?", (controlno,))
        record = cursor.fetchone()

        if record:
            try:
                # Get full image path
                image_path = os.path.join(IMAGE_FOLDER, filename)

                # Open image using PIL (Pillow)
                with Image.open(image_path) as img:
                    # Get image dimensions
                    width, height = img.size

                    # Update database record with image info
                    thumbnail_url = f"{filename}"
                    thumbnail_width = width
                    thumbnail_height = height

                    # Update database record
                    cursor.execute("UPDATE book_book SET thumbnail_url=?, thumbnail_width=?, thumbnail_height=? WHERE controlno=?", 
                                   (thumbnail_url, thumbnail_width, thumbnail_height, controlno))
                    conn.commit()
                    
                    # Log success message
                    logging.info(f"Updated record for controlno {controlno}")

            except Exception as e:
                # Log error message
                logging.error(f"Error processing image {filename}: {e}")

        else:
            # Log warning if controlno not found in database
            logging.warning(f"Controlno {controlno} not found in database for image {filename}")

    # Close database connection
    conn.close()

if __name__ == '__main__':
    logging.info("Starting image import process...")
    update_database_with_image_info()
    logging.info("Image import process completed.")
