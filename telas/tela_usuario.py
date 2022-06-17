

class TelaUsuario:
    def mensagem(self, texto):
        return print(texto)

    def tela_login(self):
        print("--------------------------------------")
        print("Por favor, preencha com seus dados:")
        login = input("Login:")
        senha = input("Senha:")

        return {"login": login, "senha": senha}

    def tela_cadastro(self):
        print("--------------------------------------")
        print("--------------CADASTRO----------------")
        login = input("Login:")
        senha = input("Senha:")

        return {"login": login, "senha": senha}

    def mostrar_opcoes_usuario(self):
        print("--------------------------------------")
        print("--------------Opções Do Usuário----------------")
        print("1 - Alterar Dados da Conta")
        print("2 - Excluir Conta")
        print("0 - Retornar")
        print("--------------------------------------")

        opcao_escolhida = int(input("Escolha a opcao: "))
        return opcao_escolhida

    def tela_deletar_usuario(self):
        print("--------------------------------------")
        print("Tem certeza que deseja apagar a conta 'nome_do_heroi' com 'numeors_de_herois' "
            "heróis salvos ?")
        print("1 - Sim")
        print("2 - Não")

        opcao_escolhida_deletar = int(input("Opção Seleciona: "))
        return opcao_escolhida_deletar
