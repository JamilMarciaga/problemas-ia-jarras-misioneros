from itertools import product

def simular(test_resultados):
    pila = []
    salida = []
    for i in range(1, 4):
        if test_resultados[i-1]:
            salida.append(i)
        else:
            pila.append(i)
    while pila:
        salida.append(pila.pop())
    return salida

opciones = {
    'a': [1,2,3],
    'b': [1,3,2],
    'c': [2,1,3],
    'd': [3,1,2],
    'e': [2,3,1],
    'f': [3,2,1],
}

def main():
    print("=== PROBLEMA 3: POSIBLES SALIDAS ===")
    posibles = set()
    for combo in product([True, False], repeat=3):
        salida = simular(combo)
        posibles.add(tuple(salida))
        estado = ''.join('V' if x else 'F' for x in combo)
        print(f"TEST(1..3)={estado} -> salida: {salida}")

    print("\nSalidas posibles generadas:", sorted(posibles))
    print("\nVerificación de opciones:")
    for letra, op in opciones.items():
        ok = tuple(op) in posibles
        print(f"  {letra}) {op}  -> {'POSIBLE' if ok else 'NO POSIBLE'}")

if __name__ == "__main__":
    main()