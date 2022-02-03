from django.db import models


# Create your models here.
class Book(models.Model):
    # Field.null ↓
    # If True, Django will store empty values as NULL in the database. Default is False.

    # Field.blank ↓
    # If True, the field is allowed to be blank. Default is False.

    # Field.unique ↓
    # If True, this field must be unique throughout the table.

    # Field.choices ↓
    # A sequence consisting itself of iterables of exactly two items (e.g. [(A, B), (A, B) ...])
    # BOOKS = (
    #     ('HB', 'Hobbit', 'Tora')
    # )
    # title = models.CharField(blanc=False, unique=True, default='Tora', choices=BOOKS)
    # Strings ↓
    title = models.CharField(blank=False, unique=True, max_length=36)
    description = models.TextField(max_length=256, blank=True)

    # Numbers ↓
    # IntegerField, BigIntegerField, DecimalField, FloatField
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)

    # Date ↓
    # DateField, TimeField, DateTimeField
    published = models.DateField(blank=True, null=True,default=None)

    # Uploading ↓
    # FileField, ImageField
    cover = models.ImageField(upload_to='covers/', blank=True)

