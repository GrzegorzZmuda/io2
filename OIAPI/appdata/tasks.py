from celery import task
from celery import shared_task
# We can have either registered task

     # Magic happens here ...
# or
@shared_task
def send_notifiction():
     print("‘Here I\’m")
     # Another trick

