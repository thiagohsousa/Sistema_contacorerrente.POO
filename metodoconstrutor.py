class Conta_corrente():
    def __init__(self,Titular,Idade, Cpf,  Saldo):
        self.Titular = Titular
        self.Saldo = Saldo
        self.Cpf = Cpf
        self.idade = Idade
  
    def transferir(self):
            transferir = float(input("Digite o   Quanto que voce deseja tranferir: "))
            if self.Saldo >= transferir:
                self.Novo_saldo = self.Saldo - transferir
                print(f"""Tranferencia Concluida
                      
                      Saldo Atual: {self.Novo_saldo}""")
                
    def informacoes(self):
         print(f""" -------------------------------------- 
      Informações
--------------------------------------     
      
1- Titular: {self.Titular}\n
2- Idade: {self.idade}\n
3- Cpf: {self.Cpf}\n
4- Saldo: {self.Novo_saldo}\n

--------------------------------------  """)

         


        

