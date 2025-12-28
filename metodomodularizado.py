from metodoconstrutor import Conta_corrente


clienteum = Conta_corrente(Titular='Thiago Henrique Sousa Melo', Idade=16, Cpf="011.111.111-11", Saldo=150000.0)




print(f""" -------------------------------------- 
      Informações
--------------------------------------     
      
1- Titular: {clienteum.Titular}\n
2- Idade: {clienteum.idade}\n
3- Cpf: {clienteum.Cpf}\n
4- Saldo: {clienteum.Saldo}\n

--------------------------------------  """)
