from django.db import models

# Create your models here.

class Review(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)  # user who commented on the flower
    flower = models.ForeignKey('flowers.Flower', on_delete=models.CASCADE, null=True)  # flower that is commented on
    text = models.TextField()  # text of the user's comment
    date_added = models.DateTimeField(auto_now_add=True)  # date when the comment was added

    def __str__(self):
        return f"{self.user.username} - {self.flower.name} - {self.text}"