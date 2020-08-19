from django.db import models
from django.db.models.signals import pre_save, post_save

from core.utils import regularizacao_file_path


ESTADO_CHEQUE = (
    ('Devolvido', 'Devolvido'),
    ('Cancelado', 'Cancelado'),
    ('Regularizado', 'Regularizado')
)

TIPO_EMITENTE = (
    ('P', 'Particular'), 
    ('E', 'Empresa')
)

FORMA_REGULARIZACAO = (
    ('Cheque', 'Cheque'),
    ('Numerario', 'Numerario')
)

class Banco(models.Model):
    nome = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.nome


class MotivoDevolucao(models.Model):
    codigo = models.IntegerField(default=11, unique=True)
    descricao = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Motivo de Devolucao'
        verbose_name_plural = 'Motivos de Devolucao'


class Assinante(models.Model):
    nome = models.CharField(max_length=255)
    numero_conta = models.CharField(max_length=100, unique=True)
    telefone_1 = models.CharField(max_length=50, unique=True)
    telefone_2 = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Emitente(models.Model):
    nome = models.CharField(max_length=255)
    numero_conta = models.CharField(max_length=100, unique=True)
    telefone_1 = models.CharField(max_length=50, unique=True)
    telefone_2 = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)
    tipo = models.CharField(max_length=1, choices=TIPO_EMITENTE)
    assinante = models.ManyToManyField(Assinante, blank=True)

    def __str__(self):
        return self.nome


class Cheque(models.Model):
    motivo_devolucao = models.ForeignKey(MotivoDevolucao, on_delete=models.CASCADE)
    numero_cheque = models.CharField(max_length=50, unique=True)
    emitente = models.ForeignKey(Emitente, on_delete=models.CASCADE)
    numero_conta = models.CharField(max_length=100, unique=True)
    valor_cheque = models.DecimalField(max_digits=10, decimal_places=2)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    codigo_balcao = models.CharField(max_length=100)
    estado_cheque = models.CharField(max_length=50, choices=ESTADO_CHEQUE, default='Devolvido')
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    dias = models.IntegerField(default=0)

    def __str__(self):
        return self.numero_cheque

class Regularizacao(models.Model):
    forma = models.CharField(max_length=10, choices=FORMA_REGULARIZACAO)
    cheque = models.ForeignKey(Cheque, on_delete=models.CASCADE)
    file = models.FileField(upload_to=regularizacao_file_path, null=True, blank=True)


    def __str__(self):
        return self.cheque.numero_cheque

# def update_estado_cheque(sender, instance, created, *args, **kwargs):
#     if created:
#         cheque = Cheque.objects.get(regularizacao=instance)
#         cheque.estado_cheque = 'Regularizado'
#         cheque.save()
       

# post_save.connect(update_estado_cheque, sender=Regularizacao)

