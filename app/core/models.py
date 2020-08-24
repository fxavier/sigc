from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse
from django.db.models.signals import pre_save, post_save

from PIL import Image

from core.utils import regularizacao_file_path, user_image_path


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
    bloqueio_utr = models.BooleanField(default=False)

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
    bloqueio_utr = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('core:emitente')


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

    class Meta:
        verbose_name_plural = 'Regularizacoes'

def update_estado_cheque(sender, instance, created, *args, **kwargs):
    if created:
        cheque = Cheque.objects.get(regularizacao=instance)
        cheque.estado_cheque = 'Regularizado'
        cheque.save()
       

post_save.connect(update_estado_cheque, sender=Regularizacao)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    image = models.ImageField(upload_to=user_image_path, default="uploads/documentos/default_user.png")
   
    def __str__(self):
        return self.user.email

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


    def save(self, *args,**kwargs):
        super(Profile, self).save(*args,**kwargs)
        img = Image.open(self.image)
        if img.height > 200 or img.width > 200 :
            new_size = (200,200)
            img.thumbnail(new_size)
            img.save(self.image.path)

def post_save_user_signal(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()

post_save.connect(post_save_user_signal, sender=User)