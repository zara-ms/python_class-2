
# Se define la clase "piso" con 4 atributos
class piso():
    numero = 0
    escalera = ''
    ventanas = 0
    cuartos = 0
    # Se le da la funcion "timbre" a cada piso
    def timbre(self):
        print("ding dong")

    # __init__ se usa para "llenar" los 4 atributos preestablecidos
    def __init__(self, numero, ventanas, escaleras, cuartos):
        self.numero = numero
        self.ventanas = ventanas
        self.escaleras = escaleras
        self.cuartos = cuartos

class planta_baja(piso):
    puerta_principal = True
    # Se da un override del timbre para la "planta_baja"
    def timbre(self):
        print("bzzzzzp")

class azotea(piso):
    antena = True
    # Se da un override del timbre para la "azotea"
    def timbre(self):
        print("Fuera de servicio")

primer_piso = piso(2,"si",4,2)

cuarto_visitas = planta_baja(1,4,"si",1)

segundo_piso = azotea(3,0,"no",0)

cuarto_visitas.timbre()