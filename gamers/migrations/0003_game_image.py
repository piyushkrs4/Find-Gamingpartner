# Generated by Django 3.1.2 on 2021-01-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(default=0, upload_to='static'),
        ),
    ]
