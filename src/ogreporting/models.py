from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.TextField()
    description = models.TextField()
    severity = models.TextField()
    reporter = models.TextField(default="Oil & Gas Employee")

