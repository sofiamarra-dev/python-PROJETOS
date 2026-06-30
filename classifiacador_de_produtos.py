#Classificador de produtos alimenticios por ID

ids = []

print(" === Classificador de produtos alimenticios de Produtos ===")
print("IDS pares == Doces | IDS impares == Amargos\n")

for i in range(1,10):
    while True:
        try:
            id_produto = int(input(f"difite o ID do produto {i}: "))
            ids.append(id_produto)
            break
        except ValueError:
            print(" Digite apenas um numero inteiro valido.")

doces = [id for id in ids if id % 2 == 0]
amargos = [id for id in ids if id % 2 != 0]

print("\n== Resultado ==")
print(f"Doces (par): {len(doces)}   Ids:{doces if doces else "nenhum"}")
print(f"Amargos (impar): {len(amargos)}   Ids: {amargos if amargos else "nenhum"}")