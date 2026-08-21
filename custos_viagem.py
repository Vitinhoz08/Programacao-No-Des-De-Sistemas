class Veiculo:
    def __init__(self, modelo, consumo_km_por_litro, preco_combustivel):
        self.modelo = modelo
        self.consumo = consumo_km_por_litro  # km/L
        self.preco_combustivel = preco_combustivel  # Preço por litro

    def calcular_custo_viagem(self, distancia):
        litros_necessarios = distancia / self.consumo
        return litros_necessarios * self.preco_combustivel


class Carro(Veiculo):
    pass


class Moto(Veiculo):
    pass


class Caminhao(Veiculo):
    pass


def calcular_custo_total_frota(lista_veiculos, distancia=200):
    """
    Recebe uma lista de diferentes tipos de veículos e calcula
    o custo total de uma viagem (padrão de 200 km) para todos eles.
    """
    custo_total = 0.0
    
    for veiculo in lista_veiculos:
        custo_total += veiculo.calcular_custo_viagem(distancia)
        
    return custo_total


carro_sedan = Carro(modelo="Civic", consumo_km_por_litro=10, preco_combustivel=5.80)
moto_esportiva = Moto(modelo="Ninja", consumo_km_por_litro=20, preco_combustivel=5.80)
caminhao_carga = Caminhao(modelo="Volvo", consumo_km_por_litro=4, preco_combustivel=6.10)


minha_frota = [carro_sedan, moto_esportiva, caminhao_carga]


custo_final = calcular_custo_total_frota(minha_frota, distancia=200)

print(f"O custo total da viagem de 200 km para todos os veículos é: R$ {custo_final:.2f}")