from django.db import models

# Create your models here.

class Post (models.Model):
    text = models.TextField()
    title = models.CharField(max_length=500, blank=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    public = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    

class Tag (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    post = models.ManyToManyField(Post)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)