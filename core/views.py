from django.shortcuts import render, redirect
from .models import StudentModel
from .forms import StudentModelForm
from django.core.paginator import Paginator

def home(request):
    entidades = StudentModel.objects.all()
    # Defina o número de estudantes por página
    estudantes_por_pagina = 5

    # Obtenha o número da página a ser exibida a partir da consulta GET ou use 1 como padrão
    page_number = request.GET.get('page', 1)

    # Certifique-se de que page_number seja um inteiro válido
    page_number = int(page_number)

    # Calcule os índices de início e fim dos estudantes para a página atual
    start_index = (page_number - 1) * estudantes_por_pagina
    end_index = start_index + estudantes_por_pagina

    # Obtenha apenas os estudantes para a página atual
    estudantes_da_pagina = entidades[start_index:end_index]
    print(estudantes_da_pagina)

    # Crie um objeto Paginator para os estudantes da página atual
    paginator = Paginator(entidades, estudantes_por_pagina)

    # Obtenha a página atual com base no número da página
    page = paginator.get_page(page_number)

    return render(request, 'home.html', {'page': page, 'estudantes_da_pagina': estudantes_da_pagina})

def cadastrar_entidade(request):

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            entidade = form.save(commit=False)
            entidade.save()
            return redirect('home')  # Redirecione para a página de listagem de entidades
    else:
        form = StudentModelForm()

    return render(request, 'cadastro_entidade.html', {'form': form})

def deletar_entidade(request, entidade_id):

    print(entidade_id)
    try:

        entidade = StudentModel.objects.get(id=entidade_id)
        # Use o método delete() para removê-lo
        entidade.delete()

    except StudentModel.DoesNotExist:

        # Se o estudante com o ID especificado não existir, trate a exceção
        print("O estudante com o ID especificado não existe.")

    except Exception as e:
        # Trate outras exceções, se necessário
        print("Ocorreu um erro ao remover o estudante:", str(e))
    
    entidades = StudentModel.objects.all()
    # Defina o número de estudantes por página
    estudantes_por_pagina = 5

    # Obtenha o número da página a ser exibida a partir da consulta GET ou use 1 como padrão
    page_number = request.GET.get('page', 1)

    # Certifique-se de que page_number seja um inteiro válido
    page_number = int(page_number)

    # Calcule os índices de início e fim dos estudantes para a página atual
    start_index = (page_number - 1) * estudantes_por_pagina
    end_index = start_index + estudantes_por_pagina

    # Obtenha apenas os estudantes para a página atual
    estudantes_da_pagina = entidades[start_index:end_index]
    print(estudantes_da_pagina)

    # Crie um objeto Paginator para os estudantes da página atual
    paginator = Paginator(entidades, estudantes_por_pagina)

    # Obtenha a página atual com base no número da página
    page = paginator.get_page(page_number)

    return render(request, 'home.html', {'page': page, 'estudantes_da_pagina': estudantes_da_pagina})

def editar_entidade(request, entidade_id):
    
    entidade = StudentModel.objects.get(id=entidade_id)

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=entidade)  # Passe a instância do objeto entidade para o formulário
        if form.is_valid():
            form.save()  # Salve o objeto entidade com os dados do formulário atualizados
            return redirect('home')  # Redirecione para a página de listagem de entidades
    else:
        form = StudentModelForm(instance=entidade)  # Passe a instância do objeto entidade para o formulário

    return render(request, 'cadastro_entidade.html', {'form': form})