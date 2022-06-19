

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
