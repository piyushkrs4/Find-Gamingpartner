# Generated by Django 3.1.2 on 2021-01-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0008_auto_20210117_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matchpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('gameid', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('option', models.IntegerField(default=0)),
            ],
        ),
    ]
