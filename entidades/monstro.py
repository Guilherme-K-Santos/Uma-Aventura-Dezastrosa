from entidades.personagem import Personagem
from entidades.item import Item


class Monstro(Personagem):
    def __init__(self, nome: str, hp: int, ataque: int, titulo: str, item_monstro: Item):
        super().__init__(nome, hp, ataque, titulo)
        self.__item_monstro = item_monstro

    @property
    def item_monstro(self):
        return self.__item_monstro

    @item_monstro.setter
    def item_monstro(self, item_monstro: Item):
        if isinstance(item_monstro, Item):
            self.__item_monstro = item_monstro


