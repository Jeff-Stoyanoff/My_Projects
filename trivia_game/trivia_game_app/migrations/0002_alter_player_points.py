# Generated by Django 4.2.2 on 2023-10-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_game_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
