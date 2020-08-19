from django.urls import path
from core.views import IndexView, EmitenteCreateView, ChequeCreateView, EmitenteListView


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('emitente/create/', EmitenteCreateView.as_view(), name='emitente-create'),
    path('emitente/', EmitenteListView.as_view(), name='emitente'),
    path('cheque/create/', ChequeCreateView.as_view(), name='cheque-create'),
    # path('emitente/create', views.EmitenteCreateView, name='emitente'),
   ]