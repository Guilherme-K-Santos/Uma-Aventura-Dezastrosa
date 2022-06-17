

class TelaSistema:

    def tela_inicial(self):
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

   # def tela_logados(self):
   #     print("--------------------------------------")
   #     print("Login efetuado com sucesso!")
   #     print("Qual a aventura que embarcaremos?")
   #     print("1 - Acessar Heróis já Criados")
   #     print("2 - Criar Novo Herói")
   #     print("3 - Sair da Conta")
   #     print("4 - Excluir Conta")
   #     print("0 - Retornar")
   #     print("--------------------------------------")

   #     opcao = int(input("Escolha a opcao: "))
   #     return opcao

#         opções para o usuário escolher (ele agora está LOGADO, então pode prosseguir
#         para acessar ou criar heróis), essa tela pode ser colocada em tela sistema também,
#         conversamos depois
