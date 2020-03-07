from .container import Container

class Liquid(Container):
    type_container = 'liquido'

    def __init__(self, peso):
        Container.__init__(self, peso)
        
    def __str__(self):        
        return self.type_container+", "+str(self.peso)


                                        