from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario
from entidades.heroi import Heroi
from controladores.controlador_heroi import ControladorHeroi


class ControladorUsuario:

    def __init__(self):
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = []
        self.__manter_tela = True
        self.__controlador_heroi = ControladorHeroi

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

    def opcoes_jogo(self, usuario):
        switcher = {0: self.retornar, 2: self.criar_novo_heroi, 1: self.acessar_herois_criados, 3: self.excluir}

        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_usuario.mostrar_opcoes_jogo()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida(usuario)

    def retornar(self):
        self.__manter_tela = False

#   eu decidi diferenciar as telas de usuarios logados e não logados.
#   Não faz sentido tu poder excluir ou sair de uma conta que voce nem logou.
 #   def abre_tela_usuarios_nao_logados(self):
 #       lista_opcoes = {1: self.cadastrar, 2: self.logar, 0: self.retornar}


 #       while True:
 #           opcao_escolhida = self.__tela_usuario.tela_usuario_nao_logados()
 #           funcao_escolhida = lista_opcoes[opcao_escolhida]
 #           funcao_escolhida()


#   essa nova parte que criei para visualização apenas de pessoas logadas pode ser movida para controle
#   heroi ou controle sistema, conversaremos sobre isso:
    def acessar_herois_criados(self,usuario):
        stacker = 0
        for heroi in usuario.lista_herois:
            print("Selecione", stacker, "para jogar com ", heroi.nome)
            stacker += 1
        escolha = int(input("Escolha o herói: "))
        heroi_escolhido = usuario.lista_herois[escolha]
        self.__controlador_heroi(heroi_escolhido).abrir_tela_opcoes()


    def criar_novo_heroi(self, usuario):
        nome_heroi = self.__tela_usuario.criar_heroi()
        if usuario.lista_herois is not None:
            for heroi in usuario.lista_herois:
                if heroi.nome == nome_heroi:
                    self.__tela_usuario.mensagem("Heroi já existente")
                    return None
            else:
                heroi_novo = Heroi(nome_heroi)
                usuario.lista_herois.append(heroi_novo)
                self.__tela_usuario.mensagem("Heroi criado")
                return heroi_novo
        else:
            heroi_novo = Heroi(nome_heroi)
            usuario.lista_herois.append(heroi_novo)
            self.__tela_usuario.mensagem("Heroi criado")
            return heroi_novo




    # basicamente, o "return login, senha na função logar() serve para ser usado em outros casos que precisamos
    # saber sobre quem está logado! Foi uma sacada minha e pode facilitar mto a nossa vida
    # Dentro dessa função excluir (que precisa ser feita após o logar, então não consegui testar direito,
    # novamente) está uma invocação da função logar, tipo: prove que é vc mesmo nessa conta, por medida de
    # segurança, dai eu puxo os dados, busco na lista de usuarios e excluo ele da lista.

    def excluir(self):
        pass

    #   tela que aparece quando o usuário completa o login em controle usuario, na função logar()
    #def abre_tela_logados(self):
    #    lista_opcoes_logados = {1: self.acessar_herois_criados, 2: self.criar_novo_heroi, 3: self.sair,
    #                            4: self.excluir, 0: self.retornar}
    #    while True:
    #        opcao = self.__tela_usuario.tela_logados()
    #        funcao_escolhida = lista_opcoes_logados[opcao]
    #        funcao_escolhida()
    #    opcao_escolhida_deletar = self.__tela_usuario.tela_deletar_usuario()
    #    if opcao_escolhida_deletar is 1:
    #        self.confirmar_credenciais()
    #    else:
    #        self.__controlador_sistema.abre_tela_logados()

  #  def confirmar_credenciais(self):
  #      while True:
  #          login, senha = self.__tela_usuario.tela_login()
  #          for usuarios in self.__usuarios:
  #              if login == usuarios.login and senha == usuarios.senha:
  #                  self.__usuarios.remove(usuarios)
  #                  self.__tela_usuario.mensagem("Exclusão Concluída com Êxito!")
  #                  self.__tela_usuario.mensagem("-----------------------------")
  #                  self.__tela_usuario.mensagem("Você Será Redirecionado para o Menu Principal")
  #                  self.__controlador_sistema.abre_tela_nao_logados()
  #          else:
  #              self.__tela_usuario.mensagem("Credenciais Incorretas!")
  #              self.__controlador_sistema.abre_tela_logados()
  #              return None
