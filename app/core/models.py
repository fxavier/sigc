from django.db import models
from django.db.models import Q
from django.urls import reverse

ESTADO_CHEQUE = (
    ('Devolvido', 'Devolvido'),
    ('Cancelado', 'Cancelado'),
    ('Regularizado', 'Regularizado')
)

TIPO_EMITENTE = (
    ('Empresa', 'Empresa'),
    ('Singular', 'Singular')
)

class EmitenteManagerQuerySet(models.query.QuerySet):
    def singular(self):
        return self.filter(tipo_emitente="Singular")

    def empresa(self):
        return self.filter(tipo_emitente="Empresa")

class EmpresaManagerQuerySet(models.query.QuerySet):
    def by_assinantes(self, assinante):
        return self.filter(assinante=assinante)

class Banco(models.Model):
    nome = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.nome


class MotivoDevolucao(models.Model):
    codigo = models.IntegerField(default=11, unique=True)
    descricao = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.descricao

class EmitenteManager(models.Manager):
    def get_queryset(self):
        return EmitenteManagerQuerySet(self.model, using=self._db)

    def create_or_get(self, numero_conta):
        created = False
        qs = self.get_queryset().filter(numero_conta=numero_conta)
        if qs.count() == 1:
            emitente_obj = qs.first()
        else:
            emitente_obj = self.model.create(numero_conta=numero_conta)
            created = True
        return emitente_obj, created


        
            
class Emitente(models.Model):
    nome = models.CharField(max_length=255)
    numero_conta = models.CharField(max_length=100, unique=True)
    telefone_1 = models.CharField(max_length=50, unique=True)
    telefone_2 = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)
    tipo_emitente = models.CharField(max_length=10, choices=TIPO_EMITENTE)

    objects = EmitenteManager()


    def __str__(self):
        return self.nome


class AssinanteManager(models.Manager):
    def create(self):
        return self.model.objects.create()


class Assinante(models.Model):
    nome = models.CharField(max_length=255)
    numero_conta = models.CharField(max_length=100, unique=True)
    telefone_1 = models.CharField(max_length=50, unique=True)
    telefone_2 = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)

    objects = AssinanteManager()

    def __str__(self):
        return self.nome


class EmpresaManager(models.Manager):
    def get_queryset(self):
        return EmpresaManagerQuerySet(self.model, using=self._db)

    def create_or_get(self,emitente=None, assinante=None):
        created = False
        qs = self.get_queryset().filter(emitente=emitente, assinante=assinante)
        if qs.exists() and qs.count() == 1:
            empresa_obj = qs.first()
        else:
            empresa_obj = self.model.create(emitente=emitente, assinante=assinante)
            created = True
        return empresa_obj, created
        

class Empresa(models.Model):
    emitente = models.ForeignKey(Emitente, on_delete=models.CASCADE)
    assinante = models.ForeignKey(Assinante, on_delete=models.CASCADE)

    objects = EmpresaManager()

    def __str__(self):
        return self.emitente


class ChequeDevolvidoManagerQuerySet(models.query.QuerySet):
    def by_numero(self):
        return self.filter(numero=numero)

    def by_numero_conta(self):
        return self.filter(numero_conta=numero_conta)


class ChequeDevolvidoManager(models.Manager):
    def get_queryset(self):
        return ChequeDevolvidoManagerQuerySet(self.model, using=self._db)

    def create_or_get(self, emitente, numero):
        created = False
        qs = self.get_queryset().filter(emitente=emitente, numero=numero)
        if qs.exists() and qs.count() == 1:
            cheque_obj = qs.first()
        else:
            cheque_obj = self.model.create(emitente=emitente, numero=numero)
            created = True
        return cheque_obj, created


class ChequeDevolvido(models.Model):
    numero = models.CharField(max_length=100, unique=True)
    numero_conta = models.CharField(max_length=100, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_devolucao = models.DateTimeField(auto_now_add=True)
    dias_nao_regularizado = models.IntegerField(default=0)
    codigo_balcao = models.CharField(max_length=100, unique=True)
    emitente = models.ForeignKey(Emitente, on_delete=models.CASCADE)
    banco = models.OneToOneField(Banco, on_delete=models.CASCADE)
    estado_cheque = models.CharField(max_length=50, choices=ESTADO_CHEQUE)
    motivo_devolucao = models.ForeignKey(MotivoDevolucao, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero







