# Generated by Django 4.1.2 on 2022-10-19 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_home_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='ptype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.propertytype'),
        ),
        migrations.AlterField(
            model_name='home',
            name='status',
            field=models.CharField(choices=[('Sale', 'sale'), ('Rent', 'rent')], max_length=40),
        ),
        migrations.AlterField(
            model_name='propertytype',
            name='types',
            field=models.CharField(max_length=40),
        ),
    ]
