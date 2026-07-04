from django.db import models

# Create your models here.
class Item (models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=500, blank=True)
    image = models.CharField(max_length=500,default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
    def __str__(self):
        return self.name

