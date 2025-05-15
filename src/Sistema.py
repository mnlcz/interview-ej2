import datetime

from src.Gestor import Gestor


class Sistema:
    def __init__(self) -> None:
        self.cotizaciones = []

    def getdata(self, date: datetime.date) -> None:
        fmt_date = date.strftime("%d/%m/%Y")
        self.cotizaciones.append(Gestor.update(fmt_date))

    def printdata(self, date: datetime.date) -> None:
        fmt_date = date.strftime("%d/%m/%Y")
        print(f"Cotizaciones del dia {fmt_date}:")
        cot = [c for c in self.cotizaciones if c.fecha == fmt_date]
        if len(cot) == 0:
            print("No hay cotizaciones para la fecha especificada")
        else:
            c = cot[0]
            for divisa in c.divisas:
                print(
                    f"{divisa.codigo} - {divisa.nombre} - {divisa.compra} - {divisa.venta} - {divisa.pase_compra} - {divisa.pase_venta}")
