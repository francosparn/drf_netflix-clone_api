# Generated by Django 4.2.5 on 2023-09-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
