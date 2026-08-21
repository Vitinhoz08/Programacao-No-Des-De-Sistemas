class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

# Função que demonstra o polimorfismo no cadastro
def registrar_atendimento(animal):
    print(f"Animal cadastrado: {animal.nome} | Som: {animal.emitir_som()}")

# Testando o código
dog = Cachorro("Rex")
cat = Gato("Mia")

registrar_atendimento(dog)
registrar_atendimento(cat)
