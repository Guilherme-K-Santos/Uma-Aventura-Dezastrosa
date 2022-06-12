from entidades.personagem import Personagem
from entidades.mochila import Mochila


class Heroi(Personagem):
    def __init__(self, nome: str, hp: int, ataque: int, titulo: str, lista_titulos: [], mochila: Mochila):
        super().__init__(nome, hp, ataque, titulo)
        self.__lista_titulos = lista_titulos
        self.__mochila = mochila

    @property
    def mochila(self):
        return self.__mochila

    @mochila.setter
    def mochila(self, mochila: Mochila):
        if isinstance(mochila, Mochila):
            self.__mochila = mochila

    @property
    def lista_titulos(self):
        return self.__lista_titulos

    @lista_titulos.setter
    def lista_titulos(self, lista_titulos: []):
        if isinstance(lista_titulos, list):
            self.__lista_titulos = lista_titulos
