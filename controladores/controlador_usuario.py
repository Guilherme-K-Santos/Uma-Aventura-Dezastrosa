from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = []

    def cadastrar(self):
        login, senha = self.__tela_usuario.mostra_tela_cadastro()

        for usuario in self.__usuarios:
            if login == usuario.login or senha == usuario.senha:
                self.__tela_usuario.mensagem("Usuário já existente! Faça o login para jogar")
                return None
        else:
            novo_usuario = Usuario(login, senha)
            self.__usuarios.append(novo_usuario)
            self.__tela_usuario.mensagem("Usuário Novo Criado! Faça o login para jogar")
            return novo_usuario

#   comparei login e senha para logar o usuario, mas não consegui saber como linkar ele com os heróis dele,
#   precisaria de um cadastro para isso. Também não consegui instanciar e ter certeza pq n tem nada cadastrado
#   ASKASKSAKSAK, mas tudo indica que ta funfando sim.
    def logar(self):
        while True:
            print("passou aqui")
            login, senha = self.__tela_usuario.tela_login()
            for usuarios in self.__usuarios:
                if login == usuarios.login and senha == usuarios.senha:
                    self.__tela_usuario.tela_logados()
                    return login, senha
            else:
                self.__tela_usuario.mensagem("Login Inválido!")
                self.__tela_usuario.tela_usuario_nao_logados()
                return None

    def retornar(self):
        self.__controlador_sistema.abre_tela_nao_logados()

#   eu decidi diferenciar as telas de usuarios logados e não logados.
#   Não faz sentido tu poder excluir ou sair de uma conta que voce nem logou.
    def abre_tela_usuarios_nao_logados(self):
        lista_opcoes = {1: self.cadastrar, 2: self.logar, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_usuario.tela_usuario_nao_logados()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

# ---------------------------------------------------------------------------------------------------------
#   essa nova parte que criei para visualização apenas de pessoas logadas pode ser movida para controle
#   heroi ou controle sistema, conversaremos sobre isso:
    def acessar_herois_criados(self):
        pass

    def criar_novo_heroi(self):
        pass

    #   criei essa função, para o usuário poder deslogar sem ter que rebootar o sistema
    def sair(self):
        pass

    # basicamente, o "return login, senha na função logar() serve para ser usado em outros casos que precisamos
    # saber sobre quem está logado! Foi uma sacada minha e pode facilitar mto a nossa vida
    # Dentro dessa função excluir (que precisa ser feita após o logar, então não consegui testar direito,
    # novamente) está uma invocação da função logar, tipo: prove que é vc mesmo nessa conta, por medida de
    # segurança, dai eu puxo os dados, busco na lista de usuarios e excluo ele da lista.
    def excluir(self):
        opcao_escolhida_deletar = self.__tela_usuario.tela_deletar_usuario()
        if opcao_escolhida_deletar is 1:
            login, senha = self.logar()
            for usuarios in self.__usuarios:
                if login == usuarios.login and senha == usuarios.senha:
                    self.__usuarios.remove(usuarios)

    #   tela que aparece quando o usuário completa o login em controle usuario, na função logar()
    def abre_tela_logados(self):
        lista_opcoes_logados = {1: self.acessar_herois_criados, 2: self.criar_novo_heroi, 3: self.sair,
                                4: self.excluir, 0: self.retornar}
        while True:
            opcao = self.__tela_usuario.tela_logados()
            funcao_escolhida = lista_opcoes_logados[opcao]
            funcao_escolhida()
