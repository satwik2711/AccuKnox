from django.urls import path
from . import views

urlpatterns = [
    path('create_model/', views.create_model, name='create_model'),
    path('trigger_request_finished/', views.trigger_request_finished, name='trigger_request_finished'),
    path('create_model_with_related/', views.create_model_with_related, name='create_model_with_related'),
]