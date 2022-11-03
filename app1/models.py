from django.db import models
from datetime import datetime

# Create your models here.
class post(models.Model):
    name = models.CharField(max_length = 100)
    text = models.TextField(max_length = 100000)
    date = models.DateTimeField(default = datetime.now)
    
    def __str__(self):
        return self.name