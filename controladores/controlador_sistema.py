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
        while True:
            opcao = self.__tela_sistema.abre_tela_inicial()
            if opcao == 1:
                if self.__controlador_usuario.logar() is not None:
                    self.__controlador_heroi.abrir_tela_opcoes()
            elif opcao == 2:
                self.__controlador_usuario.cadastrar()
            elif opcao == 3:
                self.encerrar_sistema()
            else:
                break

    def encerrar_sistema(self):
        exit()

    # controlador sistema vai ter uma função que vai levar a tela de usuario #[luiza] vou testar fazer as coisas sem isso
    #def usuarios_nao_logados(self):
    #    self.__controlador_usuario.abre_tela_usuarios_nao_logados()

    # controlador sistema vai ter uma função que vai levar a tela de heroi
    #def instrucoes_de_combate(self):
    #    pass

    # controlador sistema vai ter uma função que vai levar a tela de mochila
    #def informacoes_de_monstros_itens(self):
    #    pass

    # switcher linkado na tela_sistema
    #def abre_tela_nao_logados(self):
    #    lista_opcoes = {1: self.usuarios_nao_logados, 2: self.instrucoes_de_combate,
    #                    3: self.informacoes_de_monstros_itens, 0: self.encerrar_sistema}
    #    while True:
    #        opcao_escolhida = self.__tela_sistema.tela_nao_logados()
    #        funcao_escolhida = lista_opcoes[opcao_escolhida]
    #        funcao_escolhida()
