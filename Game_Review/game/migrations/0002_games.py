# Generated by Django 2.2.6 on 2019-10-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.IntegerField(default=0)),
                ('picname', models.CharField(default='non', max_length=50)),
            ],
        ),
    ]
