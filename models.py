from django.db import models

# Create your models here.

class Post (models.Model):
    text = models.TextField()
    title = models.CharField(max_length=500, blank=True)
    create_date = models.DateField()
    update_date = models.DateField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    

class Tag (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    post = models.ManyToManyField(Post)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)