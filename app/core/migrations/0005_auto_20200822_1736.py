# Generated by Django 3.0.9 on 2020-08-22 17:36

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200822_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='vol\\web\\media\\documents\\default_user.png', upload_to=core.utils.user_image_path),
        ),
    ]
