

class TelaSistema:
    def mensagem(self, texto):
        return print(texto)

    def tela_inicial(self):
        print("--------------------------------------")
        print("Bem-Vindo ao Menu Principal, Jogador!")
        print("O que você deseja fazer para prosseguir?")
        print("1 - Login de Usuário")
        print("2 - Cadastro de Usuário")
        print("3 - Sobre o jogo")
        print("0 - Encerrar o jogo")
        print("--------------------------------------")

        opcao_escolhida = self.excecoes_escolha("Escolha uma Opção ", [1, 2, 3, 0])
        return opcao_escolhida

    def tela_logados(self, usuario):
        print("---------------Ola!", usuario.login, "-----------------------")
        print("Login efetuado com sucesso!")
        print("Qual a aventura que embarcaremos?")
        print("1 - Acessar Hérois Criados")
        print("2 - Criar Novo Herói")
        print("3 - Opções da Conta")
        print("0 - Retornar")
        print("--------------------------------------")

        opcao_escolhida = self.excecoes_escolha("Escolha uma Opção ", [1, 2, 3, 0])
        return opcao_escolhida

#         opções para o usuário escolher (ele agora está LOGADO, então pode prosseguir
#         para acessar ou criar heróis), essa tela pode ser colocada em tela sistema também,
#         conversamos depois

    def informacoes_jogo(self):
        print("---------------Ola Jogador!---------------")
        print("Aqui será explicado um pouco sobre o nosso RPG!")
        input()
        print("Para começo, você deve criar a sua conta e logar!")
        input()
        print("Após isso, crie um herói com o nome que você quiser e embarque")
        print("na sua jornada épica, tomara que ela não seja dezastrosa!")
        input()
        print("Bom jogo!")

    def tela_opcoes_jogo(self, heroi):
        print("----------- Você está jogando com ", heroi.nome, heroi.titulo, " -----------")
        print("1 - Atacar monstro")
        print("2 - Abrir mochila")
        print("3 - Descansar")
        print("4 - Ver status do herói")
        print("5 - Selecionar título para o herói")
        print("0 - Retornar")
        opcao = self.excecoes_escolha("Escolha uma Opção ", [1, 2, 3, 4, 5, 0])
        return opcao

    def status_heroi(self, heroi):
        print("------ STATUS DE ", heroi.nome, " ------")
        print("Vida: ", heroi.hp_total)
        print("Ataque: ", heroi.ataque)
        print("Título atual: ", heroi.titulo)
        print("Títulos: ", heroi.lista_titulos)

    def escolhe_titulo(self, validacao):
        titulo_escolhido = self.excecoes_escolha("Escolha uma Opção ", validacao)
        return titulo_escolhido

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
