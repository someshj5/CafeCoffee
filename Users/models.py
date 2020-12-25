from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class User_role (models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.IntegerField(null=True)

    # Metadata
    class Meta:
        db_table = 'user_role'

    def __str__(self):
        return str(self.user_id.username)
