# Generated by Django 4.1.2 on 2022-10-24 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_home_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.home')),
            ],
        ),
    ]
