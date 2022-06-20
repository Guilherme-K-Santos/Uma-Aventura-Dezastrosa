from telas.tela_monstro import TelaMonstro
from entidades.monstro import lista_monstros


class ControladorMonstro:
    def __init__(self, controlador_sistema):
        self.__tela_monstro = TelaMonstro()
        self.__lista_monstros = lista_monstros
        self.__controlador_sistema = controlador_sistema

    def listar(self):
        for monstro in self.__lista_monstros:
            self.__tela_monstro.mensagem(monstro.nome)

    def pega_monstro(self):
        self.listar()
        nome = self.__tela_monstro.escolher_monstro()
        for monstro in self.__lista_monstros:
            if monstro.nome == nome:
                return monstro
        else:
            self.__tela_monstro.mensagem("Monstro não existente")
            return self.pega_monstro()

    def remove(self, monstro):
        self.__lista_monstros.remove(monstro)
