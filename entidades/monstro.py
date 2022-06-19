from entidades.personagem import Personagem
from entidades.item import itens_monstros


class Monstro(Personagem):
    def __init__(self, nome: str, hp: int, ataque: int, titulo: str, item_monstro: itens_monstros):
        super().__init__(nome, hp, ataque, titulo)
        self.__item_monstro = item_monstro

    @property
    def item_monstro(self):
        return self.__item_monstro

    @item_monstro.setter
    def item_monstro(self, item_monstro: itens_monstros):
        if isinstance(item_monstro, itens_monstros):
            self.__item_monstro = item_monstro


vampiro = Monstro("Morbius", 10, 20, "It's morbin time", itens_monstros[0])
mihawk = Monstro("Mihawk", 20, 40, "O Melhor Espadachim", itens_monstros[1])
demon_lord = Monstro("Lorde Demônio", 40, 70, "O Imperador do Mundo", itens_monstros[2])
