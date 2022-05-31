from django.urls import path
from . import views  

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path ('pariente/<str:pk>', views.family_members,name='familiar' )
]
  