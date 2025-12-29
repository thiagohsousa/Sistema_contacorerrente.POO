class Conta_corrente():
    def __init__(self,Titular,Idade, Cpf,  Saldo):
        self.Titular = Titular
        self.Saldo = Saldo
        self.Cpf = Cpf
        self.idade = Idade
    def transferir(self):
        transferencia = float(input("Digite o quanto vc deseja transferir: "))
        if self.Saldo >= transferencia:
            self.Novo_saldo = self.Saldo - transferencia
            print(F"""-------------------------------
TRANSFERENCIA CONCLUIDA 
-------------------------------
                  
SALDO DISPONIVEL: {self.Novo_saldo}
-------------------------------""")
            

    def informacoes(self):
        print(f"""------------------------------- 
INFORMAÇÕES
-------------------------------
          
1 - Titular: {self.Titular}


2 - Cpf: {self.Cpf}

3 - Idade: {self.idade}

4 - Saldo Disponivel: {self.Novo_saldo}""")
  


