#Importando a função Randit para gerar o Id
from random import randint

#Criando a classe conta corrente para criar a conta
class Conta_corrente:
    def __init__(self):
        while True:
            try:
                while True:
                    self._titular = input("Digite o nome do titular: ")
                    if self._titular.replace(" ", "").isalpha() and self._titular != "":
                        break
                    else:
                        print("Erro, o nome deste usuario contem letras!! digite um nome valido")

                while True:
                    self._idade = int(input("Digite a idade do titular: "))
                    if self._idade >= 18 and self._idade <= 100:
                     break
                    else:
                        print("Erro, este usuario é menor de idade, tente Novamente")
                while True:
                    self._cpf = input("Digite o CPF do titular: ")
                    if self._cpf.replace(".", "").replace("-", "").isdigit() and len(self._cpf) == 11:
                        break
                    else: 
                        print("Cpf invalido; Digite o Cpf igual a 11 caracteres")
                while True:
                    self._saldo = float(input("Digite o saldo inicial: "))
                    if self.saldo > 0:
                        break
                    else:
                        print("Saldo invcalido; Digite um saldo maior que 0")
                self._conta_id = self.gerar_id()
                print(f"""-----------------------------------------
Conta criada com sucesso!
------------------------------------------
BEM VINDO {self._titular}
------------------------------------------""")
                break
            except ValueError:
                print("Valor inválido, tente novamente..")

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
            if continuar != "S":
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
    
    def depositar(self):
        while True:
            try:
                valor_depositado = float(input("Digite o valor que deseja Deposita: "))
                if valor_depositado > 0 and isinstance(valor_depositado, (int, float)):   
                    self._saldo += valor_depositado

                    print(f"""-------------------------------
Saque realizado
Novo saldo: {self._saldo}
-------------------------------""")
                    break
                else:
                     print("Digite um valor maior que 0")
            except ValueError:
                print("Valor inválido, tente novamente..")



        

