from django.db import models
from datetime import datetime
# Create your models here.

class Sport(models.Model):
    sport_name = models.CharField(max_length=25,default='')

    def __str__(self) -> str:
        return self.sport_name
    
    class Meta:
        db_table = 'polls_Sport'