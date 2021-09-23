# Questão 10: Funções
""" Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente. """

import random
from time import sleep

class Jogo:

    def jogarDados(self):

        dado1 = random.randrange(1, 7)
        dado2 = random.randrange(1, 7)

        return dado1, dado2

    def somarDados(self, jogada1, jogada2):

        soma = jogada1 + jogada2

        return soma


    def informarResultadoJogada(self, jogada1, jogada2):

        soma = self.somarDados(jogada1, jogada2)

        print("========================================================================================")
        print(f"\nDado 1: {jogada1}")
        print(f"Dado 2: {jogada2}")
        print(f"\nA soma dos números dos dois dados é {soma}.")

    def iniciarJogo(self):

        print("\n========================"
              "\nJOGO DE CRAPS ELETRÔNICO\n"
              "========================\n")

        print("O jogo de craps consiste em lançar um par de dados e observar a soma dos números."
              "\nSe, na primeira jogada, a soma dos números for 7 ou 11, você ganhou o jogo."
              "\nSe a soma dos números na primeira jogada for igual 2, 3 ou 12, 'CRAPS!' você perdeu o jogo"
              "\nSe, na primeira jodada, os números somarem 4, 5, 6, 8, 9 ou 10, esta será a sua pontuação."
              "\nE, para ganhar, a soma dos números nas próximas jogadas precisa ser igual a da primeira."
              "\nCaso a soma dos números seja igual a 7 antes de conseguir a pontuação da primeira jogada,"
              "\nvocê perderá o jogo.")

        while True:

            jogo = input("\nDeseja lançar os dois dados agora?"
                            "\n1 - Sim"
                            "\n2 - Não\n")

            if jogo == "1":

                dado1, dado2 = self.jogarDados()

                self.informarResultadoJogada(dado1, dado2)

                soma = self.somarDados(dado1, dado2)

                if 4 <= soma <= 6 or 8 <= soma <= 10:

                    print(f"\nVocê tirou {soma}. Para ganhar o jogo, precisa tirar esse número na próxima jogada. Boa sorte!")

                    sleep(5)

                    dado3, dado4 = self.jogarDados()

                    self.informarResultadoJogada(dado3, dado4)

                    soma2 = self.somarDados(dado3, dado4)

                    while soma != soma2:

                        if soma2 != 7:

                            print(f"\nAh... Você tirou {soma2}. Você tem mais uma tentativa.")

                            sleep(7)

                            dado5, dado6 = self.jogarDados()

                            self.informarResultadoJogada(dado5, dado6)

                            soma2 = self.somarDados(dado5, dado6)

                        elif soma2 == 7:

                            print("\nAh... Você tirou 7 e perdeu o jogo... "
                                  "Quem sabe da próxima vez você tem mais sorte.")

                            quit()

                    print(f"\nUhuuu!!! Você tirou {soma} e ganhou o jogo.")

                elif soma == 2 or soma == 3 or soma == 12:

                    print(f"\nQue pena... Você tirou {soma} na primeira jogada e perdeu o jogo... "
                          f"\nQuem sabe da próxima vez você tem mais sorte.")

                elif soma == 7 or soma == 11:

                    print(f"\nUhuuu!!! Você tem muita sorte! Tirou {soma} na primeira jogada e ganhou o jogo.")

            elif jogo == "2":

                print("\nOk! Podemos tentar jogar mais tarde.")

            else:

                print("\nCódigo incorreto.\nTente novamente.")
                print("========================================================================================")

            if jogo == "1" or jogo == "2":
                quit()



a = Jogo()
b = a.iniciarJogo()
