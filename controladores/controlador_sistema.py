from controladores.controlador_heroi import ControladorHeroi
from controladores.controlador_mochila import ControladorMochila
from controladores.controlador_monstro import ControladorMonstro
from controladores.controlador_item import ControladorItem
from telas.tela_sistema import TelaSistema
from controladores.controlador_usuario import ControladorUsuario


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_item = ControladorItem(self)
        self.__controlador_mochila = ControladorMochila(self)
        self.__controlador_monstro = ControladorMonstro(self)
        self.__controlador_heroi = ControladorHeroi(self)
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        self.__tela_sistema.abre_tela()

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

    # controlador sistema vai ter uma função que vai levar a tela de usuario
    def usuarios(self):
        pass

    # controlador sistema vai ter uma função que vai levar a tela de heroi
    def herois(self):
        pass

    # controlador sistema vai ter uma função que vai levar a tela de heroi
    def mochila(self):
        pass

    def encerrar_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.usuarios, 2: self.herois, 3: self.mochila,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
