# Generated by Django 4.1.2 on 2022-10-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_home_image_home_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='images',
            field=models.FileField(upload_to=''),
        ),
    ]