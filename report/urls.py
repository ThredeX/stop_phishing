from django.urls import path
from . import views

app_name = 'report'
urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success')
]
