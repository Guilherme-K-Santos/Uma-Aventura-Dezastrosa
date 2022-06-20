from entidades.personagem import Personagem
from entidades.mochila import Mochila
from entidades.usuario import Usuario
from entidades.mochila import Mochila
from entidades.item import Item


class Heroi(Personagem):
    def __init__(self, nome: str, hp: int, ataque: int, titulo: str):
        super().__init__(nome, hp, ataque, titulo)
        self.__lista_titulos = ["o(a) Noob"]
        self.__mochila = Mochila()
        self.__hp_extra = 0
        self.__hp_total = hp + self.__hp_extra
        self.__item_equipado = None

    @property
    def item_equipado(self):
        return self.__item_equipado

    @item_equipado.setter
    def item_equipado(self, item_equipado: Item):
        if isinstance(item_equipado, Item):
            self.__item_equipado = item_equipado

    @property
    def hp_total(self):
        return self.__hp_total

    @hp_total.setter
    def hp_total(self, hp_total: int):
        if isinstance(hp_total, int):
            self.__hp_total = hp_total

    @property
    def hp_extra(self):
        return self.__hp_extra

    @hp_extra.setter
    def hp_extra(self, hp_extra: int):
        if isinstance(hp_extra, int):
            self.__hp_extra = hp_extra

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
