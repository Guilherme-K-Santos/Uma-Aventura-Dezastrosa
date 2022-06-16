

class TelaUsuario:
    def mensagem(self, texto):
        return print(texto)

    def tela_usuario_nao_logados(self):
        print("--------------------------------------")
        print("Menu de Usuários")
        print("1 - Cadastrar Novo Usuário")
        print("2 - Logar Na Conta")
        print("0 - Retornar ao Menu Principal")
        print("--------------------------------------")

        opcao_escolhida = int(input("Opção Seleciona: "))
        return opcao_escolhida

    def mostra_tela_cadastro(self):
        print("--------------------------------------")
        print("--------------CADASTRO----------------")
        login = input("Login:")
        senha = int(input("Senha:"))

        return login, senha

    def tela_login(self):
        print("--------------------------------------")
        print("Por favor, preencha com seus dados:")
        login = input("Login:")
        senha = int(input("Senha:"))

        return login, senha

    def tela_deletar_usuario(self):
        print("--------------------------------------")
        print("Tem certeza que deseja apagar a conta 'nome_do_heroi' com 'numeors_de_herois' "
              "heróis salvos ?")
        print("1 - Sim")
        print("2 - Não")

        opcao_escolhida_deletar = int(input("Opção Seleciona: "))
        return opcao_escolhida_deletar
