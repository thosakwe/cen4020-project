# Generated by Django 2.2.6 on 2019-12-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidebook',
            name='pdf_file',
            field=models.FileField(null=True, upload_to='guidebooks/', verbose_name=''),
        ),
    ]
