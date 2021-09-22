# Questão 5: Estruturas de repetição
""" Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
 ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. """
# Questão 6: Estruturas de repetição
""" Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação. """

class Populacao:

    def calcularCrescimento(self, habitante, taxa):

        habitantesPorAno = (float(taxa) / 100) * float(habitante)

        return habitantesPorAno

    def calcularCrescimentoAno(self, a, b, taxaA, taxaB, ano):

        crecA = self.calcularCrescimento(a, taxaA)
        crecB = self.calcularCrescimento(b, taxaB)

        a = a + crecA
        b = b + crecB

        ano = ano + 1

        return a, b, ano

    def calcularPaises(self):
        a = 80000
        b = 200000
        taxaA = 3
        taxaB = 1.5
        ano = 0

        while a <= b:

            dados = self.calcularCrescimentoAno(a, b, taxaA, taxaB, ano)

            a, b, ano = dados

        print(f"Considerando a população de 80000 habitantes com taxa de crescimento de 3% "
              f"ao ano do país A, e a população de 200000 habitantes com taxa de crescimento de 1,5% "
              f"ao ano do país B, o país A ultrapassa a população do país B em {ano} anos.\n"
              f"Sendo que o país A terá {a} de habitantes e o país B terá {b} de habitantes.")

    def calcularDadosPopulacao(self):
        ano = 0
        pais = "Nome do país: "
        pop = "População do país: "
        taxa = "Taxa de crescimento populacional do país (apenas números): "

        print("\nCOMPARAÇÃO DO CÁLCULO DE CRESCIMENTO POPULACIONAL ENTRE DOIS PAÍSES\n")

        print("Insira do dados do 1º país.")
        a = input(pais)
        popA = input(pop)
        popA = float(popA)
        taxaA = input(taxa)
        taxaA = float(taxaA)

        print("\nInsira do dados do 2º país.")
        b = input(pais)
        popB = input(pop)
        popB = float(popB)
        taxaB = input(taxa)
        taxaB = float(taxaB)

        if popA < popB:

            while popA <= popB:

                dados = self.calcularCrescimentoAno(popA, popB, taxaA, taxaB, ano)

                popA, popB, ano = dados

            print(f"\nA população do país {a} ultrapassa a população do país {b} em {ano} anos.")

        elif popA > popB:

            while popA >= popB:

                dados = self.calcularCrescimentoAno(popA, popB, taxaA, taxaB, ano)

                popA, popB, ano = dados

            print(f"\nA população do país {b} ultrapassa a população do país {a} em {ano} anos.")

        elif popA == popB and taxaA != taxaB:

            print(f"\nAtualmente, os países {a} e {b} possuem a mesma quantidade de habitantes. "
                  f"Divergindo apenas na taxa de crescimento populacional.")

        else:

            print(f"\nAtualmente, os países {a} e {b} possuem a mesma quantidade de habitantes.")

a = Populacao()
a.calcularPaises()
a.calcularDadosPopulacao()
