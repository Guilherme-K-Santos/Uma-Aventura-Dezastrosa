from persistencia.DAO import AbstractDAO
from entidades.heroi import Heroi
from persistencia.usuarioDAO import UsuarioDAO


class HeroiDAO(AbstractDAO):
    __instance = None

    def __init__(self):
        super().__init__("herois.pkl")
        self.__usuario_dao = UsuarioDAO()

    def __new__(cls):
        if HeroiDAO.__instance is None:
            HeroiDAO.__instance = object.__new__(cls)
        else:
            return HeroiDAO.__instance


    def add(self, key, heroi: Heroi):
        if heroi is not None and isinstance(heroi, Heroi):
            super().add(heroi.nome, heroi)
            self.__usuario_dao.persist()

    def get(self, nome_heroi: str):
        if nome_heroi is not None and isinstance(nome_heroi, str):
            return super().get(nome_heroi)

    def remove(self, nome_heroi: str):
        if nome_heroi is not None and isinstance(nome_heroi, str):
            return super().remove(nome_heroi)
