# Generated by Django 4.0.5 on 2022-06-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_stickers_username_stickers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickers',
            name='image',
            field=models.ImageField(upload_to='static/shop/stickers_image'),
        ),
    ]
