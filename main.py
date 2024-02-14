from lib import *

#obj_poly_1 = Poligono(5,18)
#print(obj_poly_1)
#print(f"Num lados: {obj_poly_1.numLado }")
#print( obj_poly_1.nomPoly() )
#
#obj_poly_2 = PoligonoRegular(5, 15, 7)
#print( obj_poly_2)
#print( obj_poly_2.nomPoly() )
#print(f"El perímetro es: {obj_poly_2.periPoly()}" )
##print(obj_poly_2.periPoly() )
#print( f"El área es: {obj_poly_2.getArea()}" )
#print( f"El área es mayor a 200??: {obj_poly_2.chkArea()}" )
#
#obj_poly_2.setColor("Verde vejiga")
#
#print(obj_poly_2.color)
#
#num1 = "10"
#num2 = 0 
#
#try:
#    div = num1 / num2
##except ZeroDivisionError:
##    print("No puedes dividir entre cero...")
##except TypeError:
##    print("No puedes divdir Strings entre Numeros")
#except Exception as e:
#    print(f"Error desconocido: {e} ")


cart1=carritou("ABC123")
cart2=carritou("DEF456")
cart3=carritou("GHI789")



art1=articulo(10256,"Coca-Cola","Canada Dry 500ml")
art1.setPrecio(25.00)
art1.setPeso(350)
art1.setDcto(10)
art1.setInv(10)
#print(art1)


art2=articulo(30601,"Sabritas","Rancheritos 500gr")
art2.setPrecio(40.00)
art2.setPeso(500)
art2.setDcto(25)
art2.setInv(5)
#print(art2)


art3=articulo(98765,"Tia Rosa","Cuernitos 150gr")
art3.setPrecio(30.00)
art3.setPeso(150)
art3.setInv(15)
#print(art3)


cart1.addArticulo( art1 )
cart1.addArticulo( art1 )
cart1.addArticulo( art1 )
cart1.addArticulo( art2 )
cart1.addArticulo( art3 )

printTicket(cart1)
printTicket(cart2)
printTicket(cart3)