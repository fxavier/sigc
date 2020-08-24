from django.contrib import admin
from .models import Banco, MotivoDevolucao, Emitente, Assinante, Cheque, Regularizacao, User, Profile


class ChequeAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero_cheque']

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Banco)
admin.site.register(MotivoDevolucao)
admin.site.register(Emitente)
admin.site.register(Assinante)
admin.site.register(Cheque, ChequeAdmin)
admin.site.register(Regularizacao)

