# Generated by Django 2.2.6 on 2019-12-08 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20191207_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='current_occupied',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
