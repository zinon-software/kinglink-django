# Generated by Django 3.2.4 on 2021-07-17 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whatsApp', '0005_category_report_sections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groub',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category_name', to='whatsApp.category'),
        ),
        migrations.AlterField(
            model_name='groub',
            name='sections',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sections_name', to='whatsApp.sections'),
        ),
    ]
