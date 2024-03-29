from entidades.usuario import Usuario
from telas.tela_usuario import TelaUsuario
from persistencia.usuarioDAO import UsuarioDAO


class ControladorUsuario:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario()
        self.__usuario_dao = UsuarioDAO()
        self.__manter_tela = True

# ------------------------------------------USUARIO---------------------------------------------------

    def cadastrar(self):
        dados_novos = self.__tela_usuario.abrir_cadastro()

        if dados_novos is None:
            self.retornar()
        elif self.__usuario_dao.get(dados_novos["login"]) is not None:
            self.__tela_usuario.mostrar_mensagem("Usuário já existente! Faça o login para jogar")
            return None
        else:
            novo_usuario = Usuario(dados_novos["login"], dados_novos["senha"])
            self.__usuario_dao.add(novo_usuario.login, novo_usuario)
            self.__tela_usuario.mostrar_mensagem("Usuário Novo Criado! Faça o login para jogar")
            return novo_usuario

    def logar(self):
        dados = self.__tela_usuario.abrir_login()

        if dados is None:
            self.retornar()
        elif self.__usuario_dao.get(dados["login"]) is not None:
            usuario_pego = self.__usuario_dao.get(dados["login"])
            if usuario_pego.senha == dados["senha"]:
                self.__tela_usuario.mostrar_mensagem("Logado com Sucesso!")
                return usuario_pego
            else:
                self.__tela_usuario.mostrar_mensagem("Senha invalida!")
                return None
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário não existente")

    def opcoes_usuario(self):
        switcher = {1: self.alterar, 2: self.excluir, 0: self.retornar}

        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_usuario.mostrar_opcoes_usuario()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()

    def alterar(self):
        credenciais = self.__tela_usuario.abrir_login()

        if credenciais is None:
            self.retornar()
        else:
            usuario_pego = self.__usuario_dao.get(credenciais["login"])
            nome_antigo = usuario_pego.login
            if (usuario_pego is not None) and usuario_pego.senha == credenciais["senha"]:
                dados_novos = self.__tela_usuario.abrir_tela_alteracao(usuario_pego)
                usuario_pego.login = dados_novos["login_novo"]
                usuario_pego.senha = dados_novos["senha_novo"]
                self.__usuario_dao.update_key(nome_antigo, usuario_pego.login, usuario_pego)
            else:
                self.__tela_usuario.mostrar_mensagem("Credenciais Incorretas!")

    def excluir(self):
        credenciais = self.__tela_usuario.abrir_login()

        if credenciais is None:
            self.retornar()
        else:
            usuario_pego = self.__usuario_dao.get(credenciais["login"])

            if usuario_pego is not None and usuario_pego.senha == credenciais["senha"]:
                resposta = self.__tela_usuario.abrir_tela_deletar_usuario()
                if resposta == 1:
                    self.__usuario_dao.remove(usuario_pego.login)
                    self.__tela_usuario.mostrar_mensagem("Exclusão Concluída com Êxito!")
                    return self.__controlador_sistema.iniciar()
                elif resposta == 2:
                    return None
            else:
                self.__tela_usuario.mostrar_mensagem("Credenciais Incorretas!")
                return None

    def retornar(self):
        self.__manter_tela = False

#   ------------------------------------USUÁRIO X HERÓI---------------------------------------------------
#   aqui eu pego a lista de todos os usuarios atualmente cadastrados e exporto para o controlador sistema

    def pega_usuario_por_heroi(self):
        lista_usuarios = self.__usuario_dao.get_all()

        return lista_usuarios

#   ele abre uma tela de seleção que responde com o nome do heroi q o usuario quer jogar
#   depois eu tentei fazer um sistema de contagem para printar para o usuario os herois q ele tem.
#   Para isso, usei o contador_herois, é MUITO útil. Depois tem um for para selecionar o herói especifico e
#   abrir a tela da jornada salva dele (precisamos fazer)

    def acessar_herois(self, usuario):
        if len(usuario.lista_herois) >= 1:
            self.__tela_usuario.mostrar_mensagem("Olá Aventureiro! Em qual jornada você quer prosseguir?")
            nomes = []
            for heroi in usuario.lista_herois:
                nomes.append(heroi.nome)
            tupla = tuple(nomes)
            nome_escolhido = self.__tela_usuario.escolhe_heroi(tupla)

            for heroi in usuario.lista_herois:
                if nome_escolhido == heroi.nome:
                    return heroi
        else:
            return None

    def remove_heroi(self, heroi, usuario):
        usuario.lista_herois.remove(heroi)
        usuario.lista_nomes_herois.remove(heroi.nome)
        return self.__controlador_sistema.abrir_tela_logados(usuario)
