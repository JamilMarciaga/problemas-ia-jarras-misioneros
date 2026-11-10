import problema1_jarras
import problema2_misioneros_canibales
import problema3_pila_salidas

def menu():
    while True:
        print("\n===== MENÚ DE PROBLEMAS =====")
        print("1. Jarras de 4 y 3 galones")
        print("2. Misioneros y caníbales")
        print("3. Salidas posibles del código con pila")
        print("0. Salir")
        op = input("Elige una opción: ").strip()

        if op == "1":
            problema1_jarras.main()
        elif op == "2":
            problema2_misioneros_canibales.main()
        elif op == "3":
            problema3_pila_salidas.main()
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()