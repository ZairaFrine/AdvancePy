#---Inicio HW---
def hw():
  print("Hello World")
#--- Fin HW ---

def printTicket( carrito ):
  print(carrito)
  print(f"Total: $ { carrito.getTotal() } mxn")
  print(f"Usted ahorro: $ { carrito.getTotalDcto() } mxn")