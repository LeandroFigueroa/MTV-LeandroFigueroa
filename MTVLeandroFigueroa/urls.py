from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FamilyProject.urls')),
    path('Miembros de la familia/', include('FamilyProject.urls')),
]
   