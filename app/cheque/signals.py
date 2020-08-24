# from django.db.models.signals import post_save
# from core.models import Regularizacao, Cheque

# from django.dispatch import receiver


# @receiver(post_save, sender=Regularizacao)
# def update_cheque_estado(sender, instance, created, *args, **kwargs):
#     if created:
#         cheque = Cheque.objects.get(regularizacao=instance)
#         cheque.estado_cheque = 'Regularizado'
#         cheque.save()


# @receiver(post_save, sender=Regularizacao)
# def save_cheque(sender, instance, *args, **kwargs):
#     instance.cheque.save()
