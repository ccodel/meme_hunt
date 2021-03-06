# Generated by Django 3.0.5 on 2020-07-29 05:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subtitle', models.CharField(max_length=100, unique_for_date='start_date')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('image', models.ImageField(upload_to='memes/')),
                ('hint1', models.CharField(max_length=100)),
                ('hint2', models.CharField(max_length=100)),
                ('hint3', models.CharField(max_length=100)),
                ('hint4', models.CharField(max_length=100)),
                ('hint5', models.CharField(max_length=100)),
                ('hint6', models.CharField(max_length=100)),
                ('hint7', models.CharField(max_length=100)),
            ],
        ),
    ]
