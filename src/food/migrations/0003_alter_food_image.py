# Generated by Django 4.2.5 on 2023-09-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_foodcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='media/food_images'),
        ),
    ]
