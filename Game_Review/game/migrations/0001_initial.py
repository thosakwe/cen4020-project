# Generated by Django 2.2.6 on 2019-10-19 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.TextField(default='ab', max_length=50)),
                ('title', models.TextField(default='non', max_length=50)),
                ('description', models.TextField()),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
    ]
