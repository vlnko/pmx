from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return f"{self.first_name} {self.last_name} (@{self.username})"


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    users = models.ManyToManyField(CustomUser, verbose_name="Users")

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name
    