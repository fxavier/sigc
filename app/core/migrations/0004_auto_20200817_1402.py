# Generated by Django 3.0.8 on 2020-08-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200816_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularizacao',
            name='documento',
        ),
        migrations.AddField(
            model_name='regularizacao',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
    ]
