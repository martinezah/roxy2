from django.db import models

class Artifact(models.Model):
    key = models.CharField(max_length=160,primary_key=True)
    data = models.BinaryField()
