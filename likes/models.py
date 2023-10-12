from django.db import models

# Create your models here.

class Likes(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    flower = models.ForeignKey('flowers.Flower', on_delete=models.CASCADE, null=True, related_name='likes_received')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.flower.name}"