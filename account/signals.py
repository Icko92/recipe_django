from django.db.models.signals import post_save
from .models import Account
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kvargs):
    if(created):
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Account)
def save_profile(sender, instance, **kvargs):
    instance.profile.save()
