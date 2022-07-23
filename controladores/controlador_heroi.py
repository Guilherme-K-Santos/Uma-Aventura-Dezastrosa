from telas.tela_heroi import TelaHeroi
from entidades.heroi import Heroi
from persistencia.heroiDAO import HeroiDAO


class ControladorHeroi:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_heroi = TelaHeroi()
        self.__manter_tela = True
        self.__heroi_dao = HeroiDAO()

    def criar_heroi(self):
        nome = self.__tela_heroi.abrir_pegar_nome_heroi()
        print(nome)
        novo_heroi = Heroi(nome, 50, 10, "o(a) Noob")
        self.__tela_heroi.mostrar_mensagem("Herói criado!")
        self.__heroi_dao.add(nome, novo_heroi)
        return novo_heroi

    def combate(self, heroi, usuario):
        monstro = self.__controlador_sistema.controlador_monstro.pega_monstro()
        if monstro is not None:
            if heroi.ataque >= monstro.hp and heroi.hp_total > monstro.ataque:
                heroi.mochila.itens.append(monstro.item_monstro)
                heroi.lista_titulos.append(monstro.titulo)

                heroi.hp_total = heroi.hp_total - monstro.ataque
                self.__controlador_sistema.controlador_monstro.remove(monstro)

                self.__tela_heroi.mensagem("Parabéns! Você matou o monstro!")
                self.__tela_heroi.mensagem("Um novo item apareceu em sua mochila")
                self.__tela_heroi.mensagem("Equipe-o para o próximo combate")
                self.__tela_heroi.mensagem("ATENÇÃO: Lembre-se de descansar de sua última batalha")

                return self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)
            else:
                self.__tela_heroi.mensagem("GAME OVER")
                self.__tela_heroi.mensagem("Seu herói morreu, crie outro herói")
                self.__tela_heroi.mensagem("Foi uma aventura dezastrosa! >:(")
                self.__controlador_sistema.controlador_usuario.remove_heroi(heroi, usuario)

                return self.__controlador_sistema.abrir_tela_logados(usuario)
        elif monstro == "na":
            self.__tela_heroi.mensagem("O mundo foi salvo! Todos os monstros foram derrotados :D")
            self.__tela_heroi.mensagem("Obrigada grande herói!")

            self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)
        else:
            return None

    def descansar(self, heroi):
        heroi.hp_total = heroi.hp + heroi.hp_extra

        self.__tela_heroi.mostrar_mensagem("Sua vida foi totalmente regenerada!")

        return heroi.hp_total

    def abre_mochila(self, heroi, usuario):
        self.__tela_heroi.mensagem("---- Mochila ----")
        if len(heroi.mochila.itens) > 0:
            indice = 1
            for item in heroi.mochila.itens:
                self.__tela_heroi.mensagem("{} - {}".format(indice, item.nome_item))
                indice += 1

            validacao = self.regularizacao(indice)

            indice_item = self.__tela_heroi.escolhe_itens(validacao)
            if indice_item != 0:
                item_escolhido = heroi.mochila.itens[indice_item-1]

                self.__tela_heroi.mensagem("Você escolheu: {} ".format(item_escolhido.nome_item))

                op = self.__tela_heroi.abrir_opcoes_itens()
                if op == 1:
                    self.__tela_heroi.mensagem(" ================================== ")
                    if heroi.item_equipado != item_escolhido:
                        heroi.item_equipado = item_escolhido
                        heroi.hp_extra = item_escolhido.hp_extra
                        heroi.ataque = item_escolhido.att_extra
                        self.__tela_heroi.mensagem(" === Item equipado com sucesso! === ")
                        self.__tela_heroi.mensagem("Ataque atual: {} ".format(heroi.ataque))
                        self.__tela_heroi.mensagem("HP atual: {} ".format(heroi.hp_total))
                    else:
                        self.__tela_heroi.mensagem(" ================================== ")
                        self.__tela_heroi.mensagem(" ======== Item já equipado! ======= ")

                elif op == 2:
                    self.__tela_heroi.mensagem(" =================================== ")
                    if heroi.item_equipado == item_escolhido:
                        heroi.hp_extra = 0
                        heroi.ataque = 0
                        self.__tela_heroi.mensagem(" ===== O item foi desequipado ====== ")
                    heroi.mochila.itens.remove(item_escolhido)
                    self.__tela_heroi.mensagem("{} foi removido da mochila".format(item_escolhido.nome_item))

                elif op == 3:
                    self.__tela_heroi.mensagem(" =================================== ")
                    if heroi.item_equipado is not None:
                        heroi.item_equipado = None
                        heroi.hp_extra = 0
                        heroi.ataque = 0
                        self.__tela_heroi.mensagem(" ===== O item foi desequipado ====== ")
                        self.__tela_heroi.mensagem("Ataque atual: {} ".format(heroi.ataque))
                        self.__tela_heroi.mensagem("HP atual: {} ".format(heroi.hp_total))
                    else:
                        self.__tela_heroi.mensagem(" ====== Nenhum item equipado ======= ")

                elif op == 0:
                    return self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)
            else:
                return self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)
        else:
            self.__tela_heroi.mensagem(" ========= Mochila vazia ========= ")
            return self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)

    def ver_status(self, heroi):
        self.__tela_heroi.abrir_status_heroi(heroi)

    def mudar_titulo(self, heroi):
        indice = 0
        for titulo in heroi.lista_titulos:
            print("Selecione ", indice, "para equipar: ", titulo)
            indice += 1

        validacao = self.regularizacao(indice)

        indice_escolhido = self.__tela_heroi.escolhe_titulo(validacao)
        heroi.titulo = heroi.lista_titulos[indice_escolhido]

        self.__tela_heroi.mensagem("Título {} equipado com sucesso".format(heroi.titulo))

    def regularizacao(self, indice):
        validacao = []
        contador = 0
        for _ in range(indice):
            validacao.append(contador)
            contador += 1
        return validacao

    def retornar(self):
        self.__manter_tela = False
