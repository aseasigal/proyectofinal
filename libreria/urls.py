from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('alfajores', views.alfajores, name='alfajores'),
    path('alfajores/crear', views.crear, name='crear'),
    path('alfajores/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('alfajores/editar/<int:id>', views.editar, name='editar'),
    path('login', views.login_request, name='login'),
    path('registro', views.registro, name='registro'),
    path('perfileditar', views.editarPerfil, name='EditarPerfil'),
    path('logout', LogoutView.as_view(template_name = 'paginas/logout.html'), name='logout'),


    
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)