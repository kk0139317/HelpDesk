from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import random

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.verification_code:
            self.verification_code = get_random_string(length=32)
        super(UserProfile, self).save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username