# Generated by Django 3.1.2 on 2021-01-17 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0005_auto_20210116_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ign', models.CharField(max_length=122, unique=True)),
                ('igid', models.CharField(max_length=122, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamers.game')),
            ],
        ),
    ]
