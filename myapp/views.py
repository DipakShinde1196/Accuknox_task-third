from django.shortcuts import render

from django.db import transaction
from django.http import HttpResponse
from .signals import my_signal
from myapp.models import MyModel

def trigger_signal(request):
    try:
        with transaction.atomic():
            my_signal.send(sender=None)
            raise Exception("Simulating transaction failure")

    except Exception as e:
        print("Transaction rolled back due to an error")
    signal_entry_exists = MyModel.objects.filter(name="Signal Entry").exists()
    return HttpResponse(f"Signal entry exists after rollback: {signal_entry_exists}")


