from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render (request, 'homepage.html')

def login(request):
    return render (request, 'login.html')

def cadastro(request):
    return render (request, 'cadastro.html')

def produtos(request):
    return render (request, 'produtos.html')

def carrinho(request):
    return render (request, 'carrinho.html')

def checkout(request):
    return render (request, 'checkout.html')

def perfil(request):
    return render (request, 'perfil.html')

def contato(request):
    return render (request, 'contato.html')

def sobre(request):
    return render (request, 'sobre.html')

def ajuda(request):
    return render (request, 'ajuda.html')

def termos(request):
    return render (request, 'termos.html')

def privacidade(request):
    return render (request, 'privacidade.html')

def devolucao(request):
    return render (request, 'devolucao.html')

def entrega(request):
    return render (request, 'entrega.html')

def pagamento(request):
    return render (request, 'pagamento.html')

def suporte(request):
    return render (request, 'suporte.html')

def feedback(request):
    return render (request, 'feedback.html')

def promocoes(request):
    return render (request, 'promocoes.html')

def relatorios(request):
    return render (request, 'relatorios.html')

def configuracoes(request):
    return render (request, 'configuracoes.html')

def seguranca(request):
    return render (request, 'seguranca.html')

def acessibilidade(request):
    return render (request, 'acessibilidade.html')

def sustentabilidade(request):
    return render (request, 'sustentabilidade.html')

