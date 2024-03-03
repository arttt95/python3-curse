def conta_ate(max):
    numero = 1
    while numero <= max:
        yield numero
        numero = numero + 1


gen = list(conta_ate(5))

print(gen)
