from django.contrib import admin

from . models import Assinante, Emitente, MotivoDevolucao, Empresa, ChequeDevolvido, Banco



admin.site.register(Empresa)
admin.site.register(Banco)
admin.site.register(Assinante)
admin.site.register(MotivoDevolucao)
admin.site.register(ChequeDevolvido)
admin.site.register(Emitente)