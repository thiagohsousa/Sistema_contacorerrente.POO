#Importando a função Randit para gerar o Id
from random import randint

#Criando a classe conta corrente para criar a conta
class Conta_corrente:
    def __init__(self):
        while True:
            try:
                self._titular = input("Digite o nome do titular: ")
                self._idade = int(input("Digite a idade do titular: "))
                self._cpf = input("Digite o CPF do titular: ")
                self._saldo = float(input("Digite o saldo inicial: "))
                self._conta_id = self.gerar_id()
                print("Conta criada com sucesso!")
                break
            except ValueError:
                print("Idade ou saldo inválidos, tente novamente.")

    # Getter e setter do saldo
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._saldo = valor
        else:
            print("Saldo inválido!")

    # Transferência
    def transferir(self):
        while True:
            try:
                transferencia = float(input("Digite o valor para transferir: "))
                if self._saldo >= transferencia:
                    self._saldo -= transferencia
                    print(f"""-------------------------------
TRANSFERÊNCIA CONCLUÍDA
SALDO DISPONÍVEL: {self._saldo}
-------------------------------""")
                else:
                    print("Saldo insuficiente, tente novamente!")
            except ValueError:
                print("Digite um número válido!")

            continuar = input("Deseja continuar? [S/N]: ").upper()
            if continuar == "N":
                print("OPERAÇÃO FINALIZADA")
                break

    # Saque
    def saque(self):
        while True:
            try:
                valor_saque = float(input("Digite o valor para sacar: "))
                if valor_saque <= self._saldo:
                    self._saldo -= valor_saque
                    print(f"""-------------------------------
Saque realizado
Novo saldo: {self._saldo}
-------------------------------""")
                else:
                    print("Saldo insuficiente!")
            except ValueError:
                print("Digite um número válido!")

            continuar = input("Deseja continuar? [S/N]: ").upper()
            if continuar != "S":
                print("Operação finalizada")
                break

    # Informações da conta
    def informacoes(self):
        print(f"""-------------------------------
INFORMAÇÕES DA CONTA
-------------------------------
Titular: {self._titular}
CPF: {self._cpf}
Idade: {self._idade}
ID da Conta: {self._conta_id}
Saldo: {self._saldo}
-------------------------------""")

    # Gerar Id
    def gerar_id(self):
        return randint(1, 1000)
