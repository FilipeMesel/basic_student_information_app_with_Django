from django import forms
from .models import StudentModel

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['nome', 'email', 'telefone', 'classe', 'marks']  # Liste todos os campos que deseja incluir no formulário
