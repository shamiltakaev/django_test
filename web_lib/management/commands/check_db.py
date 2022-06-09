from django.core.management.base import BaseCommand
from web_lib.models import Author, Book


class Command(BaseCommand):
    help = "Checking DB"
    
    def add_arguments(self, parser):
        parser.add_argument("book_ids", help="Book id", type=int, nargs="+")

    def handle(self, *args, **kwargs):
        book_ids = kwargs["book_ids"]
        
        for book_id in book_ids:
            try:
                Book.objects.get(pk=book_id)
                self.stdout.write(self.style.SUCCESS(f"Success {book_id} exist"))
            except Book.DoesNotExist as e:
                self.stdout.write(self.style.ERROR(e))