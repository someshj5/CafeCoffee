# Create your models here.

from django.db import models


class Amenity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'amenity'

    def __str__(self):
        return str(self.name)


class coffee_store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.TextField()
    state = models.CharField(max_length=2)
    email = models.EmailField()
    amenities = models.ManyToManyField(Amenity, blank=True)

    class Meta:
        db_table = 'coffee_store'

    def __str__(self):
        return str(self.name)


class Menu(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    calories = models.IntegerField(null=True)
    price = models.FloatField(null=True)

    class Meta:
        db_table = 'item'

    def __str__(self):
        return str(self.name)


class Drink(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                primary_key=True)
    caffeine = models.IntegerField(null=True)

    class Meta:
        db_table = 'drink'

    def __str__(self):
        return str(self.item)


