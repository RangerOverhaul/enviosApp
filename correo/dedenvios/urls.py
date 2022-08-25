from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

#app_name = 'dedenvios'
urlpatterns = [
    path('', views.index, name='index'),
    path('userdata/', views.userdata, name='userdata'),
    path('loggin/', LoginView.as_view(template_name='loggin.html'), name='loggin'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('history/', views.history, name='history'),
    path('loggin/register/', views.register2, name='register2'),
    path('thing/<str:userid>/', views.thing, name='thing'),
    path('datos/', views.datos, name='datos'),
    path('datos/package/<str:userid>/<str:destid>/', views.package, name='package'),
]