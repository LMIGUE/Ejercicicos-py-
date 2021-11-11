# Defina una clase con variables para **name** y **country**.
# Luego defina un método que pertenece a la clase. El método 
# propósito es imprimir una frase que usa las variables.
class Network:
    def __init__(self, marca, plataforma, Nombre, Ubicacion, IOS, IPv4_mask):
        self.marca = marca
        self.plataforma = plataforma
        self.Nombre = Nombre                                       
        self.Ubicacion = Ubicacion
        self.IOS = IOS
        self.IPv4_mask = IPv4_mask

    def Configuration (self):
        print("Hola mi dispositivo es un " + self.Nombre  + " y sus caracteristicas son: " + "\n" + " Plataforma: " + self.plataforma + "\n" + " Marca: "+ self.marca + "\n" + " Ubicacion: " + self.Ubicacion + "\n" + " IOS: " + self.IOS + "\n" + " IPV4_mask: " + self.IPv4_mask + ".")

# Primera instancia de la clase Location
conf1 = Network("Cisco", "virtual","Router", "Pasadizo", "1841", "192.168.1.1/24")
# Llamar a un método de la clase instanciada
conf1.Configuration()
conf2 = Network("Linksys", "wifi","Switch_Multiplayer", "Oficina", "MR9600", "172.16.1.1/26")
conf2.Configuration()

