# Generated by Django 4.0.5 on 2022-06-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_stickers_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickers',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]