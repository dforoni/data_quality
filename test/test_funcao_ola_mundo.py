from app.funcao import funcao_ola_mundo

def test_funcao_ola_mundo():
    saida = funcao_ola_mundo()
    gabarito = "ola, mundo"
    assert saida == gabarito