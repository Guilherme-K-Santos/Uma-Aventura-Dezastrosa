from controladores.controlador_heroi import ControladorHeroi
from controladores.controlador_monstro import ControladorMonstro
from controladores.controlador_usuario import ControladorUsuario
from telas.tela_sistema import TelaSistema
from persistencia.heroiDAO import HeroiDAO


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_monstro = ControladorMonstro(self)
        self.__controlador_heroi = ControladorHeroi(self)
        self.__tela_sistema = TelaSistema()
        self.__heroi_dao = HeroiDAO()

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

    @property
    def controlador_heroi(self):
        return self.__controlador_heroi

    @property
    def controlador_monstro(self):
        return self.__controlador_monstro

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    def iniciar(self):
        while True:
            opcao = self.__tela_sistema.tela_inicial()
            if opcao == 1:
                usuario = self.__controlador_usuario.logar()
                if usuario is not None:
                    self.abrir_tela_logados(usuario)
            elif opcao == 2:
                self.__controlador_usuario.cadastrar()
            elif opcao == 3:
                self.__tela_sistema.abrir_tela_informacoes()
            elif opcao == 0:
                exit()

    def cadastro_heroi(self, usuario):
        novo_heroi, advice = self.__controlador_heroi.criar_heroi()
        if novo_heroi.nome in usuario.lista_nomes_herois:
            self.__tela_sistema.mostra_mensagem("Heroi já existente")
            return None
        else:
            print('adicionado')
            self.__heroi_dao.add(novo_heroi.nome, novo_heroi)
            self.__tela_sistema.mostra_mensagem(advice)
            usuario.lista_herois.append(novo_heroi)
            usuario.lista_nomes_herois.append(novo_heroi.nome)

    def abrir_tela_logados(self, usuario):
        opcao2 = self.__tela_sistema.tela_logados()
        if opcao2 == 1:
            heroi = self.__controlador_usuario.acessar_herois(usuario)
            if heroi is not None:
                self.abrir_tela_opcoes_jogo(heroi, usuario)
            else:
                self.__tela_sistema.mostra_mensagem('Nome de herói inválido, escolha um nome válido!')
                self.abrir_tela_logados(usuario)
        elif opcao2 == 2:
            self.cadastro_heroi(usuario)
            self.abrir_tela_logados(usuario)
        elif opcao2 == 3:
            self.__controlador_usuario.opcoes_usuario()
            self.abrir_tela_logados(usuario)

    def abrir_tela_opcoes_jogo(self, heroi, usuario):
        opcao3 = self.__tela_sistema.abrir_tela_opcoes_jogo(heroi)
        while opcao3 != 0:
            if opcao3 == 1:
                self.__controlador_heroi.combate(heroi, usuario)
            elif opcao3 == 2:
                self.__controlador_heroi.abre_mochila(heroi, usuario)
            elif opcao3 == 3:
                self.__controlador_heroi.descansar(heroi)
            elif opcao3 == 4:
                self.__controlador_heroi.ver_status(heroi)
            elif opcao3 == 5:
                self.__controlador_heroi.mudar_titulo(heroi)
            opcao3 = self.__tela_sistema.abrir_tela_opcoes_jogo(heroi)

    def regularizacao(self, indice):
        validacao = []
        contador = 0
        for _ in range(indice):
            validacao.append(contador)
            contador += 1
        return validacao
