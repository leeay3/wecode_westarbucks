import datetime 

from django.db import models 
from django.utils import timezone 

class Menu(models.Model):
	menu_name = models.CharField(max_length=40)
    
	def __str__(self):
		return self.menu_name

class Categories(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    categorie_name = models.CharField(max_length=40)

    def __str__(self):
        return self.categorie_name

class Drinks (models.Model):
    drink_korean_name = models.CharField(max_length=45)
    drink_english_name = models.CharField(max_length=45)
    description = models.TextField()
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE)


    def __str__(self):
        return self.drink_korean_name

class Images(models.Model):
    image_url = models.URLField(max_length=2000)
    drink_img = models.ForeignKey('Drinks', on_delete=models.CASCADE)


    def __str__(self):
        return self.image_url

class Allergy(models.Model):
    allergy_name = models.CharField(max_length=45)
    name = models.ManyToManyField('Drinks', through="Allergy_drink")

    def __str__(self):
        return self.allergy_name

class Allergy_drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)

    # def __str__(self):
        # return 
    
class Nutritions(models.Model):
    kcal = models.DecimalField(max_digits = 10, decimal_places = 2)
    sodium = models.DecimalField(max_digits = 10, decimal_places = 2)
    fat = models.DecimalField(max_digits = 10, decimal_places = 2)
    sugar = models.DecimalField(max_digits = 10, decimal_places = 2)
    protein = models.DecimalField(max_digits = 10, decimal_places = 2)
    caffeine = models.DecimalField(max_digits = 10, decimal_places = 2)
    dirnk_nu = models.ForeignKey('Drinks', on_delete=models.CASCADE)

    # def __str__(self):
        # return 

class Sizes(models.Model):
    size_name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_ounce = models.CharField(max_length=45)
    nutrition = models.ForeignKey('Nutritions', on_delete=models.CASCADE)


    def __str__(self):
        return self.size_name