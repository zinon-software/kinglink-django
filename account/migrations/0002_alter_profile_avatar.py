# Generated by Django 3.2.4 on 2021-12-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.CharField(blank=True, default='https://cdn.icon-icons.com/icons2/1736/PNG/512/4043237-avatar-avocado-food-scream_113277.png', max_length=250, null=True),
        ),
    ]