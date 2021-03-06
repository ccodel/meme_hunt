# Generated by Django 3.0.5 on 2020-07-31 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='secret_key',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meme',
            name='end_date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='meme',
            name='start_date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='meme',
            name='subtitle',
            field=models.CharField(max_length=100),
        ),
    ]
