from django.db import models

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    video_type = models.CharField(max_length=50)
    num_people = models.IntegerField()
    delivery_method = models.CharField(max_length=50)
    gmail = models.CharField(max_length=120, blank=True, null=True)
    people_data = models.TextField(blank=True, null=True)
    image_paths = models.TextField(blank=True, null=True)