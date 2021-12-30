from django.db import models
from .usermanager import UserManager


# Create your models here.

class UserModel(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    firstname = models.TextField(null=True)
    lastname = models.TextField(null=True)
    username = models.TextField(unique=True)
    phone = models.IntegerField(unique=True)
    email = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        abstract = True

class User(UserModel):

    class Meta:
        abstract = False
        db_table = "Users"