# Generated by Django 4.0.3 on 2023-11-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy_tennis_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField(default=True)),
                ('name', models.TextField(max_length=155)),
                ('budget', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]