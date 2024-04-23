class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano 
     
    def exibir_informacoes(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Ano: ", self.ano)

carros = []

while True:
    marca = input("inaira a marca do carro ou 0 para sair")

    if marca == "0":
        break
    
    modelo = input("insira o modelo do carro que deseja")
    cor = input("insira a cor do carro que deseja")
    ano = input("insira o ano do carro que deseja")


    carro = Carro(marca, modelo, cor, ano)
    carros.append(carro)

print("\n informações dos carros:")
for i, carro in enumerate(carros, start=1):
    print("\n carro {i}")
    carro.exibir_informacoes()

input()
