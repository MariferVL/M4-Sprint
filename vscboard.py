# #1°
from types import BuiltinFunctionType


class ConTodo:
     pass

print("\n Lo que contiene la clase ConTodo: \n")
c= ConTodo()
print(dir(c))

##2°
print("\n Lo que contiene la clase objeto: \n")
o= object()
print(dir(o))

##3°  
print(type(print))
print(type(input))
print(type(isinstance))
result =isinstance(isinstance,BuiltinFunctionType)
print(result)

# #4°
# class BaseException:
#     pass
# class sintaxtError(BaseException)

# class Exception(BaseException)

# raise errareHumanumEst() 

# #5°
class errareHumanumEst(Exception):
    pass

raise errareHumanumEst("Eres humano, se entiende...") 