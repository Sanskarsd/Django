from django.db import models

# Create your models here.


class Review(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    review_text=models.TextField(max_length=500)
    ratings=models.IntegerField()


    def __str__(self):
        return self.username+" - "+str(self.ratings)
    