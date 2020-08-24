from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone

from core.forms import EmitenteForm, ChequeForm

from core.models import Banco, Emitente, Cheque, Profile, User

from core.utils import render_to_pdf
from django.template.loader import get_template

from core.tasks import send_report, update_dias, update_status_cheque, bloqueio_conta

@method_decorator(login_required(login_url='account:login'), name='dispatch')
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'cheque_list'
    model = Cheque

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cheque_devolvido'] = Cheque.objects.all().count()
        context['cheque_cancelado'] = Cheque.objects.filter(estado_cheque='Cancelado').count()
        context['cheque_regularizado'] = Cheque.objects.filter(estado_cheque='Regularizado').count()

        return context

    def get_queryset(self):
        return Cheque.objects.all()




@method_decorator(login_required(login_url='account:login'), name='dispatch')
class EmitenteCreateView(SuccessMessageMixin, CreateView):
    template_name = 'emitente_create.html'
    form_class = EmitenteForm
    success_url = '/'
    success_message = 'Emitente adicionado com sucesso!'

    def form_valid(self, form):
        emitente = form.save(commit=False)
        emitente.save()
        return redirect(self.success_url)


@method_decorator(login_required(login_url='account:login'), name='dispatch')
class EmitenteListView(ListView):
    template_name = 'emitente_list.html'
    queryset = Emitente.objects.all()
    paginate_by = 5


@method_decorator(login_required(login_url='account:login'), name='dispatch')
class EmitenteUpdateView(UpdateView):
    model = Emitente
    fields = ['nome', 'numero_conta', 'telefone_1', 'telefone_2', 'email', 'endereco', 'tipo', 'assinante']


@method_decorator(login_required(login_url='account:login'), name='dispatch')
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



@method_decorator(login_required(login_url='account:login'), name='dispatch')
class TodosChequesListView(ListView):
    template_name = 'cheque_list.html'
    queryset = Cheque.objects.all()


@method_decorator(login_required(login_url='account:login'), name='dispatch')
class ChequeCanceladoListView(ListView):
    template_name = 'cheque_cancelado_list.html'
    queryset = Cheque.objects.filter(estado_cheque='Cancelado')



@method_decorator(login_required(login_url='account:login'), name='dispatch')
class ChequeRegularizadoListView(ListView):
    template_name = 'cheque_regularizado_list.html'
    queryset = Cheque.objects.filter(estado_cheque='Regularizado')

def celery(request):
    update_dias.delay()
    update_status_cheque.delay()
    bloqueio_conta.delay()
    return HttpResponse('Enviado com sucesso')


@method_decorator(login_required(login_url='account:login'), name='dispatch')

class GenerateEmitentePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('reports/emitente.html')
        queryset = Emitente.objects.all()
        context = {
            "queryset": queryset,
            "data": timezone.now()
        }
        html = template.render(context)
        pdf = render_to_pdf('reports/emitente.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Clientes_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


@method_decorator(login_required(login_url='account:login'), name='dispatch')
class GenerateChequePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('reports/cheque.html')
        queryset = Cheque.objects.all()
        context = {
            "queryset": queryset,
            "data": timezone.now()
        }
        html = template.render(context)
        pdf = render_to_pdf('reports/cheque.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Cheques_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


@method_decorator(login_required(login_url='account:login'), name='dispatch')
class GenerateChequeCanceladoPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('reports/cheque-cancelado.html')
        queryset = Cheque.objects.filter(estado_cheque='Cancelado')
        context = {
            "queryset": queryset,
            "data": timezone.now()
        }
        html = template.render(context)
        pdf = render_to_pdf('reports/cheque-cancelado.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Cheques_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


@method_decorator(login_required(login_url='account:login'), name='dispatch')
class GenerateChequeRegularizadoPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('reports/cheque-regularizado.html')
        queryset = Cheque.objects.filter(estado_cheque='Regularizado')
        context = {
            "queryset": queryset,
            "data": timezone.now()
        }
        html = template.render(context)
        pdf = render_to_pdf('reports/cheque-regularizado.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Cheques_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")