from telas.tela_heroi import TelaHeroi
from entidades.heroi import Heroi


class ControladorHeroi:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_heroi = TelaHeroi()
        self.__manter_tela = True
        self.__herois = []

    # aqui eu crio o heroi em si (controlador heroi, perfetio sentido) e exporto ele pro controlador sistema
    def criar_heroi(self):
        novo_heroi = Heroi(self.__tela_heroi.pegar_nome_heroi(), 50, 10, "o(a) Noob")
        self.__tela_heroi.mensagem("Herói criado!")
        self.__herois.append(novo_heroi)
        return novo_heroi

    def retornar(self):
        self.__manter_tela = False
