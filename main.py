# SPRINT 4
# para darle color a la terminal y darle formato
import dalecolor as dc
import random
# limpiar la terminal
dc.clear()
# print("\n\n\n\n\n\n\n")


def total(bod_stock):
    '''
    suma to do el stock del parametro
    bod_stock: diccionario con los productos y sus stock
    return: total del stock
    '''
    total = 0 
    for i in bod_stock:
        total += bod_stock[i]
    return total


class Bodega:
    '''
    clase que define la clase bodega
    '''

    def __init__(self, id, nombre, total_stock, proveedores, stock, transferencias = None):
        self.id = id
        self.nombre = nombre
        self.__cantidad_total_de_productos = total_stock
        self.proveedores = proveedores
        self.stock = stock
        self.transferencias = transferencias
    
    def agregar_proveedor(self, proveedor):
        if proveedor not in self.proveedores:
            self.proveedores.append(proveedor)

    def eliminar_proveedor(self, proveedor_eliminar):
        if proveedor_eliminar in self.proveedores:
            self.proveedores.remove(proveedor_eliminar)


    def transferencia_bodega(self, inst_bodega_destino, transferencia = None):
        # iniciar las variables
        key = ''
        value = ''
        if transferencia is None:
            keys_list = [*self.stock]
            key = (random.choice(keys_list)) # key
            value = (self.stock[key]) #value
        else:
            key = transferencia[0]
            value = transferencia[1]

    
        if key in [*inst_bodega_destino.stock]:
            inst_bodega_destino.stock[key] += value
        else:
            inst_bodega_destino.stock[key] = value
        
        self.stock[key] -= value
        if self.transferencias ==  None:
            self.transferencias = []
        
        self.transferencias.append([key, value])

        # print(f"---------{key} : {value}---------")

    def transferencia_mostrar_tipo(self):
        ''' muestra el tipo de transferencia'''
        last = self.transferencias[-1]
        return(last[0])

    def transferencia_mostrar_cantidad(self):
        '''muestra la ultima transferencia'''
        last = self.transferencias[-1]
        return(last[1])

    def mostrar_total_de_productos_en_bodega(self):
        '''muestra el total de productos en la bodega'''
        x = total(self.stock)
        return (f"total de productos en bodega: {x}")


class Proveedor:
    ''' clase que define el proveedor'''
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo

    def inscripcion_en_bodega(self, bodega):
        '''funcion que inscribe en una bodega'''
        if self.id not in bodega.proveedores:
            bodega.proveedores.append(self.id)

    def mod_producto(self, nuevo_tipo):
        '''funcion que modifica el tipo de producto'''
        self.tipo = nuevo_tipo



class User:
    ''' clase que define el usuario'''
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        # define el tipo de usuario
        self.tipo = tipo

    def consulta(self, bodega):
        consulta = []
        # segun el tipo de usuario muestra un resultado diferente
        if self.tipo == 'administrador':
            consulta.append(len(bodega.proveedores))
            consulta.append(bodega.stock)
        elif self.tipo == 'operario':
            consulta.append(len(bodega.proveedores))

        return consulta

# se instancia los proveedores
                     # id   nombre   tipo
proveedor_1 = Proveedor(1, 'China', 'pc')
proveedor_2 = Proveedor(2, 'Korea', 'phone')
proveedor_3 = Proveedor(3, 'Japón', 'tablet')
proveedor_4 = Proveedor(4, 'Taiwán', 'watch')
proveedor_5 = Proveedor(5, 'Vietnam', 'tv')

# se crea info para instanciar bodega

# id, nombre, total_stock, proveedores, stock
bod = {
    1 : ['A', [proveedor_1.id, proveedor_2.id, proveedor_3.id], {'pc' : 1000, 'phone' : 1200}],
    2 : ['B', [proveedor_2.id, proveedor_3.id], {'phone' : 1600, 'tablet' : 500}],
    3 : ['C', [proveedor_4.id, proveedor_5.id], {'watch' : 600, 'tv' : 400}]
}

# se instancian bodegas

                # id nombre,    total_stock       proveedores    stock
bodega_a = Bodega(1, bod[1][0], total(bod[1][2]), bod[1][1], bod[1][2])
bodega_b = Bodega(2, bod[2][0], total(bod[2][2]), bod[2][1], bod[2][2])
bodega_c = Bodega(3, bod[3][0], total(bod[3][2]), bod[3][1], bod[3][2])

# se instancian los usuarios
            # id   nombre    tipo
user_0 = User(35, 'andres', 'administrador')
user_1 = User(235, 'beatriz', 'operario')
user_2 = User(861, 'camilo', 'operario')


# - - - - - - - - - - - - - - -
# testear las funciones
print(dc.jumbo(f"instaciación usuarios, bodegas, proveedores"))

print()
dc.print_table(
    [
        ['user_0', user_0.id, user_0.nombre, user_0.tipo],
        ['user_1', user_1.id, user_1.nombre, user_1.tipo],
        ['user_2', user_2.id, user_2.nombre, user_2.tipo]
    ],
    head = ['usuario', 'id', 'nombre', 'categoria'],
    head_style = ['normal', 'white', 'CYAN'],
    style = ['normal', 'black', 'CYAN'],
    align = 'left',
    padding = ' ',
    margin = ' '
)



print()
dc.print_table(
    [
        ['bodega_a', bodega_a.id, bodega_a.nombre, bodega_a.proveedores, bodega_a.stock],
        ['bodega_b', bodega_b.id, bodega_b.nombre, bodega_b.proveedores, bodega_b.stock],
        ['bodega_c', bodega_c.id, bodega_c.nombre, bodega_c.proveedores, bodega_c.stock],
    ],
    head = ['bodega', 'id', 'nombre', 'proveedores', 'stock'],
    head_style = ['normal', 'white', 'GREEN'],
    style = ['normal', 'black', 'GREEN'],
    align = 'left',
    padding = ' ',
    margin = ' '
)



