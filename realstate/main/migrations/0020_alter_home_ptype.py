# Generated by Django 4.1.2 on 2022-10-21 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_propertytype_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='ptype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.propertytype'),
        ),
    ]