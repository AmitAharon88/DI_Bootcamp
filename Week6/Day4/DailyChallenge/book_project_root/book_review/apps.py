from django.apps import AppConfig

class BookReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_review'

    def ready(self):
        try:
            import book_review.signals
        except ImportError:
            pass