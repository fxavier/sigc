from django.db import models

ESTADO_CHEQUE = (
    ('Devolvido', 'Devolvido'),
    ('Cancelado', 'Cancelado'),
    ('Regularizado', 'Regularizado')
)

TIPO_EMITENTE = (
    ('Empresa', 'Empresa'),
    ('Singular', 'Singular')
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


class Emitente(models.Model):
    nome = models.CharField(max_length=255)
    numero_conta = models.CharField(max_length=100, unique=True)
    telefone_1 = models.CharField(max_length=50, unique=True)
    telefone_2 = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)
    tipo_cliente = models.CharField(max_length=10, choices=TIPO_EMITENTE)


    def __str__(self):
        return self.nome

class Assinante(models.Model):
    nome = models.CharField(max_length=255)
    numero_conta = models.CharField(max_length=100, unique=True)
    telefone_1 = models.CharField(max_length=50, unique=True)
    telefone_2 = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    emitente = models.ForeignKey(Emitente, on_delete=models.CASCADE)
    assinante = models.ForeignKey(Assinante, on_delete=models.CASCADE)

    def __str__(self):
        return self.emitente.nome






