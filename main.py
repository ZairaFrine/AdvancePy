from lib import *

obj_poly_1 = Poligono(5,18)
print(obj_poly_1)
print(f"Num lados: {obj_poly_1.numLado }")
print( obj_poly_1.nomPoly() )

obj_poly_2 = PoligonoRegular(5, 15, 7)
print( obj_poly_2)
print( obj_poly_2.nomPoly() )
print(f"El perímetro es: {obj_poly_2.periPoly()}" )
#print(obj_poly_2.periPoly() )
print( f"El área es: {obj_poly_2.getArea()}" )
print( f"El área es mayor a 200??: {obj_poly_2.chkArea()}" )

obj_poly_2.setColor("Verde vejiga")

print(obj_poly_2.color)

num1 = "10"
num2 = 0 

try:
    div = num1 / num2
#except ZeroDivisionError:
#    print("No puedes dividir entre cero...")
#except TypeError:
#    print("No puedes divdir Strings entre Numeros")
except Exception as e:
    print(f"Error desconocido: {e} ")

print("Hello Boys and Girls")
print("Meew")





