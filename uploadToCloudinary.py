import cloudinary.uploader
import os
import logging
from datetime import datetime

# Configure Cloudinary with your credentials
cloudinary.config(
  cloud_name='dqpzvvd0v',
  api_key='697515542182727',
  api_secret='yySZgcOxsgnC2dnCLN9IhQLCRuk'
)

# Function to upload images from a folder to Cloudinary
def upload_images_to_cloudinary(folder_path, log_file):
    start_time = datetime.now()

    # Set up logging
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(f"Upload process started at {start_time}")

    # Iterate over files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image (you can modify this condition based on file extensions)
        if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):
            # Extract the original filename
            original_filename = os.path.basename(file_path)

            # Manually specify the public_id (filename) for the Cloudinary upload
            public_id = os.path.splitext(original_filename)[0]

            try:
                # Upload the file to Cloudinary with the specified public_id
                result = cloudinary.uploader.upload(file_path, public_id=public_id, folder="books")
                logging.info(f"Uploaded {original_filename} to Cloudinary. Secure URL: {result['secure_url']}")
            except Exception as e:
                logging.error(f"Failed to upload {original_filename} to Cloudinary. Error: {str(e)}")

    end_time = datetime.now()
    time_taken = end_time - start_time
    logging.info(f"Upload process completed at {end_time}. Time taken: {time_taken}")

# Specify the folder containing images to be uploaded
folder_path = 'assets/book_images'

# Specify the log file path
log_file = 'uploadToCloudinary.log'

# Call the function to upload images to Cloudinary and log the process
upload_images_to_cloudinary(folder_path, log_file)
