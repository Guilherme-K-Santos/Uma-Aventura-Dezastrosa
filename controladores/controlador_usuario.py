from entidades.usuario import Usuario
from telas.tela_usuario import TelaUsuario


class ControladorUsuario:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = []
        self.__manter_tela = True

# ------------------------------------------USUARIO---------------------------------------------------

    def cadastrar(self):
        dados_novos = self.__tela_usuario.tela_cadastro()

        for usuario in self.__usuarios:
            if (usuario.login == dados_novos["login"]) and \
                    usuario.senha == dados_novos["senha"]:
                self.__tela_usuario.mensagem("Usuário já existente! Faça o login para jogar")
                return None
        else:
            novo_usuario = Usuario(dados_novos["login"], dados_novos["senha"])
            self.__usuarios.append(novo_usuario)
            self.__tela_usuario.mensagem("Usuário Novo Criado! Faça o login para jogar")
            return novo_usuario

    def logar(self):
        dados = self.__tela_usuario.tela_login()

        for usuario in self.__usuarios:
            if (usuario.login == dados["login"]) and \
                    (usuario.senha == dados["senha"]):
                self.__tela_usuario.mensagem("Logado com Sucesso!")
                return usuario
        else:
            self.__tela_usuario.mensagem("Nome ou Senha invalidos!")
            return None

    def opcoes_usuario(self):
        switcher = {1: self.alterar, 2: self.excluir, 0: self.retornar}

        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_usuario.mostrar_opcoes_usuario()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()

    def alterar(self):
        resposta_alteracao = self.__tela_usuario.tela_confirmar_alteraracao()
        self.__tela_usuario.mensagem("Por favor, confirme que é você mesmo: ")
        credenciais = self.__tela_usuario.tela_login()

        if resposta_alteracao == 1:
            for usuario_login_novo in self.__usuarios:
                if (usuario_login_novo.login == credenciais["login"]) and \
                        usuario_login_novo.senha == credenciais["senha"]:
                    print(usuario_login_novo.login)
                    usuario_login_novo.login = self.__tela_usuario.tela_alteracao_login()
                    break
            else:
                self.__tela_usuario.mensagem("Credenciais Incorretas!")

        elif resposta_alteracao == 2:
            for usuario_senha_nova in self.__usuarios:
                if (usuario_senha_nova.login == credenciais["login"]) and \
                        usuario_senha_nova.senha == credenciais["senha"]:
                    usuario_senha_nova.senha = self.__tela_usuario.tela_alteracao_senha()
                    break
            else:
                self.__tela_usuario.mensagem("Credenciais Incorretas!")

    def excluir(self):
            credenciais = self.__tela_usuario.tela_login()

            for usuario in self.__usuarios:
                if (usuario.login == credenciais["login"]) and \
                        usuario.senha == credenciais["senha"]:
                    resposta = self.__tela_usuario.tela_deletar_usuario()

                    if resposta == 1:
                        self.__usuarios.remove(usuario)
                        self.__tela_usuario.mensagem("Exclusão Concluída com Êxito!")
                        self.__tela_usuario.mensagem("-----------------------------")
                        self.__tela_usuario.mensagem("Você Será Redirecionado para o Menu Principal")
                        return self.__controlador_sistema.iniciar()
                    else:
                        self.__tela_usuario.mensagem("Credenciais Incorretas!")
                        return None

    def retornar(self):
        self.__manter_tela = False

#   ------------------------------------USUÁRIO X HERÓI---------------------------------------------------
#   aqui eu pego a lista de todos os usuarios atualmente cadastrados e exporto para o controlador sistema

    def pega_usuario_por_heroi(self):
        lista_usuarios = self.__usuarios

        return lista_usuarios

#   ele abre uma tela de seleção que responde com o nome do heroi q o usuario quer jogar
#   depois eu tentei fazer um sistema de contagem para printar para o usuario os herois q ele tem.
#   Para isso, usei o contador_herois, é MUITO útil. Depois tem um for para selecionar o herói especifico e
#   abrir a tela da jornada salva dele (precisamos fazer)

    def acessar_herois(self, usuario):
        self.__tela_usuario.mensagem("Olá Aventureiro! Em qual jornada você quer prosseguir?")
        self.__tela_usuario.mensagem("")

        contador_herois = 0
        for k in usuario.lista_nomes_herois:
            self.__tela_usuario.mensagem(usuario.lista_nomes_herois[contador_herois])
            contador_herois += 1
        heroi_escolhido = self.__tela_usuario.abrir_selecao_herois()

        for herois in usuario.lista_herois:
            if herois.nome == heroi_escolhido:
                self.__tela_usuario.abre_tela_jornada_especifica()
