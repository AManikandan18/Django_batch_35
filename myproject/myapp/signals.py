from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student_Signals

@receiver(post_save, sender= Student_Signals)
def Student_created(sender ,instance ,created ,**kwargs):
    if created:
        print(f'Student Created : {instance.name}')