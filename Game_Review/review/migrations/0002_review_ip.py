# Generated by Django 2.2.6 on 2019-12-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ip',
            field=models.TextField(default='127.0.0.1'),
            preserve_default=False,
        ),
    ]