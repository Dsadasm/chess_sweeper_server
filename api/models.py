from django.db import models

# Create your models here.
class DailyRecord(models.Model):
    created_at = models.DateField(auto_now_add=True)
    points = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.created_at}: {self.points}"