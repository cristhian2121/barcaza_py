from .container import Container

class Solid(Container):
    type_container = 'solido'

    def __init__(self, peso):
        Container.__init__(self, peso)

    def __str__(self):
        return self.type_container+', '+ str(self.peso)