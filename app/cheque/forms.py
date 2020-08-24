from django import forms
from django.utils.translation import ugettext as _

from core.models import Regularizacao, Cheque


class RegularizacaoForm(forms.ModelForm):
    class Meta:
        model = Regularizacao
        fields =('forma', 'file', 'cheque')

        label = {
            'forma': _('Forma de Pagamento'),
            'cheque': _('Cheque'),
            'file': _('Documento'),

        }