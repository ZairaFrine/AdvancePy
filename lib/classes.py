class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        pass
    
    def __str__(self):
        return f"Rectángulo de largo {self.largo} y ancho {self.ancho}"
    
    def area(self):
        return (self.largo*self.ancho)
        

    def perimetro(self):
        return 2*(self.largo+self.ancho)
    
    
