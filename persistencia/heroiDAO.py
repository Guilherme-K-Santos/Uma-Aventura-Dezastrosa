from persistencia.DAO import AbstractDAO
from entidades.heroi import Heroi


class HeroiDAO(AbstractDAO):
    def __init__(self):
        super().__init__("herois.pkl")

    def add(self, heroi: Heroi):
        if heroi is not None and isinstance(heroi, Heroi):
            super().add(heroi.nome, heroi)

    def get(self, nome_heroi: str):
        if nome_heroi is not None and isinstance(nome_heroi, str):
            return super().get(nome_heroi)

    def remove(self, nome_heroi: str):
        if nome_heroi is not None and isinstance(nome_heroi, str):
            return super().remove(nome_heroi)
