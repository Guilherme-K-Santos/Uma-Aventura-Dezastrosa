from persistencia.DAO import AbstractDAO
from entidades.monstro import lista_monstros

class MonstroDAO(AbstractDAO):

    def __init__(self):
        super().__init__("monstros.pkl")
        self.__cache = {1:lista_monstros[0], 2:lista_monstros[1], 3:lista_monstros[2]}

    def get_all(self):
        return list(self.__cache.values())

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None
