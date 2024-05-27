import logging
from datetime import datetime
from .models import Book

# Initialize logging
logging.basicConfig(filename='search_results.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def search_books(query):
    try:
        start_time = datetime.now()
        
        # Search for books containing the query in the title
        books = Book.objects.filter(title__icontains=query).values('id', 'title', 'image_url')
        
        
        # Calculate time taken in seconds
        end_time = datetime.now()
        time_taken = (end_time - start_time).total_seconds()

        # Log search success
        logging.info(f"Search query '{query}' completed successfully. Time taken: {time_taken:.2f} seconds. Results: {books}")

        return list(books)  # Convert queryset to a list of dictionaries
    except Exception as e:
        # Log errors
        logging.error(f"Error occurred during search query '{query}': {e}")
        return None

def main():
    # Prompt user for search query
    query = input("Enter search query: ")

    # Search for books
    books = search_books(query)

    # Display search results
    if books:
        print("Search results:")
        for book in books:
            print(book)
    else:
        print("An error occurred while searching. Please check the log file for details.")

if __name__ == "__main__":
    main()
