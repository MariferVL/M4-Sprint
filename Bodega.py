""" clase Bodega
Atributos:
● Id
● Nombre
● __Cantidad total de productos
● Proveedores ( lista de objetos proveedores )
● Un dato con los productos y su respectivo stock  
            #json?
Métodos:
● Agregar_proveedor
● Eliminar_proveedor
● Transferir productos de una bodega a otra bodega.
● Cantidad total de productos transferidos.
● Mostrar total de tipos de productos transferidos.
● Mostrar total de productos en bodega. 

Cada Bodega tiene:
    # Operarios: Acceso a número de proveedores por bodega.
    # Administradores: acceso a número de proveedores por bodega y el stock.

"""

class Bodega:
    def __init__(self, ID, name, total_prod):
        self.ID=ID
        self.name=name
        self.total_prod=total_prod
        self.proveedores=[]

    
    def agregar_proveedor():
        pass

    def eliminar_proveedor():
        pass
    
    def warehouses_transference():
        pass

    def display_transference():
        pass

    def display_types():
        pass
    


# Parent class Users is declared.
class Employee: 
    # instance attributes.
    def __init__(self,firstname,surname,ID,password):
        # keys are initialized with their respective values
        self.firstname= firstname
        self.surname= surname
        self.ID= ID
        self.__password = password
        # self.birthDay = birthDay
        # self.birthMonth = birthMonth
        # self.birthYear = birthYear 
        # self.email= email
        # self.contact = contact 

    def display_provider():
        pass
        
    def get_password(self):
        return self.__password

#Check identity to filter who has access to the information.
    def verify_identity(self,users):
        print("\nEliminacón de Usuarios: \n")
        print("\t Ingrese nombre de usuario/ID de la cuenta a eliminar:")
        d_user = input().capitalize()
        if d_user in users.keys():
            i=0
            while i < 3:
                i += 1
                password= input('> Ingrese su contraseña:')
                if password == users[d_user][self.__password]:
                    #
                    return users
                else:
                    print('Contraseña Incorrecta \n')
                if i == 3:
                    print("Se acabaron tu número de intentos. \n")
                    return
        else:
            print(f"\n{d_user} no está registrado. \n")
            # menu()


class warehouseman(Employee):
    def __init__(self, firstname, surname, ID, password):
        super().__init__(firstname, surname, ID, password)

class manager(Employee):
    def __init__(self, firstname, surname, ID, password):
        super().__init__(firstname, surname, ID, password)

    def display_inventory():
        pass
