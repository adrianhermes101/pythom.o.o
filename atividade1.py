
#Objeto é uma unica coleção de dados(atributos) e comportamentos (metodos)
class contaBancaria:
       #Atributos são variaveis internas dentro do objeto
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        #Metodos são funções do objeto que produzem algum comportamento
    def depositar(self, valor):
        self.saldo += valor 

    def exibir_detalhes(self):
        print("Número da Conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)     

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Lhe falta bufunfas.") 

def exibir_menu():
    print("\nMENU:")
    print("1 - exibir detalhes da conta")
    print("2 - realizar depósito")
    print("3 - realizar saque")
    print("0 - Sair do Programa") 

#aqui estou criando ua instancia do objeto contaBancaria
#com o nome de conta_do_adrian
numero_conta = input("Digite o numero da conta: ")
titular_conta = input("Digite o titular da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da sua conta: ").replace(",", "."))

conta_do_Usuario = contaBancaria(numero_conta, titular_conta, saldo_inicial)

opcao = None 

while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite o numero da opção desejada: "))

    if opcao == 1:
        conta_do_Usuario.exibir_detalhes()
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor de depósito: ").replace(",", "."))
        conta_do_Usuario.depositar(valor_deposito)
    elif opcao == 3:
        valor_saque = float(input("Digite o valor a ser sacado: ").replace(",", "."))
        conta_do_Usuario.sacar(valor_saque)
