

class TelaUsuario:
    def mensagem(self, texto):
        return print(texto)

    def tela_cadastro(self):
        print("--------------------------------------")
        print("--------------CADASTRO----------------")
        login = input("Login:")
        senha = input("Senha:")

        return {"login": login, "senha": senha}

    def tela_login(self):
        print("--------------------------------------")
        print("Por favor, preencha com seus dados:")
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

    def tela_alterar_usuario(self):
        print("--------------------------------------")
        print("O que você deseja alterar em sua conta?")
        print("1 - Login")
        print("2 - Senha")

        resposta_alteracao = int(input("Opção Seleciona: "))
        return resposta_alteracao

    def tela_alterar_login(self):
        print("--------------------------------------")
        print("Qual será o seu novo login?")

        login = input("Novo Login: ")

        return {"Novo Login: ": login}

    def tela_alterar_senha(self):
        print("--------------------------------------")
        print("Qual será o seu nova senha?")

        senha = int(input("Nova Senha: "))

        return {"Nova Senha: ": senha}


    def tela_deletar_usuario(self):
        print("--------------------------------------")
        print("Tem certeza que deseja apagar a conta 'nome_do_heroi' com 'numeors_de_herois' "
            "heróis salvos ?")
        print("1 - Sim")
        print("2 - Não")

        opcao_escolhida_deletar = int(input("Opção Seleciona: "))
        return opcao_escolhida_deletar
