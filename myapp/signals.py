# signals.py
from django.dispatch import Signal, receiver
from django.db import transaction
from myapp.models import MyModel

# Define a custom signal
my_signal = Signal()

# Define a receiver function that modifies the database
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    MyModel.objects.create(name="Signal Entry")
    print("Database entry created by signal")
