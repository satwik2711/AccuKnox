from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from .models import LogEntry
from .signals import task_completed
import time, threading

@api_view(['GET'])
def trigger_signal_Q1(request):
    print("View started.")
    start_time = time.time()
    task_completed.send(sender=None)
    end_time = time.time()
    print("View finished.")
    total_time = end_time - start_time
    print(f"Total view execution time: {total_time:.2f} seconds")
    return Response({
        "message": "Signal triggered.",
        "total_execution_time": f"{total_time:.2f} seconds"
    })

@api_view(['GET'])
def trigger_signal_Q2(request):
    current_thread = threading.current_thread()
    print(f"View started in thread: {current_thread.name} (ID: {current_thread.ident})")
    task_completed.send(sender=None)
    print("View finished.")
    return Response({"message": "Signal triggered in thread."})

@api_view(['GET'])
def trigger_signal_with_transaction(request):
    try:
        with transaction.atomic():
            print("View started.")
            LogEntry.objects.create(message="Log entry from view.")
            task_completed.send(sender=None)
            print("View finished.")
            raise Exception("Simulated exception for transaction rollback.")
    except Exception as e:
        print(f"Exception occurred: {e}")
    total_entries = LogEntry.objects.count()
    print(f"Total log entries after rollback: {total_entries}")
    return Response({
        "message": "Signal triggered with transaction.",
        "total_log_entries": total_entries
    })