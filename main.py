# SPRINT 4

import dalecolor as dc

dc.clear()
# print("\n\n\n\n\n\n\n")


def total(bod_stock):
    total = 0 
    for i in bod_stock:
        total += bod_stock[i]
    return total


class Bodega:
    def __init__(self, id, nombre, total_stock, proveedores, stock):
        self.id = id
        self.nombre = nombre
        self.__cantidad_total_de_productos = total_stock
        self.proveedores = proveedores
        self.stock = stock
    
    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)

    def eliminar_proveedor(self, proveedor_eliminar):
        self.proveedores.remove(proveedor_eliminar)

    transf_tipo_ = ''
    transf_cantidad_ = 0

    def transferencia_bodega(self, inst_bodega1, inst_bodega2, transf_tipo = None, transf_cantidad = None):
        # if tipo is None or cantidad is None:
        #     num_pro = len(inst_bodega1.stock)
        #     n = random.randint(num_pro)
        inst_bodega1[transf_tipo] += transf_cantidad
        inst_bodega2[transf_tipo] -= transf_cantidad
        transf_tipo_ = transf_tipo
        transf_cantidad_ = transf_cantidad

    def transferencia_mostrar_tipo(self):
        x = self.transf_tipo_
        print(x)

    def transferencia_mostrar_total(self):
        x = self.transf_cantidad_
        print(x)

    def mostrar_total_de_productos_en_bodega(self):
        total(self.stock)


class Proveedor:
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo

    def inscripcion_en_bodega(self, bodega):
        if self.id not in bodega.proveedores:
            bodega.proveedores.append(self.id)

    def mod_producto(self, nuevo_tipo):
        self.tipo = nuevo_tipo


# anchor_User_class
class User:
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo

    def consulta(self, bodega):
        consulta = []
        if self.tipo == 'administrador':
            consulta.append(len(bodega.proveedores))
            consulta.append(bodega.stock)
        elif self.tipo == 'operario':
            consulta.append(len(bodega.proveedores))

        return consulta

                     # id   nombre   tipo
proveedor_1 = Proveedor(1, 'China', 'pc')
proveedor_2 = Proveedor(2, 'Korea', 'phone')
proveedor_3 = Proveedor(3, 'Japón', 'tablet')
proveedor_4 = Proveedor(4, 'Taiwán', 'watch')
proveedor_5 = Proveedor(5, 'Vietnam', 'tv')


# id, nombre, total_stock, proveedores, stock
bod = {
    1 : ['A', [proveedor_1.id, proveedor_2.id, proveedor_3.id], {'pc' : 1000, 'phone' : 1200}],
    2 : ['B', [proveedor_2.id, proveedor_3.id], {'phone' : 1600, 'tablet' : 500}],
    3 : ['C', [proveedor_4.id, proveedor_5.id], {'watch' : 600, 'tv' : 400}]
}



                # id nombre,    total_stock       proveedores    stock
bodega_a = Bodega(1, bod[1][0], total(bod[1][2]), bod[1][1], bod[1][2])
bodega_b = Bodega(2, bod[2][0], total(bod[2][2]), bod[2][1], bod[2][2])
bodega_c = Bodega(3, bod[3][0], total(bod[3][2]), bod[3][1], bod[3][2])

# anchor_User_instance
            # id   nombre    tipo
user_0 = User(35, 'andres', 'administrador')
user_1 = User(235, 'beatriz', 'operario')
user_2 = User(861, 'camilo', 'operario')


# - - - - - - - - - - - - - - -

print(dc.jumbo(f"PRE-CAMBIOS"))

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
# print(f"l: {dc.anchor('# anchor_User_class')} class")
# print(f"l: {dc.anchor('# anchor_User_instance')} instance")

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
# print(f"l: {dc.anchor('# anchor_User_class')} class")
# print(f"l: {dc.anchor('# anchor_User_instance')} instance")

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
# print(f"l: {dc.anchor('# anchor_User_class')} class")
# print(f"l: {dc.anchor('# anchor_User_instance')} instance")












# print{bodega_a.__cantidad_total_de_productos}
print(dc.jumbo(f"CAMBIOS)"))


proveedor_2.inscripcion_en_bodega(bodega_c)
# print(f"l: {dc.anchor('# anchor_inscripcion_en_bodega')-1} execute method -> proveedor_2.inscripcion_en_bodega(bodega_c)")

proveedor_2.mod_producto('car')
# print(f"l: {dc.anchor('# anchor_mod_producto')-1} execute method -> proveedor_2.mod_producto('car')")




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
print(f"consulta:")
# print(dc.jumbo(f"consulta (line {dc.anchor('anchor-03')})"))
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
