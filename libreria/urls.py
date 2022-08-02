from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('alfajores', views.alfajores, name='alfajores'),
    path('alfajores/crear', views.crear, name='crear'),
    path('alfajores/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('alfajores/editar/<int:id>', views.editar, name='editar'),
    path('login', views.login_request, name='login'),

    
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)