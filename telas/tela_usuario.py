class TelaUsuario:
    def mensagem(self, texto):
        return print(texto)

    #   -------------------------------------- OPÇÕES DO USUÁRIO --------------------------------------

    def tela_cadastro(self):
        print("--------------------------------------")
        print("--------------CADASTRO----------------")
        login = input("Login:")
        senha = self.excecoes_escrita_numerica("Senha:")

        return {"login": login, "senha": senha}

    def tela_login(self):
        print("--------------------------------------")
        print("Por favor, preencha com seus dados:")
        login = input("Login:")
        senha = self.excecoes_escrita_numerica("Senha:")

        return {"login": login, "senha": senha}

    def mostrar_opcoes_usuario(self):
        print("--------------------------------------")
        print("--------------Opções Do Usuário----------------")
        print("1 - Alterar Dados da Conta")
        print("2 - Excluir Conta")
        print("0 - Retornar")
        print("--------------------------------------")

        opcao_escolhida = self.excecoes_escolha("Escolha uma Opção ", [1, 2, 0])
        return opcao_escolhida

    def tela_confirmar_alteraracao(self):
        print("--------------------------------------")
        print("O que você deseja alterar em sua conta?")
        print("1 - Login")
        print("2 - Senha")

        resposta_alteracao = self.excecoes_escolha("Escolha uma Opção ", [1, 2])
        return resposta_alteracao

    def tela_alteracao_login(self):
        print("--------------------------------------")
        print("Qual será o seu novo login?")
        login = input("Login:")

        return login

    def tela_alteracao_senha(self):
        print("--------------------------------------")
        print("Qual será sua nova senha?")
        senha = self.excecoes_escrita_numerica("Senha:")

        return senha

    def tela_deletar_usuario(self, usuario):
        print("--------------------------------------")
        print("Tem certeza que deseja apagar a conta?")
        print("1 - Sim")
        print("2 - Não")

        opcao_escolhida_deletar = self.excecoes_escolha("Escolha uma Opção ", [1, 2])
        return opcao_escolhida_deletar

    #   -------------------------------------- OPÇÕES USUARIO X HEROI --------------------------------------

    def abrir_selecao_herois(self):
        print()
        print("--------------------------------------")
        print("Escreva abaixo o nome do herói que você deseja usar.")

        heroi_escolhido = input("Herói Escolhido: ")
        return heroi_escolhido

    def excecoes_escrita_numerica(self, mensagem: ""):
        while True:
            valor = input(mensagem)
            try:
                valor_comparativo = int(valor)
                return valor_comparativo
            except ValueError:
                print("Por favor, coloque um valor númerico!")

    def excecoes_escolha(self, mensagem: "", numeros_validos: [] = None):
        while True:
            resposta_usuario = input(mensagem)
            try:
                numero = int(resposta_usuario)
                if numero not in numeros_validos:
                    raise ValueError
                return numero
            except ValueError:
                print("Por favor, digite uma das opções:")
