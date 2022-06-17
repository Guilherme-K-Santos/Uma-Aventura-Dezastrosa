

class TelaUsuario:
    def mensagem(self, texto):
        return print(texto)

    #def tela_usuario_nao_logados(self):
    #    print("--------------------------------------")
    #    print("Menu de Usuários")
    #    print("1 - Cadastrar Novo Usuário")
    #    print("2 - Logar Na Conta")
    #    print("0 - Retornar ao Menu Principal")
    #    print("--------------------------------------")

    #    opcao_escolhida = int(input("Opção Seleciona: "))
    #    return opcao_escolhida

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


 #   def tela_deletar_usuario(self):
 #       print("--------------------------------------")
 #       print("Tem certeza que deseja apagar a conta 'nome_do_heroi' com 'numeors_de_herois' "
 #             "heróis salvos ?")
 #       print("1 - Sim")
 #       print("2 - Não")

 #       opcao_escolhida_deletar = int(input("Opção Seleciona: "))
 #       return opcao_escolhida_deletar

    def mostrar_opcoes_usuario(self):
        print("--------------------------------------")
        print("Login efetuado com sucesso!")
        print("Qual a aventura que embarcaremos?")
        print("1 - Acessar Heróis já Criados")
        print("2 - Criar Novo Herói")
        print("3 - Excluir Conta")
        print("0 - Retornar")
        print("--------------------------------------")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def criar_heroi(self):
        print("====CRIAR NOVO HEROI====")
        nome = input("Dê um nome ao seu herói (deve ser diferente dos demais herois): ")
        return nome
