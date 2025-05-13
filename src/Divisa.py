class Divisa:
    def __init__(self, codigo, nombre, compra, venta, pase_compra, pase_venta) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.compra = compra
        self.venta = venta
        self.pase_compra = pase_compra
        self.pase_venta = pase_venta
        
    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.compra} - {self.venta} - {self.pase_compra} - {self.pase_venta}"