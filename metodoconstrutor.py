from random import randint

#Classe para criar uma conta corrente
class Conta_corrente():
      def __init__(self, titular="", idade=0, cpf="", saldo=0):
         while True:
            try:
                self._titular = input("Digite o nome do titular: ")
                self._idade =  int(input("Digite a idade do titular: "))
                self._cpf = input("Digite o CPF do titular: ")
                self._saldo =  float(input("Digite o saldo inicial: "))
                self._conta_id = self.gerar_id()
                break
            except:
               print("Idade ou Cpf Invalidos, Tente Novamente!!")

    



   #METODO GETTER: Le o valor
      @property
      def saldo(self):
            return self._saldo

    #Metodo SETTER: Altera o Valor e trata os erros
      @saldo.setter
      def novo_saldo(self, novo_saldo):
        if isinstance(novo_saldo, (int, float)) and novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("Saldo Invalido!!!")

    #logica sem loop para transferir, incluirei na função transferir.
      def funcao_transferir(self):
      
        transferencia = float(input("Digite o quanto vc deseja transferir: "))
        if self._saldo >= transferencia:
            self._saldo -= transferencia
            print(F"""-------------------------------
TRANSFERENCIA CONCLUIDA 
-------------------------------

SALDO DISPONIVEL: {self._saldo}
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
        return self._saldo
    #Metodo SETTER: Altera o Valor e trata os erros
      @sacar.setter
      def saldo_saque(self, sacar):
        if isinstance(sacar, (int, float)) and sacar >= 0:
            self._saldo = sacar
    #Logica sem Lopp para sacar, incluirei ela na função Saque
      def funcao_saque(self):
        sacar = float(input("Digite quanto vc deseja sacar: "))
        if sacar <= self._saldo:
            self._saldo -= sacar
            print(f"""-------------------------------
Saque Realizado
Seu Novo saldo é de {self._saldo}
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

4- Id da Conta: {self._conta_id}

5 - Saldo Disponivel: {self._saldo}""")
  



    
    

      def gerar_id(self):
        return randint(1, 1000)
