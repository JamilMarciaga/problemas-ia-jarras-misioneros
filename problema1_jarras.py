from collections import deque

def jarras():
    inicio = (0, 0)
    def objetivo(s):
        return s[0] == 2
    visitado = {inicio: (None, None)}
    cola = deque([inicio])

    while cola:
        estado = cola.popleft()
        if objetivo(estado):
            camino = []
            while estado is not None:
                padre, accion = visitado[estado]
                camino.append((estado, accion))
                estado = padre
            return camino[::-1]

        a, b = estado
        acciones = [
            ("Llenar jarra de 4", (4, b)),
            ("Llenar jarra de 3", (a, 3)),
            ("Vaciar jarra de 4", (0, b)),
            ("Vaciar jarra de 3", (a, 0)),
            ("Verter 4 -> 3", (max(0, a - (3 - b)), min(3, b + a))),
            ("Verter 3 -> 4", (min(4, a + b), max(0, b - (4 - a)))),
        ]
        for nombre, nuevo in acciones:
            if nuevo not in visitado:
                visitado[nuevo] = (estado, nombre)
                cola.append(nuevo)

def main():
    print("=== PROBLEMA 1: JARRAS ===")
    camino = jarras()
    for i, ((a, b), accion) in enumerate(camino):
        if accion:
            print(f"Paso {i}: {accion:20s} -> jarra4={a}, jarra3={b}")
        else:
            print(f"Paso {i}: {'Inicio':20s} -> jarra4={a}, jarra3={b}")
    print("Objetivo logrado: 2 galones en la jarra de 4\n")

if __name__ == "__main__":
    main()