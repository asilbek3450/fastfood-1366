from django.db import models

# Create your models here.
class Category(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi
    

class Product(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.IntegerField()
    kategoriya = models.ForeignKey(Category, on_delete=models.CASCADE)
    rasmi = models.URLField()
    malumot = models.TextField()
    
    def __str__(self):
        return self.nomi
    