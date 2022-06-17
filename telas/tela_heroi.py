

class TelaHeroi:

    def tela_opcoes_heroi(self):
        print("====OPÇÕES DE HERÓI====")
        print("0 - retornar")
        print("1 - atacar")
        print("2 - descansar")
        print("2 - abrir mochila")
        print("2 - escolher titulo")
        opcao_escolhida = int(input("escolha uma opção: "))
        return opcao_escolhida

    def mensagem(self,texto):
        print(texto)
        input()

    def pegar_nome_heroi(self):
        nome = input("Nome do herói: ")


        return nome