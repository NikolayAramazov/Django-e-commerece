from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    link = models.CharField(max_length=200, help_text="Enter a relative URL like /products/3/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
