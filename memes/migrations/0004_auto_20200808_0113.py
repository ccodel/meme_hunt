# Generated by Django 3.1 on 2020-08-08 06:13

from django.db import migrations, models
import memes.models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0003_auto_20200804_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='end_date',
            field=models.DateField(unique=True, validators=[memes.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='meme',
            name='start_date',
            field=models.DateField(unique=True, validators=[memes.models.validate_date]),
        ),
    ]
