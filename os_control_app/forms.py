from django import forms
from os_control_app.models import  OrdemServico


'''class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__" '''  

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = "__all__"

'''class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = "__all__"'''