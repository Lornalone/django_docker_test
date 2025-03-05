from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Nom de la catégorie", max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

class Tag(models.Model):
    name = models.CharField(verbose_name="Nom du tag", max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Product(models.Model):
    name = models.CharField(verbose_name="Nom du produit", max_length=255)
    quantity = models.PositiveIntegerField(blank=True)
    price = models.FloatField(verbose_name="Prix du produit")
    image = models.ImageField(upload_to="images/product", max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
