from . import views
from django.urls import path
from .views import logout_view


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("login/", views.LoginInterfaceView.as_view(), name='login'),
     path('logout/', logout_view, name='logout'),
    path("signup/", views.SignupView.as_view(), name='signup'),
]