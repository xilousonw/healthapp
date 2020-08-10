from django.db import models

# Create your models here.

from healthapp.utils.models import BaseModel


class goods(BaseModel):
    name = models.CharField(max_length=32)
