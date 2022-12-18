from django.db import models
from django.urls import reverse


class Place(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField()
    date = models.DateField(auto_now_add=True)
    people = models.ForeignKey('People', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotel', kwargs={'hotel_id':self.pk})


class People(models.Model):
    fst_name = models.CharField(max_length=100)

    def __str__(self):
        return self.fst_name
