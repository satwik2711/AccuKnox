from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyModel
import threading

@api_view(['POST'])
def create_model(request):
    name = request.data.get('name', '')
    instance = MyModel.objects.create(name=name)
    instance.refresh_from_db()
    return Response({"message": "Model created", "id": instance.id})

@api_view(['GET'])
def trigger_request_finished(request):
    current_thread = threading.current_thread().name
    print(f"View running in thread: {current_thread}")
    return Response({"message": "Request finished"})

@api_view(['POST'])
def create_model_with_related(request):
    name = request.data.get('name', '')
    instance = MyModel.objects.create(name=name)
    return Response({"message": "Model and related object created", "id": instance.id})