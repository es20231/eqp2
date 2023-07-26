from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from dashboard.models import Profile

@receiver(post_save, sender=User) # The receiver decorator takes the signal and the sender as arguments
def create_profile(sender, instance, created, **kwargs): # The receiver function takes the arguments of the signal
    if created: # If the user is created
        Profile.objects.create(usuario=instance) # Create a profile object with the user instance

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()