# Questão 2: Estruturas de repetição
""" Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações. """

class Cadastro:

    def inserirDados(self):

        nome = input("Crie um usuário: ")
        senha = input("Crie uma senha: ")

        return nome, senha

    def validarSenha(self):

        print("\nSISTEMA DE CADASTRO DE USUÁRIO\n")

        dados = self.inserirDados()

        nome, senha = dados

        while senha == nome:
            print("\nEsta senha não é permitida.\n")
            senha = input("Crie uma senha novamente: ")

        print(f"\nSenha válida.\nUsuário(a) {nome} cadastrado com sucesso.")

a = Cadastro()
a.validarSenha()


