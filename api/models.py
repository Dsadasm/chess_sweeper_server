from django.db import models

# Create your models here.
class DailyRecord(models.Model):
    created_at = models.DateField(auto_now_add=True)
    point = models.IntegerField()
    name = models.CharField(max_length=100)
    time = models.DurationField()

    def __str__(self):
        return f"{self.created_at}: {self.point}"