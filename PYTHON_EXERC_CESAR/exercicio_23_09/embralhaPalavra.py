# Questão 12: Funções
""" Construir uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
de forma aleatória. Padronizar em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
independentemente de como foram digitados. """

import random

class Palavra:

    def embaralharPalavra(self, palavra):

        embaralha = ''.join(random.sample(palavra, len(palavra)))

        return embaralha

    def escreverPalavra(self):

        palavra = input("Digite uma palavra: ")

        novaPalavra = self.embaralharPalavra(palavra)

        novaPalavra = novaPalavra.upper()

        print(novaPalavra)

a = Palavra()
a.escreverPalavra()