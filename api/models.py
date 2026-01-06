from django.db import models

# Create your models here.
class DailyRecord(models.Model):
    date = models.DateField(auto_now_add=True)
    point = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date}: {self.point}"