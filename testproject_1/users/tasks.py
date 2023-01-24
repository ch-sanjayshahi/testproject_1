import datetime as dt
from celery import shared_task


@shared_task
def initial():
    print(f"hello from initial. {dt.datetime.now()}")
    
@shared_task
def say_hello():
    print(f"hello {dt.datetime.now()}")
