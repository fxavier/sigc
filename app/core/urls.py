from django.urls import path
from core.views import IndexView, EmitenteCreateView, ChequeCreateView, EmitenteListView, EmitenteUpdateView, \
                       GenerateEmitentePDF, TodosChequesListView, GenerateChequePDF, ChequeCanceladoListView, \
                       GenerateChequeCanceladoPDF, ChequeRegularizadoListView, GenerateChequeRegularizadoPDF
from core import views


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('emitente/create/', EmitenteCreateView.as_view(), name='emitente-create'),
    path('emitente/', EmitenteListView.as_view(), name='emitente'),
    path('emitente/<int:pk>', EmitenteUpdateView.as_view(), name='emitente-edit'),
    path('cheque/create/', ChequeCreateView.as_view(), name='cheque-create'),
    path('cheque/', TodosChequesListView.as_view(), name='cheque'),
    path('cheque/cancelado/', ChequeCanceladoListView.as_view(), name='cheque-cancelado'),
    path('cheque/relatorio/', GenerateChequePDF.as_view(), name='cheque-relatorio'),
    path('cheque/regularizado/', ChequeRegularizadoListView.as_view(), name='cheque-regularizado'),
    path('cheque-regularizado/relatorio/', GenerateChequeRegularizadoPDF.as_view(), name='cheque-regularizado-relatorio'),
    path('cheque-cancelado/relatorio/', GenerateChequeCanceladoPDF.as_view(), name='cheque-cancelado-relatorio'),
    path('celery/', views.celery, name='celery'),
    path('emitente/relatorio', GenerateEmitentePDF.as_view(), name='emitente-relatorio'),
    # path('emitente/create', views.EmitenteCreateView, name='emitente'),
   ]