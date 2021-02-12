from django.db import models

from stdimage import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  active = models.BooleanField(default=True)

  class Meta:
    abstract = True


class Product(Base):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  stock = models.IntegerField()
  image = StdImageField(upload_to='products', variations={'thumb': (124, 124)})
  slug = models.SlugField(max_length=100, blank=True, editable=False)

  def __str__(self):
    return self.name

def product_pre_save(signal, instance, sender, **kwargs):
  instance.slug = slugify(instance.name)
signals.pre_save.connect(product_pre_save, sender=Product)

