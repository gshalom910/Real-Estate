# Generated by Django 4.1.2 on 2022-10-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_home_created_att_home_updated_att_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='created_att',
        ),
        migrations.RemoveField(
            model_name='home',
            name='updated_att',
        ),
        migrations.AlterField(
            model_name='home',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
