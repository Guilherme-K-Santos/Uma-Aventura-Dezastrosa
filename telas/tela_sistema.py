

class TelaSistema:
    def abre_tela_inicial(self):
        print("--------------------------------------")
        print("Bem-Vindo ao Menu Principal, Jogador!")
        print("O que você deseja fazer para prosseguir?")
        print("1 - Login de Usuário")
        print("2 - Cadastro de Usuário")
        print("3 - Dúvidas sobre itens ou monstros(?)")
        print("0 - Encerrar o jogo")
        print("--------------------------------------")

        opcao_escolhida = int(input("Escolha a opcao: "))
        return opcao_escolhida
#         opções para o usuário escolher (ele ainda não logou, então pensei em fazer uma "instruções"
#         ou informações sobre o jogo antes de entrar na opções de fato)

