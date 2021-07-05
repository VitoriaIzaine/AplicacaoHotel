from django.shortcuts import render
import conexao
c = conexao.conectar()

# Create your views here.
def index(request):
    with c.cursor() as selecionar:
        sql = 'select * from tbaluno'
        selecionar.execute(sql)
        dados = selecionar.fetchall()
    return render(request, 'aluno/index.html', {'alunos' : dados})

def insere_aluno(request):
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')
    email = request.POST.get('email')

    with c.cursor() as inserir:
        sql = 'insert into tbaluno(nome, telefone, email) values(%s, %s, %s)'
        inserir.execute(sql,(nome, telefone, email))
        c.commit()
    return render(request, 'aluno/form_aluno.html')

def formulario(request):
    return render(request, 'aluno/form_aluno.html')

def home(request):
    return render(request, '../../home/templates/home/index.html')