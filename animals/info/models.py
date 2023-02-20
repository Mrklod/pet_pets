from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.category

class Animal(models.Model):
    name = models.CharField(max_length=150)
    age = models.SmallIntegerField()
    text = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=160)

    def __str__(self):
        return self.name