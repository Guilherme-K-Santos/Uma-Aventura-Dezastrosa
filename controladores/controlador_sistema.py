from controladores.controlador_heroi import ControladorHeroi
from controladores.controlador_monstro import ControladorMonstro
from controladores.controlador_usuario import ControladorUsuario
from telas.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
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
                self.__tela_sistema.informacoes_jogo()
            elif opcao == 0:
                exit()

    def cadastro_heroi(self):
        novo_heroi = self.__controlador_heroi.criar_heroi()
        lista_usuarios = self.__controlador_usuario.pega_usuario_por_heroi()

        for usuario in lista_usuarios:
            if novo_heroi.nome in usuario.lista_nomes_herois:
                self.__tela_sistema.mensagem("Heroi já existente")
                return None
            else:
                if novo_heroi not in usuario.lista_herois:
                    usuario.lista_herois.append(novo_heroi)
                    usuario.lista_nomes_herois.append(novo_heroi.nome)

    def combate(self, heroi, usuario):
        monstro = self.__controlador_monstro.pega_monstro()
        if monstro is not None:
            if heroi.ataque >= monstro.hp and heroi.hp_total > monstro.ataque:
                heroi.mochila.itens.append(monstro.item_monstro)
                heroi.lista_titulos.append(monstro.titulo)

                heroi.hp_total = heroi.hp_total - monstro.ataque
                self.__controlador_monstro.remove(monstro)

                self.__tela_sistema.mensagem("Parabéns! Você matou o monstro!")
                self.__tela_sistema.mensagem("Um novo item apareceu em sua mochila")
                self.__tela_sistema.mensagem("Equipe-o para o próximo combate")
                self.__tela_sistema.mensagem("Lembre-se de descansar de sua última batalha")

                return self.abrir_tela_opcoes_jogo(heroi, usuario)
            else:
                self.__tela_sistema.mensagem("GAME OVER")
                self.__tela_sistema.mensagem("Seu herói morreu, crie outro herói")
                self.__tela_sistema.mensagem("Foi uma aventura dezastrosa! >:(")
                self.__controlador_usuario.remove_heroi(heroi, usuario)
                input("Aperte ENTER para retornar")

                return self.abrir_tela_logados(usuario)
        else:
            self.__tela_sistema.mensagem("O mundo foi salvo! Todos os monstros foram derrotados :D")
            self.__tela_sistema.mensagem("Obrigada grande herói!")
            input("Aperte ENTER para retornar")

            self.abrir_tela_opcoes_jogo(heroi, usuario)

    def abrir_tela_logados(self, usuario):
        opcao2 = self.__tela_sistema.tela_logados(usuario)
        if opcao2 == 1:
            heroi = self.__controlador_usuario.acessar_herois(usuario)
            if heroi is not None:
                self.abrir_tela_opcoes_jogo(heroi, usuario)
            else:
                self.abrir_tela_logados(usuario)
        elif opcao2 == 2:
            self.cadastro_heroi()
            self.abrir_tela_logados(usuario)
        elif opcao2 == 3:
            self.__controlador_usuario.opcoes_usuario()
            self.abrir_tela_logados(usuario)

    def abrir_tela_opcoes_jogo(self, heroi, usuario):
        opcao3 = self.__tela_sistema.tela_opcoes_jogo(heroi)
        while opcao3 != 0:
            if opcao3 == 1:
                self.combate(heroi, usuario)
            elif opcao3 == 2:
                self.abre_mochila(heroi, usuario)
            elif opcao3 == 3:
                self.descansar(heroi)
            elif opcao3 == 4:
                self.ver_status(heroi)
            elif opcao3 == 5:
                self.mudar_titulo(heroi)
            opcao3 = self.__tela_sistema.tela_opcoes_jogo(heroi)

    def abre_mochila(self, heroi, usuario):
        self.__tela_sistema.mensagem("-----MOCHILA----")
        if len(heroi.mochila.itens) > 0:
            indice = 0
            for item in heroi.mochila.itens:
                print(indice, "-", item.nome_item)
                indice += 1

            validacao = self.regularizacao(indice)

            indice_item = self.__tela_sistema.escolhe_itens(validacao)
            item_escolhido = heroi.mochila.itens[indice_item]

            print("Você escolheu: ", item_escolhido.nome_item)

            op = self.__tela_sistema.opcoes_itens()
            if op == 1:
                self.__tela_sistema.mensagem(" ================================== ")
                if heroi.item_equipado != item_escolhido:
                    heroi.item_equipado = item_escolhido
                    heroi.hp_extra = item_escolhido.hp_extra
                    heroi.ataque = item_escolhido.att_extra
                    self.__tela_sistema.mensagem(" === Item equipado com sucesso! === ")
                    print("Ataque atual: ", heroi.ataque)
                    print("HP atual: ", heroi.hp_total)
                    input("Aperte ENTER para retornar")
                else:
                    self.__tela_sistema.mensagem("=======================")
                    self.__tela_sistema.mensagem("== Item já equipado! ==")
                    input("Aperte ENTER para retornar")

            elif op == 2:
                self.__tela_sistema.mensagem("=====================")
                if heroi.item_equipado == item_escolhido:
                    heroi.hp_extra = 0
                    heroi.ataque = 0
                    self.__tela_sistema.mensagem("O item foi desequipado")
                heroi.mochila.itens.remove(item_escolhido)
                print(item_escolhido.nome_item, "foi removido da mochila")
                input("Aperte ENTER para retornar")

            elif op == 3:
                self.__tela_sistema.mensagem("=====================")
                if heroi.item_equipado is not None:
                    heroi.item_equipado = None
                    heroi.hp_extra = 0
                    heroi.ataque = 0
                    self.__tela_sistema.mensagem("O item foi desequipado")
                    print("Vida atual: ", heroi.hp_total)
                    print("Ataque atual: ", heroi.ataque)
                else:
                    self.__tela_sistema.mensagem("Nenhum item equipado")
                input("Aperte ENTER para retornar")

            elif op == 0:
                return self.abrir_tela_opcoes_jogo(heroi, usuario)

        else:
            self.__tela_sistema.mensagem("Mochila vazia")
            input("Aperte ENTER para retornar")
            return self.abrir_tela_opcoes_jogo(heroi, usuario)

    def regularizacao(self, indice):
        validacao = []
        contador = 0
        for _ in range(indice):
            validacao.append(contador)
            contador += 1
        return validacao

    def descansar(self, heroi):
        heroi.hp_total = heroi.hp + heroi.hp_extra

        self.__tela_sistema.mensagem("Sua vida foi totalmente regenerada!")

        return heroi.hp_total

    def ver_status(self, heroi):
        self.__tela_sistema.status_heroi(heroi)

    def mudar_titulo(self, heroi):
        indice = 0
        for titulo in heroi.lista_titulos:
            print("Selecione ", indice, "para equipar: ", titulo)
            indice += 1

        validacao = self.regularizacao(indice)

        indice_escolhido = self.__tela_sistema.escolhe_titulo(validacao)
        heroi.titulo = heroi.lista_titulos[indice_escolhido]

        self.__tela_sistema.mensagem(heroi.titulo)
