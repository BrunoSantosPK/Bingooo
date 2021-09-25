import random
from typing import List
from bingooo.mecanica.cartao import Cartao


class Gerador:

    def __init__(self):
        self.__limites = {
            "b": (1, 15, 5),
            "i": (16, 30, 5),
            "n": (31, 45, 4),
            "g": (46, 60, 5),
            "o": (61, 75, 5)
        }

    def gerar_cartao(self) -> Cartao:
        gerados = {"b": [], "i": [], "n": [], "g": [], "o": []}

        for letra in gerados.keys():
            # Recupera range de números e total na letra
            valor_minimo = self.__limites[letra][0]
            valor_maximo = self.__limites[letra][1]
            numeros_necessarios = self.__limites[letra][2]

            while len(gerados[letra]) < numeros_necessarios:
                numero = random.randint(valor_minimo, valor_maximo)
                
                if numero not in gerados[letra]:
                    gerados[letra].append(numero)

            # Ordena valores gerados
            gerados[letra].sort()
        
        return Cartao(gerados["b"], gerados["i"], gerados["n"], gerados["g"], gerados["o"])

    def gerar_cartoes_em_massa(self, quantidade: int) -> List[Cartao]:
        cartoes: List[Cartao] = []

        while len(cartoes) < quantidade:
            # Cria um cartão novo, supostamente válido
            cartao = self.gerar_cartao()
            valido = True

            # Verifica se o cartão é repetido
            for c in cartoes:
                if cartao.get_identificador() == c.get_identificador():
                    valido = False

            # Adiciona o cartão
            if valido:
                cartoes.append(cartao)

        return cartoes

    def validar_cartao(self, cartao: Cartao) -> bool:
        letras = cartao.get_letras()
        valido = True

        for letra in letras.keys():
            # Recupera range de números e total na letra
            valor_minimo = self.__limites[letra][0]
            valor_maximo = self.__limites[letra][1]
            numeros_necessarios = self.__limites[letra][2]

            # Valida o tamanho do conjunto de números na letra
            if len(letras[letra]) != numeros_necessarios:
                valido = False
                break

            # Valida os valores dentro do conjunto da letra
            for n in letras[letra]:
                if n < valor_minimo or n > valor_maximo:
                    valido = False
                    break

        return valido
