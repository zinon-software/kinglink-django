# Generated by Django 3.2.4 on 2021-12-10 20:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
    ]
