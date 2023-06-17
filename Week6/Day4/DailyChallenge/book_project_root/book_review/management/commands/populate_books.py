import requests
from book_review.models import Book
from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):
    help = 'Populates the Book model with data from the Google Books API'
    
    def handle(self, *args, **options):
        def fetch_and_populate_books():
            url = 'https://www.googleapis.com/books/v1/volumes?q=python'  # Replace 'python' with your desired search query
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                for item in data.get('items', []):
                    volume_info = item.get('volumeInfo', {})
                    
                    published_date = volume_info.get('publishedDate')
                    if published_date:
                        try:
                            published_date = datetime.strptime(published_date, '%Y-%m-%d').date()
                        except ValueError:
                            try:
                                published_date = datetime.strptime(published_date, '%Y-%m').date()
                            except ValueError:
                                try:
                                    published_date = datetime.strptime(published_date, '%Y').date()
                                except ValueError:
                                    published_date = None  # Set to None if the date format is not recognized

                    book = Book(
                        title=volume_info.get('title', ''),
                        author=', '.join(volume_info.get('authors', [])),
                        published_date=published_date,
                        description=volume_info.get('description', ''),
                        page_count=volume_info.get('pageCount', 0),
                        categories=', '.join(volume_info.get('categories', [])),
                        thumbnail_url=volume_info.get('imageLinks', {}).get('thumbnail', '')
                    )
                    book.save()

                print('Books successfully populated.')
            else:
                print('Failed to fetch books from the API.')
                
        fetch_and_populate_books()

