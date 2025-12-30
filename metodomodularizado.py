from metodoconstrutor import Conta_corrente

# Criar conta 
while True:
    try:
        titular = input("Digite o nome do titular: ")
        idade = int(input("Digite a idade do titular: "))
        cpf = input("Digite o CPF do titular: ")
        saldo = float(input("Digite o saldo inicial: "))
        break
    except ValueError:
        print("Valores inválidos, tente novamente")

# Criando a conta
clienteum = Conta_corrente(Titular=titular, Idade=idade, Cpf=cpf, Saldo=saldo)
print(f"Conta de {clienteum._titular} foi criada com sucesso!\n")

# Método para sacar
clienteum.saque()

# Método para mostrar informações
clienteum.informacoes()

#Método para Sacar
clienteum.saque()





