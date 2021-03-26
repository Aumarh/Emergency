from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class UserInfo(models.Model):
    user_id = models.CharField(max_length=20, blank=True, primary_key=True)
    nickname = models.CharField(max_length=20, unique=True)
    firstcontact_name = models.CharField(max_length=20)
    firstcontact_number = PhoneNumberField(blank=False)
    secondcontact_name = models.CharField(max_length=20)
    secondcontact_number = PhoneNumberField(blank=False)

    def __str__(self):
        return self.nickname