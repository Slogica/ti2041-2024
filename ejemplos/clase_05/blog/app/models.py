from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    category = models.CharField(max_length=100, default="Principal")

    def __str__(self):
        return self.title + " (" + self.author + ")"