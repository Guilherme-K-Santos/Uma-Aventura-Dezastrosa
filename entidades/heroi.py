from entidades.personagem import Personagem
from entidades.mochila import Mochila


class Heroi(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.__nome = nome
        self.__hp = 20
        self.__ataque = 0
        self.__titulo = ""
        self.__lista_titulos = []
        self.__mochila = Mochila()

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
