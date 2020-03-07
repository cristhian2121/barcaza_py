from random import random
from .liquid_container import Liquid
from .solid_cotainer import Solid
from .container import Container

class Barcaza:
    filas = 0
    capacidad = 0
    posicion = 0
    container_solid = 0
    container_liquid = 0
    container_list_liquid = []
    container_list_solid = []
    diff_weigth = 0.25 # sen toneladas
    percentage_medium_weigth = 0.3 # esto esta en %
    medium_weigth_number = 0

    def __init__(self):
        pass        

    def inputs(self):
        self.filas = int(input("¿Cuantas filas tiene su barcaza? "))
        self.capacidad = int(input("¿Cuantos container va a transportar? "))
        #self.mostrar_filas()
        self.set_weigth()

    '''
    Configurar los pesos de los contenedores de forma aleatorea
    '''
    def set_weigth(self):
        # mitad liquidos y mitad solidos
        self.container_liquid = self.capacidad // 2
        self.container_solid = self.capacidad - self.container_liquid

        #envia a fill_container la cantidad de container
        self.container_list_liquid = self.fill_container(self.container_liquid, 'liquido')
        self.container_list_solid = self.fill_container(self.container_solid, 'solido')
        self.medium_weigth()
        self.order_container()
    
    def fill_container(self, len_list, type_container):
        list_container = []
        for x in range(len_list):
            container = {}
            if type_container == 'liquido': container = Liquid(round(random(),2))
            else: container = Solid(round(random(),2))

            list_container.append(container) # en toneladas
        return list_container
    
    def mostrar_filas(self):
        print(f'Sus filas son:  {self.filas}')
    
    def medium_weigth(self):
        number_total = 0
        for container in self.container_list_liquid:
            number_total += container.peso
        for container in self.container_list_solid:
            number_total += container.peso

        self.total = float(number_total)
        self.medium_weigth_number = float(self.total * self.percentage_medium_weigth)
    
    def order_container(self):
        center_list = []
        number_center_list = []
        parada = False
        type_container_array = False # Es container_list_liquid
        while not parada:
            container_deleted = {}
            if type_container_array:
                container_deleted = self.container_list_solid.pop()
                center_list.append(container_deleted)
            else:
                container_deleted = self.container_list_liquid.pop()
                center_list.append(container_deleted)
            number_center_list.append(container_deleted.peso)
            sum_center_list = float(sum(number_center_list))
        
            if sum_center_list > (self.medium_weigth_number - 0.5) and sum_center_list < (self.medium_weigth_number + 0.5):
                # termina
                parada = True
            type_container_array = not type_container_array
        #for de prueba
        print('Contenedores del centro', self.total)
        for container in center_list:
            print(container)

        

        

