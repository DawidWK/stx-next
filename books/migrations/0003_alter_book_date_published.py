# Generated by Django 3.2.9 on 2021-11-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.PositiveIntegerField(),
        ),
    ]
