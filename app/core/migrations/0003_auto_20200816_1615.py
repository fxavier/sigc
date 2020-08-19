# Generated by Django 3.0.8 on 2020-08-16 16:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200816_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='cheque',
            name='banco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Banco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cheque',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cheque',
            name='dias',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Regularizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(choices=[('Cheque', 'Cheque'), ('Numerario', 'Numerario')], max_length=10)),
                ('cheque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cheque')),
                ('documento', models.ManyToManyField(to='core.Documento')),
            ],
        ),
    ]