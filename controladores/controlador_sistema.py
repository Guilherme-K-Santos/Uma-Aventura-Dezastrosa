from controladores.controlador_heroi import ControladorHeroi
from controladores.controlador_mochila import ControladorMochila
from controladores.controlador_monstro import ControladorMonstro
from controladores.controlador_item import ControladorItem
from telas.tela_sistema import TelaSistema
from controladores.controlador_usuario import ControladorUsuario


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario()
        self.__controlador_item = ControladorItem()
        self.__controlador_mochila = ControladorMochila()
        self.__controlador_monstro = ControladorMonstro()
        self.__controlador_heroi = ControladorHeroi()
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        pass

    @property
    def controlador_mochila(self):
        return self.__controlador_mochila

    @property
    def controlador_monstro(self):
        return self.__controlador_monstro

    @property
    def controlador_heroi(self):
        return self.__controlador_heroi

    @property
    def controlador_item(self):
        return self.__controlador_item
