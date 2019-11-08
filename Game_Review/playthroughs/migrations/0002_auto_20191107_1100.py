# Generated by Django 2.2.6 on 2019-11-07 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playthroughs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playthrough_comment',
            name='gameName',
            field=models.CharField(default='anonymous', max_length=50),
        ),
        migrations.AlterField(
            model_name='playthrough_comment',
            name='on_playthrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playthroughs.Playthroughs'),
        ),
    ]
