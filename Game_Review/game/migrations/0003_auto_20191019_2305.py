# Generated by Django 2.2.6 on 2019-10-19 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20191019_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image_path',
            field=models.ImageField(upload_to='reviews/static/game_images/'),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.TextField(max_length=120),
        ),
    ]