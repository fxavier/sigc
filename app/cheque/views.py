from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, CreateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from cheque.forms import RegularizacaoForm

from core.models import Cheque



@method_decorator(login_required(login_url='account:login'), name='dispatch')
class RegularizacaoCreateView(CreateView):
    template_name = 'regularizacao_create.html'
    form_class = RegularizacaoForm
    queryset = Cheque.objects.exclude(estado_cheque__icontains='Regularizado')
    success_url = '/'
    success_message = 'Cheque regularizado com sucesso!'

    def form_valid(self, form):
        regularizacao = form.save(commit=False)
        regularizacao.save()
        return redirect(self.success_url)
