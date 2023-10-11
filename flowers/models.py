from django.db import models

# Create your models here.

class Flower(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    care_instructions = models.TextField()
    blooming_season = models.CharField(max_length=255)
    origin = models.CharField(max_length=255, blank=True, null=True)
    warning_signs = models.TextField(blank=True, null=True)
    health_indicators = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="flowers/", blank=True, null=True)
    likes = models.ManyToManyField(
        'users.User',
        related_name='liked_flower',
        blank=True
    )

    def __str__(self):
        return self.name