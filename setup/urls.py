from django.contrib import admin
from django.urls import path, include
from os_control_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
#from os_control_app.views import SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("cadastrar_usuario/", views.cadastrar_usuario, name='cadastrar_usuario'),
    path("add_user/", views.add_user, name='add_user'),
    #path('cliente/', views.cliente, name='cliente'),
    #path('colaborador/', views.colaborador, name='colaborador'),
    path('tarefas/', views.tarefas, name='tarefas'),
    #exibe minha pagina index
    path('', views.index, name='index'),
    path('pesquisa_tarefa/', views.pesquisa_tarefa, name='pesquisa_tarefa'),
    path('deleta_tarefa/<int:id>', views.deleta_tarefa, name='deleta_tarefa'),
    path('tarefa_update/<int:id>/', views.tarefa_update, name='tarefa_update'),
    #path('tarefa_update_salva/', views.tarefa_update_salva, name='tarefa_update_salva'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('alerta_excluir/<id>', views.alerta_excluir, name='alerta_excluir'),
    path('dashboard_sidebar/', views.dashboard_sidebar, name='dashboard_sidebar'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
