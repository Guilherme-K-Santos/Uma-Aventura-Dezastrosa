from entidades.item import Item

class Mochila:
    def __init__(self):
        self.__itens = [adaga_basica]

    @property
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, itens: list):
        if isinstance(itens, list):
            self.__itens = itens
