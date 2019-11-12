# Generated by Django 2.2.6 on 2019-11-12 07:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('playthroughs', '0007_video_video_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.RenameField(
            model_name='playthroughs',
            old_name='game_reviewed',
            new_name='game_played',
        ),
        migrations.AddField(
            model_name='playthroughs',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playthroughs',
            name='video_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playthroughs',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
