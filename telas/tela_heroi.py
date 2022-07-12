

class TelaHeroi:

    def mensagem(self, texto):
        print(texto)
        input()

    def pegar_nome_heroi(self):
        nome = input("Nome do herói: ")
        return nome

    def opcoes_itens(self):
        print(" 1 - Equipar")
        print(" 2 - Deletar")
        print(" 3 - Desequipar")
        print(" 0 - Retornar")
        opcao = self.excecoes_escolha("Escolha uma Opção ", [1, 2, 3, 0])
        return opcao

    def escolhe_itens(self, validacao):
        print("Escolha um item para equipar ou deletar")
        print("Ou digite 0 para retornar")
        item = self.excecoes_escolha("Escolha uma Opção ", validacao)
        return item

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
