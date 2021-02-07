from django.db import models
from django.utils.text import slugify

# Create your models here.


class Bikes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='bikes/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Bikes, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'bike'
        verbose_name_plural = 'bikes'

    def __str__(self):
        return self.name

