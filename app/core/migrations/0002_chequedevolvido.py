# Generated by Django 3.0.8 on 2020-07-22 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChequeDevolvido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100, unique=True)),
                ('numero_conta', models.CharField(max_length=100, unique=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_devolucao', models.DateTimeField(auto_now_add=True)),
                ('dias_nao_regularizado', models.IntegerField(default=0)),
                ('codigo_balcao', models.CharField(max_length=100, unique=True)),
                ('estado_cheque', models.CharField(choices=[('Devolvido', 'Devolvido'), ('Cancelado', 'Cancelado'), ('Regularizado', 'Regularizado')], max_length=50)),
                ('banco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Banco')),
                ('emitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Emitente')),
                ('motivo_devolucao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MotivoDevolucao')),
            ],
        ),
    ]