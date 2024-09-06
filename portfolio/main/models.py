from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneno = models.CharField(max_length=30)
    emailsub = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.title

    