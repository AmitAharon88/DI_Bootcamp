import requests
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_project.settings")
django.setup()

from book_review.models import Book

def populate_books():
    # Retrieve data from the Google Books API
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=python')
    data = response.json()

    # Process the retrieved data and create Book objects
    for item in data.get('items', []):
        volume_info = item.get('volumeInfo')
        title = volume_info.get('title')
        author = volume_info.get('authors', ['Unknown Author'])[0]
        published_date = volume_info.get('publishedDate')
        description = volume_info.get('description', '')
        page_count = volume_info.get('pageCount', 0)
        categories = ', '.join(volume_info.get('categories', []))
        thumbnail_url = volume_info.get('imageLinks', {}).get('thumbnail', '')

        book = Book(
            title=title,
            author=author,
            published_date=published_date,
            description=description,
            page_count=page_count,
            categories=categories,
            thumbnail_url=thumbnail_url
        )
        book.save()

if __name__ == '__main__':
    populate_books()