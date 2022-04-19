# Generated by Django 3.2.13 on 2022-04-18 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='inventory.product_category', verbose_name='categorias'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='region',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='región'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inventory.product_category', verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='measure_unit',
            field=models.PositiveSmallIntegerField(choices=[('KG', 'Kilo'), ('LT', 'litro')], default='KG', verbose_name='unidad de medida'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.SmallIntegerField(verbose_name='cantidad'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inventory.supplier', verbose_name='proveedor'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='inventory.warehouse', verbose_name='almacén'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=200, verbose_name='dirección'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact',
            field=models.CharField(max_length=200, verbose_name='contacto'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.CharField(max_length=50, verbose_name='correo electrónico'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone1',
            field=models.CharField(max_length=12, verbose_name='teléfono principal'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone2',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='teléfono secundario'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='description',
            field=models.CharField(max_length=255, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nombre'),
        ),
    ]
