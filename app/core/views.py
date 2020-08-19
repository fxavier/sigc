from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, CreateView

from django.contrib.messages.views import SuccessMessageMixin

from core.forms import EmitenteForm, ChequeForm

from core.models import Banco, Emitente


class IndexView(ListView):
    template_name = 'index.html'
    queryset = Banco.objects.all()


class EmitenteCreateView(SuccessMessageMixin, CreateView):
    template_name = 'emitente_create.html'
    form_class = EmitenteForm
    success_url = '/'
    success_message = 'Emitente adicionado com sucesso!'

    def form_valid(self, form):
        emitente = form.save(commit=False)
        emitente.save()
        return redirect(self.success_url)


class EmitenteListView(ListView):
    template_name = 'emitente_list.html'
    queryset = Emitente.objects.all()

    


class ChequeCreateView(SuccessMessageMixin, CreateView):
    template_name = 'cheque_create.html'
    form_class = ChequeForm
    success_url = '/'
    success_message = 'Chque adicionado com sucesso'

    def form_valid(self, form):
        cheque = form.save(commit=False)
        cheque.estado_cheque = 'Devolvido'
        cheque.save()
        return redirect(self.success_url)
