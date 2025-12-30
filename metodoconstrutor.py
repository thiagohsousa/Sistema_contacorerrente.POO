#Classe para criar uma conta corrente
class Conta_corrente():
    def __init__(self,Titular,Idade, Cpf,  Saldo):
        self._titular = Titular      
        self._idade = Idade
        self._cpf = Cpf
        self._Saldo = Saldo


   #METODO GETTER: Le o valor
    @property
    def saldo(self):
        return self._Saldo

    #Metodo SETTER: Altera o Valor e trata os erros
    @saldo.setter
    def novo_saldo(self, novo_saldo):
        if isinstance(novo_saldo, (int, float)) and novo_saldo >= 0:
            self._Saldo = novo_saldo
        else:
            print("Saldo Invalido!!!")

    #logica sem loop para transferir, incluirei na função transferir.
    def funcao_transferir(self):
      
        transferencia = float(input("Digite o quanto vc deseja transferir: "))
        if self._Saldo >= transferencia:
            self._Saldo -= transferencia
            print(F"""-------------------------------
TRANSFERENCIA CONCLUIDA 
-------------------------------

SALDO DISPONIVEL: {self._Saldo}
-------------------------------""")
        
            
        else:
            print("Saldo Insuficiente, Tente Novamente")

     #função para transferir  com o loop.
    def tranferencia(self):
        while True:
            self.funcao_transferir()
            continuar = input("Deseja Continuar? [S/N]: ")
            if continuar != "S":
                print("OPERAÇÃO FINALIZADA")
                break


   #METODO GETTER: Le o valor
    @property
    def sacar(self):
        return self._Saldo
    #Metodo SETTER: Altera o Valor e trata os erros
    @sacar.setter
    def saldo_saque(self, sacar):
        if isinstance(sacar, (int, float)) and sacar >= 0:
            self._Saldo = sacar
    #Logica sem Lopp para sacar, incluirei ela na função Saque
    def funcao_saque(self):
        sacar = float(input("Digite quanto vc deseja sacar: "))
        if sacar <= self._Saldo:
            self._Saldo -= sacar
            print(f"""-------------------------------
Saque Realizado
Seu Novo saldo é de {self._Saldo}
-------------------------------""")
        else:
            print("Saque invalido!!!")
    #Funçaõ para sacar com loop
    def saque(self):
        while True:
            self.funcao_saque()
            continuar =  continuar = input("Deseja Continuar? [S/N]: ")
            if continuar != "S":
                print("OPERAÇÃO FINALIZADA")
                break
            

    





#Função que Printa todas as informações da conta
    def informacoes(self):
        print(f"""------------------------------- 
INFORMAÇÕES
-------------------------------
          
1 - Titular: {self._titular}


2 - Cpf: {self._cpf}

3 - Idade: {self._idade}

4 - Saldo Disponivel: {self._Saldo}""")
  
            