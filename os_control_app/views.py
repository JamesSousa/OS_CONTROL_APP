from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.template import loader
from os_control_app.forms import OrdemServicoForm
from os_control_app.models import OrdemServico
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
MESSAGE_TAGS = {
    messages.INFO: "",
    50: "critical",
    messages.SUCCESS: "",
    50: "success",
}




'''class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def signup(request):
    sig = SignUpView()
    return sig'''

'''def login(request):
    username = request.POST["nome"]
    password = request.POST["senha"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('usuarios/')
        
    else:
        return render(request, 'authentication/login.html')'''
        
'''def login(request):
    return render(request, 'authentication/login.html')'''


#@require_POST
@login_required
def cadastrar_usuario(request):
    '''nome_usuario = request.POST['nome']
    email = request.POST['email']
    senha = request.POST['senha']
    
    novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
    novoUsuario.save()'''

    return render(request, 'adiciona_usuarios.html')

@login_required
def add_user(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            return render(request, 'adiciona_usuarios.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

    except User.DoesNotExist:
        nome_usuario = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        
        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        return redirect('usuarios/')



'''def cliente(request):
    if request.method == 'GET':
        form = ClienteForm()
        context = {
            'form': form
        }
        
        return render(request, 'cliente.html', context=context)
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ClienteForm()
    context = {
        'form': form
    }
    
    return render(request, 'cliente.html', context=context)'''    

@login_required
def index(request):  
    '''todas_as_tarefas = {
        'todas_as_tarefas': OrdemServico.objects.all()
    }'''

    '''clientes = {
        'clientes': Cliente.objects.all()
    }'''
    context = {
        'todas_as_tarefas': OrdemServico.objects.all(),
        'status_em_espera': OrdemServico.objects.filter(status='em_espera').count(),
        'status_aberto': OrdemServico.objects.filter(status='aberto').count(),
        'status_em_atraso': OrdemServico.objects.filter(status='em_atraso').count(),
        'status_pausado': OrdemServico.objects.filter(status='pausado').count(),
        'status_nao_atribuido': OrdemServico.objects.filter(status='nao_atribuido').count(),
        'status_encerra_hoje': OrdemServico.objects.filter(status='encerra_hoje').count(),
        'status_concluidos': OrdemServico.objects.filter(status='concluidos').count(),
    }
    
    return render(request, 'index.html', context=context)

'''def colaborador(request):  
    if request.method == 'GET':
        form = ColaboradorForm()
        context = {
            'form': form
        } 
        return render(request, 'colaborador.html', context=context)
    else:
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            Colaborador = form.save()
            form = ColaboradorForm()
    context = {
        'form': form
    }
    
    return render(request, 'colaborador.html', context=context)'''

@login_required

def tarefas(request): 
    
    if request.method == 'GET': 
        form_tarefa = OrdemServicoForm()
        context = {
            'form_tarefa': form_tarefa
        } 
        return render(request, 'ordem_servico.html', context=context)
    else:
        form_tarefa = OrdemServicoForm(request.POST, request.FILES)
        if form_tarefa.is_valid():
            OrdemServico = form_tarefa.save()
            form_tarefa = OrdemServicoForm()
            aviso = 'Cadastrado com sucesso!!'
            msg = messages.add_message(request, messages.SUCCESS, 'Cadastrado com sucesso!!')
            
            context = {
                    'form_tarefa': form_tarefa,
                    'message': msg
                } 
            
            return render(request, 'ordem_servico.html', context=context)
    
@login_required
def pesquisa_tarefa(request):
    #Realizando pesquisa e filtra na tabela
    
    busca_tarefa = request.GET.get('pesquisa')
    if busca_tarefa.isdigit():
        if busca_tarefa:
            
            context = {
                'todas_as_tarefas': OrdemServico.objects.filter(tarefa = busca_tarefa)
            }

        return render(request, 'index.html', context=context)

    else:
        context = {
        'todas_as_tarefas': OrdemServico.objects.all()
    }
    return render(request, 'index.html', context=context)

@login_required
def deleta_tarefa(request, id):
    deleta_tarefa = get_object_or_404(OrdemServico, id = id)
    
    deleta_tarefa.delete()
        
    # Exibi todos os pedidos já cadastrados
    context = {
        'todas_as_tarefas': OrdemServico.objects.all()
    }
    return redirect('/', context=context)


@login_required
def tarefa_update(request, id):
    #Busca a tarefa que queremos editar
    tarefa_update = get_object_or_404(OrdemServico, pk=id)
    # Preenche o formulários com os dados
    form_update = OrdemServicoForm(instance=tarefa_update)
    if(request.method == 'POST'):
        form_update = OrdemServicoForm(request.POST, instance=tarefa_update)
    
        
        if(form_update.is_valid()):
            tarefa_update = form_update.save(commit=False)
            tarefa_update.tarefa = form_update.cleaned_data['tarefa']
            #tarefa_update.data_cadastro = form_update.cleaned_data['data_cadastro']
            tarefa_update.data_atendimento = form_update.cleaned_data['data_atendimento']
            tarefa_update.prioridade = form_update.cleaned_data['prioridade']
            tarefa_update.status = form_update.cleaned_data['status']
            tarefa_update.cliente = form_update.cleaned_data['cliente']
            tarefa_update.colaborador = form_update.cleaned_data['colaborador']
            tarefa_update.funcao_colaborador = form_update.cleaned_data['funcao_colaborador']
            tarefa_update.obs_tarefa = form_update.cleaned_data['obs_tarefa']

            msg = messages.add_message(request, messages.SUCCESS, 'Atualizado com sucesso!!')

            tarefa_update.save()
            context = {
                'todas_as_tarefas': OrdemServico.objects.all(),
                'message': msg
            }
            
            return redirect('/', context=context)
            
        else:
            return render(request, 'tarefa_update.html', {'form_update': form_update, 'tarefa_update' : tarefa_update})
    elif(request.method == 'GET'):
        return render(request, 'tarefa_update.html', {'form_update': form_update, 'tarefa_update' : tarefa_update})
 

@login_required
def usuarios(request):
    User = get_user_model()
    all_users = {
        'usuarios': User.objects.all().values()}

    return render(request, 'usuarios.html', all_users)

def alerta_excluir(request, id):
    id = {
        'id': id
    }
    return render(request, 'alerta_excluir.html', id)

@login_required
def dashboard_sidebar(request):
    
    context = {
        'todas_as_tarefas': OrdemServico.objects.all(),
        'status_em_espera': OrdemServico.objects.filter(status='em_espera').count(),
        'status_aberto': OrdemServico.objects.filter(status='aberto').count(),
        'status_em_atraso': OrdemServico.objects.filter(status='em_atraso').count(),
        'status_pausado': OrdemServico.objects.filter(status='pausado').count(),
        'status_nao_atribuido': OrdemServico.objects.filter(status='nao_atribuido').count(),
        'status_encerra_hoje': OrdemServico.objects.filter(status='encerra_hoje').count(),
        'status_concluidos': OrdemServico.objects.filter(status='concluidos').count(),
    }
    return render(request, 'dashboard_sidebar.html', context=context)



