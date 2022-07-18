from telas.tela_monstro import TelaMonstro
from entidades.monstro import lista_monstros


class ControladorMonstro:
    def __init__(self, controlador_sistema):
        self.__tela_monstro = TelaMonstro()
        self.__lista_monstros = lista_monstros
        self.__controlador_sistema = controlador_sistema

    def listar(self):
        contador = 1
        for monstro in self.__lista_monstros:
            self.__tela_monstro.mensagem("{} - {}".format(contador, monstro.nome))
            contador += 1

    def pega_monstro(self):
        if len(self.__lista_monstros) > 0:
            self.listar()
            self.__tela_monstro.mensagem("0 - Retornar")
            ind = self.__tela_monstro.escolher_monstro()
            if ind != 0:
                for monstro in self.__lista_monstros:
                    if monstro.nome == self.__lista_monstros[ind-1].nome:
                        return monstro
                else:
                    self.__tela_monstro.mensagem("Monstro não existente")
                    return self.pega_monstro()
            else:
                return None
        else:
            return "na"

    def remove(self, monstro):
        self.__lista_monstros.remove(monstro)
