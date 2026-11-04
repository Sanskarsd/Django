from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify




class Country(models.Model):
    name = models.CharField(max_length=100)
    code=models.IntegerField(max_length=2)


    def __str__(self):
        return self.name


    
class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} - {self.zip_code}"
    





class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    

class Book(models.Model):

    title = models.CharField(max_length=200)

    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name="books")
    published_country = models.ManyToManyField(Country)
    is_bestselling = models.BooleanField(default=False)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.rating}"