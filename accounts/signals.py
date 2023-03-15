from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User

@receiver(post_save, sender=User)
def assign_user_profile_and_group(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        user_group = Group.objects.get(name='User')
        instance.groups.add(user_group)


