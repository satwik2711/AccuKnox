from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.signals import request_finished
from .models import MyModel
import threading
import time

@receiver(post_save, sender=MyModel)
def my_synchronous_handler(sender, instance, created, **kwargs):
    if created:
        time.sleep(2)#processing
        print(f"Synchronous signal handler executed for {instance.name}")
        MyModel.objects.create(name=f"Related to {instance.name}", _signal_triggered=True)

@receiver(request_finished)
def my_request_finished_handler(sender, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal handler running in thread: {current_thread}")
    

@receiver(post_save, sender=MyModel)
def my_transactional_handler(sender, instance, created, **kwargs):
    # This will be in the same transaction as the save operation
    MyModel.objects.create(name=f"Related to {instance.name}")