from django.shortcuts import render

# views.py
from django.db import transaction
from django.http import HttpResponse
from .signals import my_signal
from myapp.models import MyModel

def trigger_signal(request):
    try:
        with transaction.atomic():
            # Send the signal inside a transaction
            my_signal.send(sender=None)

            # Rollback transaction manually to simulate a failure
            raise Exception("Simulating transaction failure")

    except Exception as e:
        print("Transaction rolled back due to an error")

    # Check if the database entry created by the signal exists
    signal_entry_exists = MyModel.objects.filter(name="Signal Entry").exists()

    return HttpResponse(f"Signal entry exists after rollback: {signal_entry_exists}")


