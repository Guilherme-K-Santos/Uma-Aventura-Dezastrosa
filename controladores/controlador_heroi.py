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
        advice = 'Herói Criado!'
        return novo_heroi, advice

    def combate(self, heroi, usuario):
        antigo_heroi = heroi
        monstro = self.__controlador_sistema.controlador_monstro.pega_monstro()
        if monstro is not None:
            if heroi.ataque >= monstro.hp and heroi.hp_total > monstro.ataque:
                heroi.mochila.itens.append(monstro.item_monstro)
                heroi.lista_titulos.append(monstro.titulo)

                heroi.hp_total = heroi.hp_total - monstro.ataque
                self.__controlador_sistema.controlador_monstro.remove(monstro)

                self.__heroi_dao.update_key(antigo_heroi.nome, heroi.nome, heroi)

                ok = self.__tela_heroi.abrir_depois_matar_monstro()
                if ok is not None:
                    return self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)
            else:
                ok = self.__tela_heroi.abrir_depois_morrer()
                if ok is not None:
                    self.__controlador_sistema.controlador_usuario.remove_heroi(heroi, usuario)
                    self.__heroi_dao.remove(heroi.nome)
                    return self.__controlador_sistema.abrir_tela_logados(usuario)
        else:
            return None

    def descansar(self, heroi):
        antigo_heroi = heroi
        heroi.hp_total = heroi.hp + heroi.hp_extra

        self.__heroi_dao.update_key(antigo_heroi.nome, heroi.nome, heroi)
        self.__tela_heroi.mostrar_mensagem("Sua vida foi totalmente regenerada!")

        return heroi.hp_total

    def abre_mochila(self, heroi, usuario):
        antigo_heroi = heroi
        nomes_itens = []
        if len(heroi.mochila.itens) > 0:
            for item in heroi.mochila.itens:
                nomes_itens.append(item.nome_item)
            nomes = tuple(nomes_itens)
            nome_item = self.__tela_heroi.escolhe_item(nomes)
            item_escolhido = ""

            if nome_item != 0:
                for i in heroi.mochila.itens:
                    if i.nome_item == nome_item:
                        item_escolhido = i

                self.__tela_heroi.mostrar_mensagem("Você escolheu: {} ".format(item_escolhido.nome_item))

                op = self.__tela_heroi.abrir_opcoes_itens()
                if op == 1:
                    if heroi.item_equipado != item_escolhido:
                        heroi.item_equipado = item_escolhido
                        heroi.hp_extra = item_escolhido.hp_extra
                        heroi.ataque = item_escolhido.att_extra
                        self.__heroi_dao.update_key(antigo_heroi.nome, heroi.nome, heroi)
                        self.__tela_heroi.mostrar_mensagem("Item equipado com sucesso!")
                        self.__tela_heroi.mostrar_mensagem("Ataque atual: {} \n HP atual: {} ".format(heroi.ataque,
                                                                                                      heroi.hp_total))
                    else:
                        self.__tela_heroi.mostrar_mensagem("Item já equipado!")

                elif op == 2:
                    if heroi.item_equipado == item_escolhido:
                        heroi.hp_extra = 0
                        heroi.ataque = 0
                        self.__tela_heroi.mostrar_mensagem("O item foi desequipado")
                    heroi.mochila.itens.remove(item_escolhido)
                    self.__heroi_dao.update_key(antigo_heroi.nome, heroi.nome, heroi)
                    self.__tela_heroi.mostrar_mensagem("{} foi removido da mochila".format(item_escolhido.nome_item))

                elif op == 3:
                    if heroi.item_equipado is not None:
                        heroi.item_equipado = None
                        heroi.hp_extra = 0
                        heroi.ataque = 0
                        self.__tela_heroi.mostrar_mensagem("O item foi desequipado")
                        self.__tela_heroi.mostrar_mensagem("Ataque atual: {} \n HP atual: {} ".format(heroi.ataque,
                                                                                                      heroi.hp_total))
                    else:
                        self.__tela_heroi.mostrar_mensagem("Nenhum item equipado")
                    self.__heroi_dao.update_key(antigo_heroi.nome, heroi.nome, heroi)
                elif op == 0:
                    return self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)
            else:
                return self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)
        else:
            self.__tela_heroi.mostrar_mensagem('Mochila vazia')
            return self.__controlador_sistema.abrir_tela_opcoes_jogo(heroi, usuario)

    def ver_status(self, heroi):
        self.__tela_heroi.abrir_status_heroi(heroi)

    def mudar_titulo(self, heroi):
        antigo_heroi = heroi
        tupla_titulos = tuple(heroi.lista_titulos)
        titulo_escolhido = self.__tela_heroi.escolhe_titulo(tupla_titulos)
        heroi.titulo = titulo_escolhido
        self.__heroi_dao.update_key(antigo_heroi.nome, heroi.nome, heroi)
        self.__tela_heroi.mostrar_mensagem("Título {} equipado com sucesso".format(heroi.titulo))

    def regularizacao(self, indice):
        validacao = []
        contador = 0
        for _ in range(indice):
            validacao.append(contador)
            contador += 1
        return validacao

    def retornar(self):
        self.__manter_tela = False
