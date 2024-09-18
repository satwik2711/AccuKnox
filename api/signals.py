from django.dispatch import Signal, receiver
import time, threading
from .models import LogEntry


task_completed = Signal()

@receiver(task_completed)
def heavy_processing(sender, **kwargs):
    print("Signal receiver started.")
    start_time = time.time()
    time.sleep(5)
    end_time = time.time()
    print("Signal receiver finished.")
    print(f"Signal receiver execution time: {end_time - start_time:.2f} seconds")

@receiver(task_completed)
def print_thread_info(sender, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal receiver running in thread: {current_thread.name} (ID: {current_thread.ident})")

@receiver(task_completed)
def create_log_entry(sender, **kwargs):
    print("Signal receiver started.")
    LogEntry.objects.create(message="Log entry from signal receiver.")
    print("Signal receiver finished.")
