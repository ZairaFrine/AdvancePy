#---- Inicio clase Polígono
class Poligono:
  def __init__(self, numLado, sizeLado):
    self.numLado = numLado
    self.sizeLado = sizeLado
    pass
  
  def __str__(self):
    return f"Número de Lados: {self.numLado} y Tamaño del lado: {self.sizeLado} "
  
  def nomPoly( self ):
    match self.numLado:
      case 3:
        return "Tu polígono es un triángulo"
      case 4:
        return "Tu polígono es un cuadrado"
      case 5:
        return "Tu polígono es un pentágono"
      case _:
        return "Tu polígono no lo identifico"
  
  def periPoly( self ):
    return self.numLado * self.sizeLado
  
#---- Fin clase Polígono  

#---- Iicio clase PoligonoRegular  
class PoligonoRegular( Poligono ):
  def __init__(self, numLado, sizeLado, apotema):
    super().__init__(numLado, sizeLado)
    self.apotema = apotema
    pass
    
  def __str__(self):
    return f"Num Lado: {self.numLado}, Size Lado: {self.sizeLado}, Apotema: {self.apotema}"
  
  def getArea( self ):
    area = ((self.apotema)*(super().periPoly()))/2
    return area
  
  def chkArea( self ):
    if self.getArea() >= 200:
      return "Si"
    else:
      return "No"
    
  def setColor( self,color ):
    self.color = color
    pass
#---- Fin clase PoligonoRegular    
    
    
    
    