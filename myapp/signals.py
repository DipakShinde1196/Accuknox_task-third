from django.dispatch import Signal, receiver
from django.db import transaction
from myapp.models import MyModel

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    MyModel.objects.create(name="Signal Entry")
    print("Database entry created by signal")
