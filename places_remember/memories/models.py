from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=250, null=False)
    title = models.CharField(max_length=80, null=False)
    description = models.TextField(max_length=1000, null=False)

    def __str__(self) -> str:
        return (f"User: {self.user.first_name} {self.user.last_name}, "
                f"Location: {self.location}, Title: {self.title}, "
                f"Description: {self.description}")
