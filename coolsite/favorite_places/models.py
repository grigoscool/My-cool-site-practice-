from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name





