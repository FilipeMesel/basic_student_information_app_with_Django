# Aplicação CRUD em Django (Aplicativo Básico de Informações de Estudantes)

Este projeto é uma aplicação web simples baseada em Django que permite a adição, exclusão e atualização de informações de estudantes, com paginação.

# Funcionalidades Principais

    1. Lista de Estudantes: A página "home.html" exibe uma lista de estudantes cadastrados no sistema. Cada entrada inclui o ID, Nome, Email, Telefone, Classe e Marks do estudante.

    2. Cadastro e Edição de Estudantes: A página "cadastro_entidade.html" permite adicionar novos estudantes ou editar informações de estudantes existentes. Você pode preencher os campos de Nome, Email, Telefone, Classe e Marks para cada estudante.

    3. Exclusão de Estudantes: É possível excluir estudantes diretamente da lista de estudantes na página "home.html" clicando no botão "Excluir" ao lado do nome do estudante.

    4. Paginação: Os resultados na página "home.html" são paginados, o que significa que apenas um número específico de estudantes é exibido por página. Você pode navegar entre as páginas usando os links de paginação.

# Como Executar o Projeto

1. Clone este repositório para o seu ambiente de desenvolvimento local.

    ```bash
        git clone https://github.com/FilipeMesel/basic_student_information_app_with_Django.git
    ```

2. Navegue até a pasta do projeto.

    ```bash
        cd basic_student_information_app
    ```

3. Instale as dependências do projeto

    No caso, é só o Django

4. Aplique as migrações para configurar o banco de dados SQLite.

    ```bash
        python manage.py makemigatrions
        python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento.

    ```bash
        python manage.py runserver
    ```

6. Acesse o aplicativo no seu navegador em http://localhost:8000/home/

# Referências

O projeto usou como base o CRUD de estudantes apresentado em https://dev.to/shivamrohilla/top-5-django-projects-that-can-get-you-a-job-1mn3