from django import forms
from django.utils.translation import ugettext as _

from core.models import Emitente, Cheque

class EmitenteForm(forms.ModelForm):
    class Meta:
        model = Emitente
        fields = ( 'nome', 'numero_conta', 'telefone_1', 'telefone_2', 'email', 'endereco', 'tipo', 'assinante',)
        
        label = {
            'nome': _('Nome'),           
            'numero_conta': _('Numero da Conta'),
            'telefone_1': _('Telefone Principal'),
            'telefone_2': _('Telefone Secundario'),
            'email': _('Email'),
            'endereco': _('Endereco'),
            'tipo': _('Tipo Emitente'),
            'assinante': _('Assinante'),
        }


class ChequeForm(forms.ModelForm):

    class Meta:
        model = Cheque
        fields = ('motivo_devolucao', 'numero_cheque', 'banco', 'emitente', 'numero_conta',
                  'valor_cheque', 'data_devolucao', 'codigo_balcao')

        # widgets = {
        #     'motivo_devolucao': forms.Select(attrs={'class': 'form-control'}),
        #     'numero_cheque': forms.TextInput(attrs={'class': 'form-control'}),
        #     'banco': forms.Select(attrs={'class': 'form-control'}),
        #     'emitente': forms.Select(attrs={'class': 'form-control'}),
        #     'numero_conta': forms.TextInput(attrs={'class': 'form-control'}),
        #     'valor_cheque': forms.TextInput(attrs={'class': 'form-control'}),
        #     'data_devolucao': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        #     'codigo_balcao': forms.TextInput(attrs={'class': 'form-control'})
        # }

        label = {
            'motivo_devolucao': _('Motivo Devolucao'),
            'numero_cheque': _('Numero Cheque'),
            'emitente': _('Emitente'),
            'banco': _('Banco'),
            'numero_conta': _('Numero Conta'),
            'valor_cheque': _('Valor Cheque'),
            'data_devolucao': _('Data Devolucao'),
            'codigo_balcao': _('Codigo Balcao'),
            'estado_cheque': _('Estado Cheque')
        }