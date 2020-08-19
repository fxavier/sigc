from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, CreateView

from django.contrib.messages.views import SuccessMessageMixin

from cheque.forms import RegularizacaoForm


class RegularizacaoCreateView(CreateView):
    template_name = 'regularizacao_create.html'
    form_class = RegularizacaoForm
    success_url = '/'
    success_message = 'Cheque regularizado com sucesso!'

    def form_valid(self, form):
        regularizacao = form.save(commit=False)
        regularizacao.save()
        return redirect(self.success_url)