print()
dc.print_table(
    [
        ['proveedor_1', proveedor_1.id, proveedor_1.nombre, proveedor_1.tipo],
        ['proveedor_2', proveedor_2.id, proveedor_2.nombre, proveedor_2.tipo],
        ['proveedor_3', proveedor_3.id, proveedor_3.nombre, proveedor_3.tipo],
        ['proveedor_4', proveedor_4.id, proveedor_4.nombre, proveedor_4.tipo],
        ['proveedor_5', proveedor_5.id, proveedor_5.nombre, proveedor_5.tipo]
    ],
    head = ['proveedor', 'id', 'nombre', 'tipo'],
    head_style = ['normal', 'white', 'BLUE'],
    style = ['normal', 'black', 'BLUE'],
    align = 'left',
    padding = ' ',
    margin = ' '
)














# print{bodega_a.__cantidad_total_de_productos}
print(dc.jumbo(f"inscripción y modificación de productos"))

print('proveedor_2.inscripcion_en_bodega(bodega_c)')
proveedor_2.inscripcion_en_bodega(bodega_c)

print('proveedor_2.mod_producto("car")')
proveedor_2.mod_producto('car')





print()
dc.print_table(
    [
        ['bodega_a', bodega_a.id, bodega_a.nombre, bodega_a.proveedores, bodega_a.stock],
        ['bodega_b', bodega_b.id, bodega_b.nombre, bodega_b.proveedores, bodega_b.stock],
        ['bodega_c', bodega_c.id, bodega_c.nombre, bodega_c.proveedores, bodega_c.stock],
    ],
    head = ['bodega', 'id', 'nombre', 'proveedores', 'stock'],
    head_style = ['normal', 'white', 'GREEN'],
    style = ['normal', 'black', 'GREEN'],
    align = 'left',
    padding = ' ',
    margin = ' '
)

print()
dc.print_table(
    [
        ['proveedor_1', proveedor_1.id, proveedor_1.nombre, proveedor_1.tipo],
        ['proveedor_2', proveedor_2.id, proveedor_2.nombre, proveedor_2.tipo],
        ['proveedor_3', proveedor_3.id, proveedor_3.nombre, proveedor_3.tipo],
        ['proveedor_4', proveedor_4.id, proveedor_4.nombre, proveedor_4.tipo],
        ['proveedor_5', proveedor_5.id, proveedor_5.nombre, proveedor_5.tipo]
    ],
    head = ['proveedor', 'id', 'nombre', 'tipo'],
    head_style = ['normal', 'white', 'BLUE'],
    style = ['normal', 'black', 'BLUE'],
    align = 'left',
    padding = ' ',
    margin = ' '
)



print()
print()

print()
print(dc.jumbo("consultas de usurios"))

print()

dc.print_table(
    [
        ["user_0.consulta(bodega_a)", user_0.consulta(bodega_a)],
        ["user_0.consulta(bodega_b)", user_0.consulta(bodega_b)],
        ["user_0.consulta(bodega_c)", user_0.consulta(bodega_c)],
        ["", ""],
        ["user_1.consulta(bodega_a)", user_1.consulta(bodega_a)],
        ["user_1.consulta(bodega_b)", user_1.consulta(bodega_b)],
        ["user_1.consulta(bodega_c)", user_1.consulta(bodega_c)],
        ["", ""],
        ["user_2.consulta(bodega_a)", user_2.consulta(bodega_a)],
        ["user_2.consulta(bodega_b)", user_2.consulta(bodega_b)],
        ["user_2.consulta(bodega_c)", user_2.consulta(bodega_c)]
    ],
    head = ['consulta', 'salida'],
    head_style = ['normal', 'white', 'BLUE'],
    style = ['normal', 'black', 'BLUE'],
    align = 'left',
    padding = ' ',
    margin = ' '
)












# agregar y eliminar proveedor
print(dc.jumbo(f"agregar y eliminar proveedor:"))

print('agregar_proveedor id 8 en bodega_a')
bodega_a.agregar_proveedor(8)

print('eliminar_proveedor id 2 en bodega_a')
bodega_a.eliminar_proveedor(3)



#tranferencias bodegas
print(dc.jumbo("transferencia_bodega"))
bodega_a.transferencia_bodega(bodega_b)
# bodega_a.transferencia_bodega(bodega_b, transferencia = ['pc',200])

print(f"transferencia_mostrar_tipo: {bodega_a.transferencia_mostrar_tipo()}")
print(f"transferencia_mostrar_cantidad: {bodega_a.transferencia_mostrar_cantidad()}")


print()
print(f"mostrar_total_de_productos_en_bodega {bodega_a.mostrar_total_de_productos_en_bodega()}")










print(dc.jumbo("status bodega"))
dc.print_table(
    [
        ['bodega_a', bodega_a.id, bodega_a.nombre, bodega_a.proveedores, bodega_a.stock],
        ['bodega_b', bodega_b.id, bodega_b.nombre, bodega_b.proveedores, bodega_b.stock],
        ['bodega_c', bodega_c.id, bodega_c.nombre, bodega_c.proveedores, bodega_c.stock],
    ],
    head = ['bodega', 'id', 'nombre', 'proveedores', 'stock'],
    head_style = ['normal', 'white', 'GREEN'],
    style = ['normal', 'black', 'GREEN'],
    align = 'left',
    padding = ' ',
    margin = ' '
)
