# Generated by Django 2.2.3 on 2020-06-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_storage', '0005_remove_image_rest_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]