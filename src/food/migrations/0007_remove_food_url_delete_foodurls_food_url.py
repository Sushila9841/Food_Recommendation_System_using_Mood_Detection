# Generated by Django 4.2.5 on 2023-09-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_foodurls_remove_food_url_food_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='url',
        ),
        migrations.DeleteModel(
            name='FoodURLS',
        ),
        migrations.AddField(
            model_name='food',
            name='url',
            field=models.CharField(default='/', max_length=200),
            preserve_default=False,
        ),
    ]