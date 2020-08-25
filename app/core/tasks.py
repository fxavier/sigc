from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.core.mail import send_mail
from core.models import *
from datetime import datetime, timezone



@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def send_report():
    total = Banco.objects.all().count()
    send_mail(
        'Relatrio Celery',
        'Relatorio Geral de Bancos %f' % total,
        'xavier.f@fincode.co.mz',
        ['xavierfrancisco353@gmail.com'],
        fail_silently=False,

    )

    return total


@shared_task
def update_dias():
    cheque_obj = Cheque.objects.all()
    for cheque in cheque_obj:
        cheque.dias = (datetime.now(timezone.utc) - cheque.data_devolucao).days
        cheque.save()
    return 'Dias actualizadas com sucesso'

@shared_task
def update_status_cheque():
    cheque_obj = Cheque.objects.all()
    for cheque in cheque_obj:
        if cheque.dias > 5 and cheque.estado_cheque == 'Devolvido':
            cheque.estado_cheque = 'Cancelado'
            cheque.save()
    return 'Status actualizado com sucesso'

@shared_task
def bloqueio_conta():
    cheque_obj = Cheque.objects.all()
    for cheque in cheque_obj:
        if cheque.estado_cheque == 'Cancelado'and cheque.dias > 10:
            cheque.emitente.bloqueio_utr = True
            cheque.save()

    return 'Conta bloqueada no BM'

@shared_task
def notification_email():
    send_mail(
    'That’s your subject',
    'That’s your message body',
    'xavier.f@fincode.co.mz',
    ['xavierfrancisco353@gmail.com'],
    fail_silently=False,
)
            




