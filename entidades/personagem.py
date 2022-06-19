from abc import ABC, abstractmethod


class Personagem(ABC):
    @abstractmethod
    def __init__(self, nome, hp, ataque, titulo):
        self.__nome = nome
        self.__hp = hp
        self.__ataque = ataque
        self.__titulo = titulo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp: int):
        if isinstance(hp, int):
            self.__hp = hp

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, ataque: int):
        if isinstance(ataque, int):
            self.__ataque = ataque

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    def atacar(self, ataque: int, hp: int):
        pass
