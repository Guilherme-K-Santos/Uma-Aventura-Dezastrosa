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

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

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

    def iniciar(self):
        self.abre_tela_nao_logados()

    # controlador sistema vai ter uma função que vai levar a tela de usuario
    def usuarios_nao_logados(self):
        self.__controlador_usuario.abre_tela_usuarios_nao_logados()

    # controlador sistema vai ter uma função que vai levar a tela de heroi
    def instrucoes_de_combate(self):
        pass

    # controlador sistema vai ter uma função que vai levar a tela de mochila
    def informacoes_de_monstros_itens(self):
        pass

    # para desligar o sistema
    def encerrar_sistema(self):
        exit()

    # switcher linkado na tela_sistema
    def abre_tela_nao_logados(self):
        lista_opcoes = {1: self.usuarios_nao_logados, 2: self.instrucoes_de_combate,
                        3: self.informacoes_de_monstros_itens, 0: self.encerrar_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_nao_logados()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
