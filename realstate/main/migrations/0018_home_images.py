# Generated by Django 4.1.2 on 2022-10-20 19:15


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_home_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='images',
            field=models.ImageField(default='images/p1.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
