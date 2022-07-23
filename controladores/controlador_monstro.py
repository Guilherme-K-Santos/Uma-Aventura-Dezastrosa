from telas.tela_monstro import TelaMonstro
from entidades.monstro import lista_monstros
from persistencia.monstroDAO import MonstroDAO


class ControladorMonstro:
    def __init__(self, controlador_sistema):
        self.__tela_monstro = TelaMonstro()
        self.__controlador_sistema = controlador_sistema
        self.__monstro_dao = MonstroDAO()

    def pega_monstro(self):
        monstro = None
        id = self.__tela_monstro.escolher_monstro()
        if id != 0:
            monstro = self.__monstro_dao.get(id)
            self.__tela_monstro.mensagem(monstro.nome)
        return monstro

    def remove(self, id):
        self.__monstro_dao.remove(id)
