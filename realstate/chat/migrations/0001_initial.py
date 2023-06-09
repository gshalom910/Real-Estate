# Generated by Django 4.1.2 on 2022-10-23 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('from_u', models.ForeignKey(blank=True, db_column='from_user', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_id', to=settings.AUTH_USER_MODEL)),
                ('to_u', models.ForeignKey(blank=True, db_column='to_user', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
