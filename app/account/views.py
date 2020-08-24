from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator

from core.models import User, Profile
from account.forms import UserRegisterForm, UserUpdateForm

from django.views.generic import CreateView, UpdateView, DetailView, ListView


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'user_register.html'
    form_class = UserRegisterForm
    success_url = '/'
    success_message = 'Sua conta foi criada com sucesso!'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'login.html'

# def loginView(request):
#     if request.user.is_authenticated:
#         return redirect('core:index')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('email')
#             password = request.POST.get('password')

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('core:index')
#             else:
#                 messages.info(request, 'Email Ou Paswword incorrectos!')
#         return render(request, 'login.html', {})

class UserLogoutView(LogoutView):
    template_name = 'login.html'

# @method_decorator(login_required(login_url='/account/login'),name='dispatch')
@login_required(login_url='core:login')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    success_message = "Seu perfil foi actualizado com sucesso!"
    template_name = 'update.html'
    form_class = UserUpdateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserUpdateView, self).form_valid(form)

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UserUpdateView, self).get(request,*args,**kwargs)

    def get_success_url(self):
        return reverse('account:update_profile',kwargs={'pk':self.object.pk})



