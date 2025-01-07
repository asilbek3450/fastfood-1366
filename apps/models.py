from django.db import models
from django.core.validators import RegexValidator

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

telefon_regex = RegexValidator(
                regex=r'^\+998\d{9}$',
                message="Telefon raqami '+998' bilan boshlanishi va 9 ta raqamdan iborat bo‘lishi kerak.",
)

class BookTable(models.Model):
    ism = models.CharField(max_length=255)
    telefon = models.CharField(max_length=13, validators=[telefon_regex])
    soni = models.IntegerField()
    sana = models.DateField()

    def __str__(self):
        return f"{self.ism} - {self.telefon} | - {self.soni} kishilik joy bron qildi"
    