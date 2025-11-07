from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Zgloszenie
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=Zgloszenie)
def zwieksz_liczbe_graczy(sender, instance, created, **kwargs):
    if created:
        turniej = instance.turniej
        turniej.aktualna_liczba += 1
        turniej.save()

@receiver(post_delete, sender=Zgloszenie)
def zmniejsz_liczbe_graczy(sender, instance, **kwargs):
    turniej = instance.turniej
    if turniej.aktualna_liczba > 0:
        turniej.aktualna_liczba -= 1
        turniej.save()
