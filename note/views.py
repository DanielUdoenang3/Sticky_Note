from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'note/register.html'
    success_url = reverse_lazy('notes.lis')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.lis')
        return super().get(request, *args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name = 'note/login.html'

def logout_view(request):
    logout(request)
    return redirect('home')

class HomeView(TemplateView):
    template_name = 'note/welcome.html'
