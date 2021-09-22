# Questão 2: Estruturas de repetição
""" Use a função len(string) para saber o tamanho de um texto (número de caracteres). """

class Contagem:

    def escreverTexto(self):

        texto = input("Escreva o texto: ")
        contagem = len(texto)

        print(f"O texto possui {contagem} caracteres.")


a = Contagem()
a.escreverTexto()