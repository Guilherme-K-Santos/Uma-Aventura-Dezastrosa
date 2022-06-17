

class Usuario:
    def __init__(self, login: str, senha: int):
        self.__login = login
        self.__senha = senha
        self.__lista_herois = []

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        if isinstance(login, str):
            self.__login = login

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: int):
        if isinstance(senha, int):
            self.__senha = senha

    @property
    def lista_herois(self):
        return self.__lista_herois

    @lista_herois.setter
    def lista_herois(self, lista_herois: list):
        self.__lista_herois = lista_herois

