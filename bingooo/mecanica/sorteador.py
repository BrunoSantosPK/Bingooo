from typing import List, Tuple
from bingooo.mecanica.cartao import Cartao


class Regra:

    def __init__(self, marcacoes: List[bool], nome: str):
        self.__nome = nome
        self.__marcacoes = marcacoes
        self.__ativa = True
        self.__id = -1

    def get_nome(self) -> str:
        return self.__nome

    def get_marcacoes(self) -> List[bool]:
        return self.__marcacoes

    def get_id(self) -> int:
        return self.__id

    def esta_ativa(self) -> bool:
        return self.__ativa

    def set_ativa(self, valor: bool) -> None:
        self.__ativa = valor

    def set_id(self, valor: int) -> None:
        self.__id = valor


class Sorteador:

    def __init__(self):
        self.__sorteados = []
        self.__cartoes: List[Cartao] = []
        self.__regras: List[Regra] = []

        self.__contador_cartoes = 1
        self.__contador_regras = 1

    def get_cartao(self, id_cartao: int) -> Cartao:
        for cartao in self.__cartoes:
            if cartao.get_id() == id_cartao:
                return cartao

    def add_cartao(self, cartao: Cartao) -> int:
        # Atribui um id ao cartão e realiza autoincremento
        cartao.set_id(self.__contador_cartoes)
        self.__contador_cartoes = self.__contador_cartoes + 1

        # Registra cartão no observer
        self.__cartoes.append(cartao)

    def add_regra(self, regra: Regra):
        # Atribui id à regra e realiza autoincremento
        regra.set_id(self.__contador_regras)
        self.__contador_regras = self.__contador_regras + 1

        # Registra regra nas válidas
        self.__regras.append(regra)

    def criar_regra(self, marcacoes: List[bool], nome=""):
        if nome == "":
            nome = f"regra-{len(self.__regras) + 1}"

        return Regra(marcacoes, nome)

    def marcar(self, numero: int) -> Tuple[bool, str]:
        # Não realiza marcação se não existir regra
        if len(self.__regras) == 0:
            return False, "Não existem regras para realizar marcação."

        # Não marca se não existirem regras ativas (existem prêmios)
        terminaram_premios = True
        for regra in self.__regras:
            if regra.esta_ativa():
                terminaram_premios = False

        if terminaram_premios:
            return False, "Não existem mais regras ativas para sorteio."

        # Não realiza marcação se o número já foi sorteado
        if numero in self.__sorteados:
            return False, "O número já foi sorteado."
        
        # Faz a marcação em cada cartão
        for cartao in self.__cartoes:
            cartao.marcar(numero)

        self.__sorteados.append(numero)
        return True, "Marcação realizada com sucesso."

    def buscar_ganhadores(self) -> List[Tuple[int, int]]:
        ganhadores: List[Tuple[int, int]] = []

        for regra in self.__regras:
            # Regras não ativas significam ganhadores já sorteados
            if not regra.esta_ativa():
                continue

            marcacao = regra.get_marcacoes()
            for cartao in self.__cartoes:
                ganhou = cartao.ganhou(marcacao)

                # Se um cartão foi ganhador, registr o cartão e destiva a regra
                if ganhou:
                    ganhadores.append((regra.get_id(), cartao.get_id()))

                    if regra.esta_ativa():
                        regra.set_ativa(False)

        return ganhadores
