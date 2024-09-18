from django.urls import path
from .views import trigger_signal_Q1, trigger_signal_Q2, trigger_signal_with_transaction

urlpatterns = [
    path('trigger-signal/', trigger_signal_Q1, name='trigger_signal'),
    path('trigger-signal-thread/', trigger_signal_Q2, name='trigger_signal_thread'),
    path('trigger-signal-transaction/', trigger_signal_with_transaction, name='trigger_signal_with_transaction'),
]
