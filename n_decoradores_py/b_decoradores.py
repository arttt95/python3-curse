"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorator envolvem outras funções e aprimoram seus comportamentos;
- Decorators também sãso exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açucar Sintático)


/----------------------------------------------------------/
/              Function Decorator                          /
/----------------------------------------------------------/

/  /-------------------------------------------------------/  /
/  /-------------------------------------------------------/  /
/  /                    Função decorada                    /  /
/  /------------------------------------------------------/  /
/  /------------------------------------------------------/  /

# Decorators como funções (SIntaxe não recomendada / Sem Açucar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Geek University')


# Testando 1

# saudacao()

teste = seja_educado(saudacao)

teste()


# Testando 2

def raiva():
    print('EU TE ODEIO')

raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntaxy Sugar (Açucar Sintático)
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro!')

# Testando

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir()
"""

"""
----------------------------------------------------------------------------
|   Home     |    Serviços     |    Produtos     |     Administrativo      |
----------------------------------------------------------------------------

htttp://www.suaempresa.com.br/home

htttp://www.suaempresa.com.br/servicos

htttp://www.suaempresa.com.br/produtos

htttp://www.suaempresa.com.br/admin

# OBS: Não é código funcional (Que funcione) é apenas exemplo

def checa_login()
    if not request.usuario:
        redirect('htttp://www.suaempresa.com.br')

def home(request):
    return 'Pode acessar home'
    
def servicos(request):
    return 'Pode acessar serviços'
    
def produtos(request):
    return 'Pode acessar produtos'
    
@checa_login    
def admin(request):
    return 'Pode acessar admin'        
"""

# OBS: Não confundam Decorator com Decorator Functions
