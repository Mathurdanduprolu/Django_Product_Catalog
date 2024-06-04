from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='categories/', default="")  # New image field

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=50)
    additional_details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image1.delete()
        self.image2.delete()
        self.image3.delete()
        if self.image4:
            self.image4.delete()
        super().delete(*args, **kwargs)
