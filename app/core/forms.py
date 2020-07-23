from core.models import Emitente, Empresa, Assinante, ChequeDevolvido
from django import forms



class InsertEmitenteForm(forms.ModelForm):

    class Meta:
        model = Emitente
        fields = [
              'nome',
              'numero_conta', 
              'telefone_1',
              'telefone_2',
              'email',
              'endereco',
              'tipo_emitente'
            ]