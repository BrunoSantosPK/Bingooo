from bingooo.mecanica.cartao import Cartao
from bingooo.mecanica.gerador import Gerador
from bingooo.mecanica.sorteador import Sorteador


def criar_cartao_exemplo():
    b = [1, 2, 3, 4, 5]
    i = [21, 22, 23, 24, 25]
    n = [33, 34, 35, 36]
    g = [46, 47, 48, 49, 50]
    o = [64, 65, 66, 67, 68]
    return Cartao(b, i, n, g, o)


def test_cartao_valido():
    gerador = Gerador()
    cartao = criar_cartao_exemplo()
    assert gerador.validar_cartao(cartao) == True


def test_gerar_cartao():
    gerador = Gerador()
    cartao = gerador.gerar_cartao()
    assert gerador.validar_cartao(cartao) == True


def test_gerar_cartoes_em_massa():
    gerador = Gerador()
    quantidade = 10
    cartoes = gerador.gerar_cartoes_em_massa(quantidade)
    assert len(cartoes) == quantidade


def test_foi_marcado():
    cartao = criar_cartao_exemplo()
    marcou = cartao.marcar(1)
    assert marcou == True


def test_nao_foi_marcado():
    cartao = criar_cartao_exemplo()
    marcou = cartao.marcar(10)
    assert marcou == False


def test_cartao_ganhador():
    cartao = criar_cartao_exemplo()
    marcacoes = cartao.get_identificador().split(" ")
    marcacoes = [int(n) for n in marcacoes]
    regra = [True for n in range(len(marcacoes))]

    ganhador = False
    for m in marcacoes:
        cartao.marcar(m)
        ganhador = cartao.ganhou(regra)

    assert ganhador == True


def test_marcacao_sorteador():
    sorteador = Sorteador()
    cartao = criar_cartao_exemplo()

    regra = sorteador.criar_regra([True] * 24)
    sorteador.add_regra(regra)

    sorteador.add_cartao(cartao)
    sorteador.marcar(3)

    assert cartao.verifica_marcacao(3) == True


def test_sorteio_ganhador():
    sorteador = Sorteador()
    cartao = criar_cartao_exemplo()

    marcacoes = cartao.get_identificador().split(" ")
    marcacoes = [int(n) for n in marcacoes]

    regra = sorteador.criar_regra([True] * 24)
    sorteador.add_regra(regra)
    sorteador.add_cartao(cartao)

    for valor in marcacoes:
        sucesso, mensagem = sorteador.marcar(valor)
    
    ganhadores = sorteador.buscar_ganhadores()
    foi_ganhador = False

    for id_regra, id_cartao in ganhadores:
        cartao_ganhador = sorteador.get_cartao(id_cartao)
        if cartao_ganhador.get_identificador() == cartao.get_identificador():
            foi_ganhador = True

    assert foi_ganhador == True


def test_sorteio_regra_nova():
    sorteador = Sorteador()
    cartao = criar_cartao_exemplo()

    regra_marcacoes = [False] * 24
    regra_marcacoes[0] = True
    regra_marcacoes[6] = True
    regra_marcacoes[17] = True
    regra_marcacoes[23] = True

    regra = sorteador.criar_regra(regra_marcacoes)
    sorteador.add_regra(regra)
    sorteador.add_cartao(cartao)

    for valor in [1, 22, 49, 68, 70]:
        sucesso, mensagem = sorteador.marcar(valor)
    
    ganhadores = sorteador.buscar_ganhadores()
    foi_ganhador = False

    for id_regra, id_cartao in ganhadores:
        cartao_ganhador = sorteador.get_cartao(id_cartao)
        if cartao_ganhador.get_identificador() == cartao.get_identificador():
            foi_ganhador = True

    assert foi_ganhador == True
