from collections import deque

def valido(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    m2, c2 = 3 - m, 3 - c
    if m2 > 0 and c2 > m2:
        return False
    return True

def misioneros():
    inicio = (3, 3, 'I')
    objetivo = (0, 0, 'D')
    visitado = {inicio: (None, None)}
    cola = deque([inicio])
    movs = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    while cola:
        estado = cola.popleft()
        if estado == objetivo:
            camino = []
            while estado is not None:
                padre, accion = visitado[estado]
                camino.append((estado, accion))
                estado = padre
            return camino[::-1]

        m, c, lado = estado
        for dm, dc in movs:
            if lado == 'I':
                nm, nc, nl = m - dm, c - dc, 'D'
            else:
                nm, nc, nl = m + dm, c + dc, 'I'
            if valido(nm, nc):
                nuevo = (nm, nc, nl)
                if nuevo not in visitado:
                    accion = f"{dm}M+{dc}C -> {'Derecha' if nl=='D' else 'Izquierda'}"
                    visitado[nuevo] = (estado, accion)
                    cola.append(nuevo)

def main():
    print("=== PROBLEMA 2: MISIONEROS Y CANÍBALES ===")
    camino = misioneros()
    for i, ((m, c, lado), accion) in enumerate(camino):
        if accion:
            print(f"Paso {i:2d}: {accion:25s} | Izq=({m}M,{c}C) Bote en {'Izq' if lado=='I' else 'Der'}")
        else:
            print(f"Paso {i:2d}: {'Inicio':25s} | Izq=({m}M,{c}C) Bote en {'Izq' if lado=='I' else 'Der'}")
    print(f"Total de cruces: {len(camino)-1}\n")

if __name__ == "__main__":
    main()