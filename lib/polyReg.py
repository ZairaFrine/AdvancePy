class poligono:
  def __init__(self, numLados, largoLados):
    self.numLados = numLados
    self.largoLados = largoLados
    pass
    
  def __str__(self):
    return f"Polígono de {self.numLados} y largo de lados {self.largoLados}"
    
  def nombrePoligono(self):
    pass
  
  def perimetro(self):
    periPoli = self.numLados * self.largoLados
    return periPoli
      
class poliReg(poligono):
  
  def __init__(self, numLados, largoLados, apotema):
    self.apotema = apotema
    poligono.__init__(self, numLados, largoLados)
    pass
  
  def area(self):
    areaPoli = (poligono.perimetro(self) * self.apotema)/2
    return areaPoli
  
  def __str__(self):
    return f"Polígono regular de {self.numLados}, largo de lados {self.largoLados} y apotema: {self.apotema}"
  
  
