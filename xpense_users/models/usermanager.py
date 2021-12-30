from django.db import models


__all__ = ["UserManager"]


class UserManager(models.Manager):

    def create_user(self):
        return self.create()

    def create():
        pass