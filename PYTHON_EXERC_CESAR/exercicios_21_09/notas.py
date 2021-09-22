# Questão 1:Estruturas de repetição
"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
 seja inválido e continue pedindo até que o usuário informe um valor válido."""

class Notas:

    def iniciarMenuAvaliacao(self):

        print("\nLANÇAMENTO DE NOTAS DO SEMESTRE")

        avaliacao = input("\nO lançamento das notas deve ser realizado escolhendo-se uma das avaliações abaixo:"
                          "\n1 - Primeira Avaliação"
                          "\n2 - Segunda Avaliação"
                          "\n3 - Terceira Avaliação\n")

        while avaliacao != "1" and avaliacao != "2" and avaliacao != "3":
            print("Opção inválida.\nTente novamente.")
            avaliacao = input("\nO lançamento das notas deve ser realizado escolhendo-se uma das avaliações abaixo:"
                              "\n1 - Primeira Avaliação"
                              "\n2 - Segunda Avaliação"
                              "\n3 - Terceira Avaliação\n")

        if avaliacao == "1":
            return 1
        elif avaliacao == "2":
            return 2
        elif avaliacao == "3":
            return 3

    def lancarNota(self):

        nota = input("\nDigite a nota: ")
        nota = float(nota)

        return nota

    def lancarNome(self):

        nome = input("\nDigite o nome do(a) aluno(a): ")

        return nome

    def finalizarLancamento(self):
        avaliacao = self.iniciarMenuAvaliacao()
        nome = self.lancarNome()
        nota = self.lancarNota()

        if avaliacao == "1":
            print(f"\nO(A) aluno(a) {nome} tirou a nota {nota} na {avaliacao}º avaliação.")
        elif avaliacao == "2":
            print(f"\nO(A) aluno(a) {nome} tirou a nota {nota} na {avaliacao}º avaliação.")
        else:
            print(f"\nO(A) aluno(a) {nome} tirou a nota {nota} na {avaliacao}º avaliação.")


a = Notas()
a.finalizarLancamento()
