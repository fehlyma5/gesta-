from django.urls import path
from.views import *

urlpatterns = [
    
    path('', homepage, name='homepage'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('produtos/', produtos, name='produtos'),
    path('carrinho/', carrinho, name='carrinho'),
    path('checkout/', checkout, name='checkout'),
    path('perfil/', perfil, name='perfil'),
    path('contato/', contato, name='contato'),
    path('privacidade/', privacidade, name='privacidade'),
    path('devolucao/', devolucao, name='devolucao'),
    path('entrega/', entrega, name='entrega'),
    path('pagamento/', pagamento, name='pagamento'),
    path('suporte/', suporte, name='suporte'),
    path('feedback/', feedback, name='feedback'),
    path('promocoes/', promocoes, name='promocoes'),
    path('relatorios/', relatorios, name='relatorios'),
    path('configuracoes/', configuracoes, name='configuracoes'),
    path('seguranca/', seguranca, name='seguranca'),
    path('acessibilidade/', acessibilidade, name='acessibilidade'),
    path('sustentabilidade/', sustentabilidade, name='sustentabilidade'),
]