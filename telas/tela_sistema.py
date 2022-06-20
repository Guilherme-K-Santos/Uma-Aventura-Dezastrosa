

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

        opcao_escolhida = int(input("Escolha a opcao: "))
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

        opcao_escolhida = int(input("Escolha a opcao: "))
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

    def tela_opcoes_jogo(self,heroi):
        print("----------- Você está jogando com ", heroi.nome, heroi.titulo, " -----------")
        print("1 - Atacar monstro")
        print("2 - Abrir mochila")
        print("3 - Descansar")
        print("4 - Ver status do herói")
        print("5 - Selecionar título para o herói")
        print("0 - Retornar")
        opcao = int(input("Digite uma opção: "))
        return opcao

    def escolhe_itens(self):
        print("Escolha um item para equipar ou deletar")
        item = int(input("Digite o número do item: "))
        return item

    def opcoes_itens(self):
        print(" 1 - Equipar")
        print(" 2 - Deletar")
        print(" 0 - Retornar")
        opcao = int(input("Digite uma opção: "))
        return opcao

    def status_heroi(self,heroi):
        print("------ STATUS DE ", heroi, " ------")
        print("Vida: ", heroi.hp)
        print("Ataque: ", heroi.ataque)
        print("Título atual: ", heroi.titulo)
        print("Títulos: ", heroi.lista_titulos)