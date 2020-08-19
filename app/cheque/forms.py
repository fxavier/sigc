from django import forms
from django.utils.translation import ugettext as _

from core.models import Regularizacao


class RegularizacaoForm(forms.ModelForm):

    class Meta:
        model = Regularizacao
        fields =('forma', 'cheque', 'file',)

        widgets = {
            'forma': forms.Select(attrs={'class': 'form-control'}),
            'cheque': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }

        label = {
            'forma': _('Forma de Pagamento'),
            'cheque': _('Cheque'),
            'file': _('Documento'),

        }