import requests
from bs4 import BeautifulSoup
from src.Cotizaciones import Cotizaciones
from src.Divisa import Divisa

class Gestor:
    @staticmethod
    def update(fecha: str) -> Cotizaciones:
        url = "http://b2b.sif.com.ar/Servicios/Aplicaciones/Cotizacion/CotizacionesList.asp"
        out = []
        res = requests.post(url, data=fecha)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            xml_data = soup.find('xml', {'id': 'list_xml'})

            for divisa in xml_data.find_all('divisa'):
                code = divisa.get('divisa')
                name = divisa.get('descripcion').replace('<DIV class=negrita>', '').replace('</DIV>', '').strip()
                buy = divisa.get('compra')
                sell = divisa.get('venta')
                buy_rate = divisa.get('pasecompra')
                sell_rate = divisa.get('paseventa')
                
                divisa = Divisa(code, name, buy, sell, buy_rate, sell_rate)
                out.append(divisa)
        else:
            print(f"Error, status code: {res.status_code}")
        return Cotizaciones(fecha, out)
