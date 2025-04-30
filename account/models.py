from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    AbstractUser,
)

USER_TYPE_CHOICES = (
    ("Doctor", "Doctor"),
    ("Patient", "Patient"),
)

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        unique=True,
    )
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default="Patient",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)

@receiver(post_save, sender=CustomUser)
def create_username(sender, instance=None, created=False, **kwargs):
    if created:
        email = instance.email
        sliced_email = email.split("@")[0]
        instance.username = sliced_email
        instance.save()