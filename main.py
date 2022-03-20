# from asyncio import exceptions
from logging import exception
from re import X
import poo
from exceptions import Excepcion
import dalecolor as dc
# from exceptions import test

dc.clear()

# __init__(self, nombre, RUT, nombre, razon_social, pais, persona)
db_proveedores = {
    1: poo.Proveedor('Proveedor A', '1234', 'Poundland', 'Proveedor A Ltda.', 'UK', 'Juridica'),
    2: poo.Proveedor('Proveedor B', '5678', 'BBB', 'Proveedor B Ltda.', 'Chile', 'Juridica')
}
# __init__(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo, edad, historial_compras)
db_clientes = {
    1: poo.Cliente(1, "José", "Rua", "jose@gmail.com", "2020-10-01", 1000, 33,[300,200]),
    2: poo.Cliente(2, "Maria", "Lee", "maria@gmail.com", "2018-12-03", 2000, 43,[]),
    3: poo.Cliente(3, "Kimberly", "Choriza", "kim@gmail.com", "2009-03-23", 3000, 23,[570,3000,200]),
    4: poo.Cliente(4, "Tamara", "Neira", "tamara@gmail.com", "1980-12-22", 33000, 45,[100,100,10]),
    5: poo.Cliente(5, "Paula", "Ramirez", "paula@gmail.com", "1998-12-21", 5000, 88,[])
}


# __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, color)
db_productos = {
    836942: poo.Producto(836942, 'zapatillas', 'calzado', db_proveedores[1].RUT, 35, 329586, 'blanco'),
    642264: poo.Producto(642264, 'polearas', 'ropa', 'china', 735, 3, 'rosa'),
    624426: poo.Producto(624426, 'zapatos', 'calzado', db_proveedores[2].RUT, 24, 735735, 'rojo'),
    264624: poo.Producto(264624, 'poleron', 'ropa', 'EU', 45, 4685732, 'verde'),
    624642: poo.Producto(624642, 'chaqueta', 'ropa', 'EU', 36, 753, 'azul'),
    624643: poo.Producto(624643, 'guantes', 'accesorio', 'EU', 753, 735, 'naranja')
}

# (self, run, nombre, apellido, seccion)
db_vendedores = {
    15666777: poo.Vendedor(15666777, 'Juan', 'Perez', 1, '2020-10-01'),
    15222777: poo.Vendedor(15222777, 'Pedro', 'Gonzalez', 2, '2018-12-03'),
}

# reporte estadistico del inventario
print("")
poo.reporte_estadistica_productos(db_productos)

db_clientes[4].get_saldo()

#Simulación de venta
v = db_vendedores[15222777].vender(id_venta = 1,
                            cliente = db_clientes[4],
                            productos = [db_productos[624642]],
                            cantidad = [12]
                            )

print("\n\n")
print(dc.f("Después de la venta:",'red'))
print("")

poo.reporte_estadistica_productos(db_productos)

db_clientes[4].get_saldo()

#def __init__(self, dirección, mts2,sku, nombre, categoria, proveedor, stock, valor_neto, color):
sucursalA = poo.Sucursal('calle', 11, 200, "93939393", "polo", "osososos", "lolo" , 40, 121212, "verde")
bodega1 = poo.BodegaPrincipal("dirección", "mts2", 325)

print("\n")
sucursalA.control_stock(bodega1)

print(dc.jumbo(f'mro y __mro__:'))
print(poo.Sucursal.mro())
print(poo.Sucursal.__mro__)

print(dc.jumbo(f'Saldo sucursalA: {sucursalA.stock}'))
# print(db_vendedores[15222777].vender2)

# Excepcion.test(5)
ex1 = Excepcion.sin_stock(bodega1)
ex2 = Excepcion.sin_stock(sucursalA)
ex3 = Excepcion.max_compra(v[0])
ex4 = Excepcion.promedio_cero(db_clientes[5].promedio_compras())


print("")
dc.tof(ex1,'red','green')
dc.tof(ex2,'red','green')
dc.tof(ex3,'red','green')
dc.tof(ex4,'red','green')
print("")

