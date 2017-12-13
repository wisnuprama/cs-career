from django.db import models
from core.utils import generate_token


# Create your models here.

class PublicAccess(models.Model):
    token = models.CharField("Token", default=generate_token(), unique=True, max_length=64)
    email = models.EmailField("Email", unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.email
