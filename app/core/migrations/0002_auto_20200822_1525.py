# Generated by Django 3.0.9 on 2020-08-22 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regularizacao',
            options={'verbose_name_plural': 'Regularizacoes'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nome',
        ),
    ]
