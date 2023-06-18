from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Image, Profile

@receiver(post_save, sender=Image)
def update_profile(sender, instance, created, **kwargs):
    if created:
        # Increase the count of uploaded images for the user's profile
        instance.upload_user.profile.num_images += 1
        instance.upload_user.profile.save()