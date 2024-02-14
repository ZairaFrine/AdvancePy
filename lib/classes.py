#---- Inicio Articulo()
class articulo():
    def __init__(self, idArt, marca, nombre, precio=None, peso=None, dcto=None, inv=None):
        self.idArt = idArt
        self.marca=marca
        self.nombre=nombre
        self.precio=precio
        self.peso=peso
        self.dcto=dcto
        self.inv=inv
        pass
    
    def __str__(self):
        return f"idArt: {self.idArt} - marca: {self.marca} - nombre: {self.nombre} - precio: {self.precio} - peso: {self.peso} - dcto: {self.dcto} - inv: {self.inv}"
    
    def setPrecio(self, price):
        self.precio=price
        return 0
    
    def setPeso(self, peso):
        self.peso=peso
        return 0
    
    def setDcto(self, dcto):
        self.dcto=dcto
        return 0
    
    def setInv(self, inv):
        self.inv=inv
        return 0    
    
    def getPriceDcto(self):
        if self.dcto != None:
            precioDcto = self.precio - ( self.precio * (self.dcto/100) )
        else:
            precioDcto = self.precio
        return precioDcto
    
    def getDcto(self):
        if self.dcto != None:
            precioDcto = ( self.precio * (self.dcto/100) )
        else:
            precioDcto = 0
        return precioDcto
    
    
    
    
    pass
#---- Fin Articulo()

class carritou():
    def __init__(self, idCart):
        self.idCart = idCart
        self.objArticulos = []
        pass
    
    def __str__(self):
        printCarrito = f'Ticket #: {self.idCart} \n'
        if len(self.objArticulos) >= 1:
            for i in range(0,len(self.objArticulos),1 ):
                printCarrito += f" {self.objArticulos[i].idArt}\t{self.objArticulos[i].nombre}\t$ {self.objArticulos[i].precio} mxn\t  -${self.objArticulos[i].getDcto()} mxn\n"
        else:
                printCarrito += f" Carrito Vacío "
        return printCarrito
    
    def addArticulo(self, objArt):
        if type(objArt.inv) != type(None):
            if objArt.inv >= 1:
                objArt.inv-=1
                self.objArticulos.append( objArt )
            else:
                print(f"No hay inventario de: {objArt.nombre}")
        else:
            print("Inventario No definido")        
        return 0
    
    def getTotal( self ):
        total = 0
        for i in range(0, len(self.objArticulos),1):
            total += self.objArticulos[i].getPriceDcto()

        return total
    
    def getTotalDcto( self ):
        total = 0
        for i in range(0, len(self.objArticulos),1):
            total += self.objArticulos[i].getDcto()

        return total
        
    pass



