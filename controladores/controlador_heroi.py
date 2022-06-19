from telas.tela_heroi import TelaHeroi
from entidades.heroi import Heroi


class ControladorHeroi:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_heroi = TelaHeroi()
        self.__manter_tela = True
        self.__herois = []

    def abrir_tela_opcoes(self):

        switcher = {0: self.retornar}

        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_heroi.tela_opcoes_heroi()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()

    # aqui eu crio o heroi em si (controlador heroi, perfetio sentido) e exporto ele pro controlador sistema
    def criar_heroi(self):
        novo_heroi = Heroi(self.__tela_heroi.pegar_nome_heroi(), 50, 10, "")
        self.__tela_heroi.mensagem("Herói criado!")
        # return novo_heroi #[luiza] acho que não precisa colocar para retornar

    def selecionar(self, usuario):
        pass

    def retornar(self):
        self.__manter_tela = False
