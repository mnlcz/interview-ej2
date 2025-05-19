import os
from datetime import datetime
from src.Sistema import Sistema

# Debería incluir opciones para consultar el histórico
def run(sistema: Sistema) -> None:
    while True:
        os.system('cls')
        d = datetime.strptime(input("Ingrese fecha (ej: 28 2 2000): "), "%d %m %Y")
        sistema.getdata(d)
        sistema.printdata(d)

        cont = input("Desea continuar? (s/n): ")
        if cont == "n":
            break


if __name__ == "__main__":
    sis = Sistema()
    run(sis)
