# Gerenciador de Alunos e Professores

## Descrição

Esta aplicação Flask tem como objetivo gerenciar alunos e professores, permitindo que professores criem turmas e adicionem alunos com base no e-mail. A aplicação possibilitará, futuramente, o compartilhamento de arquivos e aulas dentro das turmas. A autenticação é baseada em sessões, e a aplicação utiliza um sistema de logs para registrar eventos importantes como login, criação de turmas e registro de usuários.

## Funcionalidades

- **Autenticação de usuários**: Alunos e professores podem se registrar e fazer login.
- **Dashboard personalizado**: Professores podem gerenciar suas turmas, enquanto alunos visualizam as turmas em que estão inscritos.
- **Criação de turmas**: Professores podem criar turmas e gerenciá-las.
- **Adição de alunos**: Professores podem adicionar alunos às suas turmas usando o e-mail do aluno.
- **Sistema de logs**: Todas as ações importantes são registradas em um arquivo de log para fins de auditoria e acompanhamento.

## Estrutura de Pastas

```bash
.
├── app.py               # Arquivo principal que executa a aplicação Flask
├── config.py            # Configurações da aplicação (e.g., chave secreta e URI do banco de dados)
├── logger/
│   └── log.py           # Implementação da classe de log para registrar eventos
├── models/
│   ├── classm.py        # Modelo de dados para turmas e relação aluno-turma
│   └── user.py          # Modelo de dados para usuários (alunos e professores)
├── routes/
│   ├── auth.py          # Rotas de autenticação (login, registro)
│   ├── class_routes.py  # Rotas relacionadas à criação e gerenciamento de turmas
│   └── dashboard.py     # Rota para o dashboard de alunos e professores
├── templates/           # Arquivos HTML para renderização de páginas
│   ├── add_student.html
│   ├── add_teacher.html
│   ├── create_class.html
│   ├── login.html
│   ├── manage_classes.html
│   ├── dashboard.html
│   └── menu.html
└── desenvolvimento_log.txt # Arquivo de log gerado automaticamente
```
## Tecnologias Utilizadas

- **Flask**: Framework web utilizado para desenvolver a aplicação.
- **Flask SQLAlchemy**: ORM utilizado para modelar e interagir com o banco de dados SQLite.
- **Werkzeug**: Utilizado para a geração e verificação de hashes de senha.
- **Blueprints**: Estrutura para organizar as rotas da aplicação em diferentes módulos.
- **Session**: Utilizado para gerenciar sessões de usuários autenticados.
- **HTML**: Templates para as interfaces.

## Como Executar o Projeto

1. Clone o repositório:
```bash
   git clone https://github.com/usuario/gerenciador-alunos-professores.git
   cd gerenciador-alunos-professores
```
2. Crie um ambiente virtual e ative-o:
```bash
    python3 -m venv venv
    venv\Scripts\activate
```
3. Instale as dependências:
```bash
    pip install -r requirements.txt

```
4. Execute a aplicação:
```bash
    python /flaskapp/app.py
```
5. Acesse a aplicação no seu navegador: http://localhost:5000.

## Banco de Dados

A aplicação utiliza um banco de dados SQLite para armazenar informações sobre usuários, turmas e suas relações. O banco é inicializado automaticamente na primeira execução do projeto, criando as tabelas definidas nos modelos `User`, `ClassM` e `ClassStudent`.

## Logs

O sistema de logs registra eventos importantes, como:

- **Login de usuários**: Um log é gerado toda vez que um usuário faz login ou tenta fazer login.
- **Registro de usuários**: O registro de novos alunos e professores é registrado no log.
- **Criação de turmas**: Quando um professor cria uma nova turma, essa ação é registrada.
- **Adição de alunos a turmas**: Professores que adicionam alunos às turmas geram entradas no log.

Todos os logs são armazenados no arquivo `desenvolvimento_log.txt`.

## Observação importante:
- O projeto está em desenvolvimento e planejamos, na sprint 4, desenvolver o sistema de arquivos assim como integrar o sistema de simulação de experiências, para que os estudantes da LEPIC pratiquem conforme o desafio lançado no Challenge.


## FORMA DE TESTAR
Caso for realizar o teste da aplicação, recomendamos que registre um usuário Aluno e um usuário Professor e realize os seguintes passos:

1) Logue como professor, crie uma turma através do dashboard e nomeie como desejar.
2) Dentro da tela da Turma (Ao editar) você poderá adicionar a conta de aluno que você criou, basta escrever o email de registro e clicar em adicionar
3) Deslogue como professor e logue novamente como aluno
4) Você poderá conferir que esta na sala assim como a conta de professor inseriu
5) Sinta-se livre para registrar quantos alunos/professores quiser e criar quantas turmas desejar!

6) Próxima atualização será possivel subir arquivos nas salas para os alunos verem!


