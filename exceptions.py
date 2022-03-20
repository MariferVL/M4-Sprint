from poo import Vendedor
import dalecolor as dc
class Excepcion():

    # Chequear si stock de producto1= Producto(), sucursal1=Sucursal() y bodega1=Bodega()   > 0
    def sin_stock(x):
        try:
            x.stock >= 1
        except:
            print(dc.f(dc.jumbo(f'{x} no tiene stock'),"red"))
            return True
        else:
            print(dc.f(dc.jumbo(f'El stock actual es de {x.stock} unidades.'),"green"))
            return False

    # Chequear que carro de clientes tenga máx 10 productos. De lo contrario, enviar mensaje de error.
    def max_compra(carrito):
        # cantidad=  productos_venta[key][0] 
        
        try:
            carrito < 10
            if carrito > 10: 
                raise Exception("Carrito tiene mas de 10 productos")

            # delete = carrito - 10
            # if delete >= 1:
            #     carrito = carrito - delete
            #     print(f' Se eliminaron {delete} items de su carrito')
            #     print(carrito)
            # else:
            #     print(f'Su carro contiene {carrito} unidades.')        
        
        except Exception as error:
            print(dc.f(dc.jumbo(f"Error, limite máximo: {error}"),"red"))
            return True
        else:
            print(dc.f(dc.jumbo(f"Gracias por comprar en nuestra tienda"),"green"))
            return False
            


    # Obtener valor promedio de compras del cliente y enviar mensaje en caso de que sea 0.
    def promedio_cero(prom):
 
        try:
            prom[1] == 0
            if prom[1] == 0: raise Exception("falla")
        except Exception as error:
            print(dc.f(dc.jumbo("no ha realizado compras"),"red"))
            return True
        else:
            print(dc.f(dc.jumbo(f'La compra promedio de **cliente {prom[0]}** es: ${prom[1]}'),"green"))
            return False



# cantidad = productos_venta[key][0]


    def test(x):
        print(x)