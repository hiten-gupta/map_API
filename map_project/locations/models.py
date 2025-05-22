from django.db import models
class Location(models.Model):
    CATEGORY_CHOICES = [
        ('Monument', 'Monument'),
        ('University', 'University'),
        ('Restaurant', 'Restaurant'),
        ('Park', 'Park'),
        ('Other', 'Other'),
    ]
     
    name = models.CharField(max_length = 100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
