# Questão 3: Estruturas de repetição
""" Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'. """

class Validacao:

    def iniciarMenuValida(self):

        print("Insira os dados abaixo.")

        nome = input("Nome: ")
        idade = input("Idade: ")
        idade = int(idade)
        salario = input("Salário: ")
        salario = float(salario)
        sexo = input("Sexo: ")
        civil = input("Estado civil: ")

        return nome, idade, salario, sexo, civil

    def validarDados(self):

        dados = self.iniciarMenuValida()

        nome, idade, salario, sexo, civil = dados

        if len(nome) > 3:
            print("\nNome válido.")
        else:
            print("\nNome inválido."
                  "\nO nome precisa ter mais de três letras.")

        if idade < 0 or idade > 150:
            print("\nIdade inválida."
                  "\nApenas permitida a idade entre 0 e 150.")
        elif idade >=0 and idade <= 150:
            print("\nIdade válida.")

        if salario <= 0:
            print("\nSalário inválido."
                  "\nO salário precisa ser maior que 0.")
        else:
            print("\nSalário válido.")

        if sexo == "f" or sexo == "m":
            print("\nSexo válido.")
        elif sexo != "f" and sexo != "m":
            print("\nSexo inválido."
                  "\nDigite f para feminino, m para masculino.")

        if civil == "s" or civil == "c" or civil == "v" or civil == "d":
            print("\nEstado civil válido.")
        elif civil != "s" and civil != "c" and civil != "v" and civil != "d":
            print("\nEstado civil inválido."
                  "\nDigite s para solteiro(a), c para casado(a), v para viúvo(a), d para divorciado(a).")


a = Validacao()
a.validarDados()


