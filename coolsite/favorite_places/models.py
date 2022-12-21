from django.db import models
from django.urls import reverse


class Place(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    img = models.ImageField(upload_to='static/images/')
    date = models.DateField(auto_now_add=True)
    people = models.ForeignKey('People', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotel', kwargs={'slug':self.slug})


class People(models.Model):
    fst_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.fst_name

    def get_absolute_url(self):
        return reverse('people', kwargs={'people_slug':self.slug})
