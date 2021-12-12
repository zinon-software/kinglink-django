# Generated by Django 3.2.4 on 2021-12-11 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_avatar'),
        ('group', '0003_alter_group_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user', to='account.profile'),
        ),
        migrations.AlterField(
            model_name='group',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='account.Profile'),
        ),
    ]