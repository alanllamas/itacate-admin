from django.db import models
from django.utils.translation import gettext as _

class Warehouse(models.Model):
  name = models.CharField('nombre', max_length=200)
  description = models.CharField('descripción', max_length=255)

  created = models.DateTimeField('creado', auto_now_add=True)
  modified = models.DateTimeField('modificado', auto_now=True)

  class Meta:
    verbose_name = "almacen"
    verbose_name_plural = "almacenes"

  def __str__(self):
    return self.name



class Product_Category(models.Model):
  name = models.CharField('nombre', max_length=200)
  warehouse = models.ForeignKey(
    Warehouse, related_name='categories', on_delete=models.CASCADE,
    verbose_name='almacén', null=False, blank=False)

  created = models.DateTimeField('creado', auto_now_add=True)
  modified = models.DateTimeField('modificado', auto_now=True)

  class Meta:
    verbose_name = "categoria de producto"
    verbose_name_plural = "categorias de productos"

  def __str__(self):
    return self.name

class Supplier(models.Model):

  name = models.CharField('nombre', max_length=200)
  contact = models.CharField('contacto', max_length=200)
  phone1 = models.CharField('teléfono principal', max_length=12)
  phone2 = models.CharField('teléfono secundario', max_length=12, null=True, blank=True)
  email = models.CharField('correo electrónico',max_length=50)
  address = models.CharField('dirección',max_length=200)
  categories = models.ForeignKey(
    Product_Category, related_name='suppliers', on_delete=models.CASCADE,
    verbose_name='categorias', null=True, blank=True)
  region = models.CharField('región', max_length=200, null=True, blank=True)

  created = models.DateTimeField('creado', auto_now_add=True)
  modified = models.DateTimeField('modificado', auto_now=True)

  class Meta:
    verbose_name = "proveedor"
    verbose_name_plural = "proveedores"

  def __str__(self):
    return self.name

class Product(models.Model):

  class Measure_Units(models.TextChoices):
    KILOGRAM = 'KG', _('Kilo')
    Liter = 'LT', _('litro')

  name = models.CharField('nombre', max_length=200)
  supplier = models.ForeignKey(
    Supplier, related_name='products', on_delete=models.CASCADE,
    verbose_name='proveedor', null=False, blank=False)
  quantity = models.SmallIntegerField('cantidad')
  measure_unit = models.PositiveSmallIntegerField('unidad de medida',choices=Measure_Units.choices, default=Measure_Units.KILOGRAM)
  category = models.ForeignKey(
    Product_Category, related_name='products', on_delete=models.CASCADE,
    verbose_name='categoria', null=True, blank=True)
  price = models.SmallIntegerField('precio', null=True, blank=True)
  created = models.DateTimeField('creado', auto_now_add=True)
  modified = models.DateTimeField('modificado', auto_now=True)  

  class Meta:
    verbose_name = "producto"
    verbose_name_plural = "productos"

  def __str__(self):
    return self.name


class Inventory(models.Model):

  created = models.DateTimeField('creado', auto_now_add=True)
  modified = models.DateTimeField('modificado', auto_now=True)

  class Meta:
    verbose_name = "inventario"
    verbose_name_plural = "inventarios"

  def __str__(self):
    return self.name