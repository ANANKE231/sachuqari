from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    #path('my-admin/', views.custom_admin, name='custom_admin'),  
]