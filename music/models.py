from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Song(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    file = models.FileField()
    user = models.CharField(max_length=250)

    def __str__(self):
        return self.title
