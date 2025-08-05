from django.db import models

status_choices = (
    ('aberto', 'Aberto'),
    ('em_espera', 'Em espera'),
    ('em_atraso', 'Em atraso'),
    ('pausado', 'Pausado'),
    ('nao_atribuido', 'Não atribuído'),
    ('encerra_hoje', 'Encerra hoje'),
    ('concluidos', 'Concluídos')
)

prioridade_choices = (
    ('alta', 'Alta'),
    ('media', 'Média'),
    ('baixa', 'Baixa')
)

# Create your models here.
'''class Cliente(models.Model):
    cliente = models.CharField(max_length=30)
    nome_responsavel = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.cliente'''


class OrdemServico(models.Model):
    tarefa = models.CharField(null=False, max_length=250)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atendimento = models.DateField(blank=True, null=True)
    prioridade = models.CharField(max_length=30, choices=prioridade_choices)
    status = models.CharField(null=True, max_length=40, choices=status_choices)
    cliente = models.CharField(null=True, max_length=30)
    colaborador = models.CharField(null=True, max_length=50)
    funcao_colaborador = models.CharField(null=True, max_length=30)
    enviar_RAT = models.FileField(blank=True, null=True, upload_to='file_uploads/')
    obs_tarefa = models.TextField(null=True, max_length=300)
    

    def __str__(self):
        return self.tarefa
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

'''class Colaborador(models.Model):
    nome_colaborador = models.CharField(max_length=30)
    funcao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_colaborador'''