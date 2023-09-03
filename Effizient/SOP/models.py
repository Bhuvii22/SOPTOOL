# Create your models here.
# models.py
from django.db import models

class SOPDocument(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()
    email = models.EmailField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    highest_education = models.CharField(
        max_length=50,
        choices=[
            ('high_school', 'High School'),
            ('undergraduate', 'Undergraduate'),
            ('graduate', 'Graduate'),
            ('postgraduate', 'Postgraduate'),
        ]
    )
    institute = models.CharField(max_length=100)
  

    def __str__(self):
        return self.title
