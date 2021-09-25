from typing import List


class Cartao:

    def __init__(self, b: List[int], i: List[int], n: List[int], g: List[int], o: List[int]):
        # Cria dicionário representativo do cartão e números em sequência
        self.__id = -1
        self.__letras = {"b": b, "i": i, "n": n, "g": g, "o": o}
        
        self.__numeros = []
        self.__numeros.extend(b)
        self.__numeros.extend(i)
        self.__numeros.extend(n)
        self.__numeros.extend(g)
        self.__numeros.extend(o)

        # Inicializa sequência de marcação
        self.__marcados = [False for i in range(len(self.__numeros))]

    def get_identificador(self) -> str:
        numeros = [str(n) for n in self.__numeros]
        return " ".join(numeros)

    def get_letras(self) -> dict:
        return self.__letras

    def get_id(self) -> int:
        return self.__id

    def set_id(self, valor: int) -> None:
        self.__id = valor

    def marcar(self, numero: int) -> bool:
        foi_marcado = False

        for i in range(len(self.__numeros)):
            if self.__numeros[i] == numero:
                self.__marcados[i] = True
                foi_marcado = True
                break

        return foi_marcado

    def verifica_marcacao(self, numero: int) -> bool:
        marcou = False
        for i in range(len(self.__numeros)):
            if self.__numeros[i] == numero and self.__marcados[i]:
                marcou = True

        return marcou

    def ganhou(self, regra: List) -> bool:
        ganhador = True

        for i in range(len(self.__marcados)):
            if regra[i] and not self.__marcados[i]:
                ganhador = False
                break

        return ganhador
