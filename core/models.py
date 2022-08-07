from django.db import models

# Create your models here.
class Year(models.Model):
    month = models.CharField(max_length=9)
    url = models.CharField(max_length=120)

    def __str__(self):
        return self.month

class January(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class December(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class February(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class March(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class April(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class May(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class June(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class July(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title
class August(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class September(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class October(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class November(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    place = models.CharField(max_length=4)

    def __str__(self):
        return self.title