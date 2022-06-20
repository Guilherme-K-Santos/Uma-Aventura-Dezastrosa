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
                self.__tela_sistema.informacoes_jogo()
            elif opcao == 0:
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
            if novo_heroi.nome in usuario.lista_nomes_herois:
                self.__tela_sistema.mensagem("Heroi já existente")
                return None
            else:
                if novo_heroi not in usuario.lista_herois:
                    usuario.lista_herois.append(novo_heroi)
                    usuario.lista_nomes_herois.append(novo_heroi.nome)
                    print(usuario.lista_nomes_herois)

    def escolhe_heroi(self, usuario):
        heroi = self.__controlador_heroi.selecionar(usuario)
        self.__controlador_heroi.abrir_tela_opcoes()

    def combate(self,heroi,usuario):
        monstro = self.__controlador_monstro.pega_monstro()
        if heroi.ataque >= monstro.hp:
            heroi.mochila.itens.append(monstro.item_monstro)
            heroi.lista_titulos.append(monstro.titulo)
            heroi.hp = heroi.hp + heroi.hp_extra - monstro.ataque
            self.__tela_sistema.mensagem("Parabéns! Você matou o monstro!")
            self.__tela_sistema.mensagem("Um novo item apareceu em sua mochila")
            self.__tela_sistema.mensagem("Equipe-o para o próximo combate")
            self.__tela_sistema.mensagem("Lembre-se de descansar de sua última batalha")
            return self.abrir_tela_opcoes_jogo(heroi, usuario)
        else:
            self.__tela_sistema.mensagem("GAME OVER")
            self.__tela_sistema.mensagem("Seu herói morreu, crie outro herói")
            self.__tela_sistema.mensagem("Você não foi prudente >:(")
            self.__controlador_usuario.remove_heroi(heroi, usuario)
            return self.abrir_tela_logados(usuario)

    def abrir_tela_logados(self, usuario):
        opcao2 = self.__tela_sistema.tela_logados(usuario)
        if opcao2 == 1:
            heroi = self.__controlador_usuario.acessar_herois(usuario)
            if heroi is not None:
                self.abrir_tela_opcoes_jogo(heroi,usuario)
            else:
                self.abrir_tela_logados(usuario)
        elif opcao2 == 2:
            self.cadastro_heroi()
            self.abrir_tela_logados(usuario)
        elif opcao2 == 3:
            self.__controlador_usuario.opcoes_usuario()
            self.abrir_tela_logados(usuario)


    def abrir_tela_opcoes_jogo(self,heroi,usuario):
        opcao3 = self.__tela_sistema.tela_opcoes_jogo(heroi)
        while opcao3 != 0:
            if opcao3 == 1:
                self.combate(heroi,usuario)
            elif opcao3 == 2:
                self.abre_mochila(heroi)
            elif opcao3 == 3:
                self.descansar(heroi)
            elif opcao3 == 4:
                pass
            opcao3 = self.__tela_sistema.tela_opcoes_jogo(heroi)

    def pega_mochila(self,heroi):
        mochila_do_heroi = heroi.mochila
        return mochila_do_heroi

    def abre_mochila(self,heroi):
        self.__tela_sistema.mensagem("-----MOCHILA----")
        indice = 0
        for item in heroi.mochila.itens:
            print(indice, "-", item.nome_item)
            indice += 1
        indice_item = self.__tela_sistema.escolhe_itens()
        item_escolhido = heroi.mochila.itens[indice_item]
        print("Você escolheu: ", item_escolhido.nome_item)
        op = self.__tela_sistema.opcoes_itens()
        if op == 1:
            heroi.hp_extra = item_escolhido.hp_extra
            heroi.ataque = item_escolhido.att_extra
            print(heroi.ataque)
            print(heroi.hp_extra)
        elif op == 2:
            heroi.mochila.itens.remove(item_escolhido)
            print(item_escolhido, "removido da mochila")

    def descansar(self,heroi):
        heroi.hp = 50 + heroi.hp_extra
        return heroi.hp

    def ver_status(self,heroi):
        self.__tela_sistema.status_heroi(heroi)
