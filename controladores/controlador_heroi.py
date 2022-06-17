from telas.tela_heroi import TelaHeroi
from entidades.heroi import Heroi


class ControladorHeroi:

    def __init__(self, controlador_sistema):
        self.__tela_heroi = TelaHeroi()
        self.__manter_tela = True
        self.__herois = []
        self.__controlador_sistema = controlador_sistema

    def abrir_tela_opcoes(self,usuario):
        
        switcher = {1: self.criar,
                    2: self.selecionar,
                    0: self.retornar}

        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_heroi.tela_opcoes_heroi()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida(usuario)

    def criar(self,usuario):
        nome = self.__tela_heroi.pegar_nome_heroi()
        novo_heroi = Heroi(nome, usuario)

        if novo_heroi not in usuario.lista_herois:
            usuario.lista_herois.append(novo_heroi)
            return novo_heroi
        else:
            self.__tela_heroi.mensagem("Heroi já existente")
            return None


    def selecionar(self, usuario):
        pass


    def retornar(self):
        self.__manter_tela = False
