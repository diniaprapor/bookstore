from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=256)
    cover = models.CharField(max_length=128)
    #models.ImageField(upload_to='book_covers')
    author = models.CharField(max_length=128)
    category = models.ForeignKey(Category)
    price = models.FloatField()
    #owner
    #isbn
    def __unicode__(self):
        return self.name
