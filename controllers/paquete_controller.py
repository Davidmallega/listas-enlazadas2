from models.paquete import ListaDobleEnlazada

class PaqueteController:
    def __init__(self):
        self.lista_paquetes = ListaDobleEnlazada()

    def insertar_paquete(self, codigo_seguimiento, origen, destino, estado):
        self.lista_paquetes.insertar_paquete(codigo_seguimiento, origen, destino, estado)

    def eliminar_paquete(self, codigo_seguimiento):
        return self.lista_paquetes.eliminar_paquete(codigo_seguimiento)

    def obtener_paquete(self, codigo_seguimiento):
        return self.lista_paquetes.buscar_paquete(codigo_seguimiento)

    def actualizar_estado(self, codigo_seguimiento, nuevo_estado):
        return self.lista_paquetes.actualizar_estado(codigo_seguimiento, nuevo_estado)

    def obtener_todos_los_paquetes(self):
        return self.lista_paquetes.obtener_todos_los_paquetes()
