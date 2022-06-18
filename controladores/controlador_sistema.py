from controladores.controlador_heroi import ControladorHeroi
from controladores.controlador_mochila import ControladorMochila
from controladores.controlador_monstro import ControladorMonstro
from controladores.controlador_item import ControladorItem
from controladores.controlador_usuario import ControladorUsuario
from telas.tela_sistema import TelaSistema


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
    def controlador_heroi(self):
        return self.__controlador_heroi

    @property
    def controlador_mochila(self):
        return self.__controlador_mochila

    @property
    def controlador_monstro(self):
        return self.__controlador_monstro

    @property
    def controlador_item(self):
        return self.__controlador_item

    def iniciar(self):
        while True:
            opcao = self.__tela_sistema.tela_inicial()
            if opcao == 1:
                usuario = self.__controlador_usuario.logar()
                if usuario is not None:
                    opcao2 = self.__tela_sistema.tela_logados(usuario)
                    if opcao2 == 1:
                        self.__controlador_usuario.acessar_herois()
                    elif opcao2 == 2:
                        self.cadastro_heroi()
                    elif opcao2 == 3:
                        self.__controlador_usuario.opcoes_usuario()
                    elif opcao2 == 0:
                        self.iniciar()
            elif opcao == 2:
                self.__controlador_usuario.cadastrar()
            elif opcao == 3:
                self.encerrar_sistema()
            else:
                break

    def encerrar_sistema(self):
        exit()

    def cadastro_heroi(self):
        novo_heroi = self.__controlador_heroi.criar_heroi()
        lista_usuarios = self.__controlador_usuario.pega_usuario_por_heroi()
        # acima estão as duas exportações necessárias e abaixo está o seu código com algumas alterações
        # (os prints eu estava usando pra acompanhar o cod)
        for usuario in lista_usuarios:
            print(usuario)
            if novo_heroi.nome in usuario.lista_herois:
                self.__tela_sistema.mensagem("Heroi já existente")
                return None
            else:
                if novo_heroi not in usuario.lista_herois:
                    usuario.lista_herois.append(novo_heroi)
                    print(usuario.lista_herois)

    def escolhe_heroi(self, usuario):
        heroi = self.__controlador_heroi.selecionar(usuario)
        self.__controlador_heroi.abrir_tela_opcoes()

    def cadastrar_mochila(self):
        pass

    def cadastrar_monstro(self):
        pass

    def cadastrar_item(self):
        pass
