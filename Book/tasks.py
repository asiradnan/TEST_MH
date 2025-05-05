from datetime import timedelta
from celery import shared_task
from Book.models import Book
from django.utils import timezone  

from celery import Celery
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, check_for_archieve(), name='add every 10')



@app.task
def check_for_archieve():
    books = Book.objects.all()
    for book in books:
        if (timezone.now()- book.publish_year < timedelta(days=365 * 10)):
            book.archived = True
            book.save()
