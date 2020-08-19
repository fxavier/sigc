from django.urls import path
from cheque.views import RegularizacaoCreateView

app_name = 'cheque'

urlpatterns = [
    path('regularizacao/create', RegularizacaoCreateView.as_view(), name='regularizacao-create'),
]