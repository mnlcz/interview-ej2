from datetime import date

from src.Gestor import Gestor

if __name__ == "__main__":
    hoy = date.today().strftime("%d/%m/%Y")
    historico = []
    datos_hoy = Gestor.update(hoy)
    historico.append(datos_hoy)
    for d in historico[0].divisas:
        print(d)
    
    