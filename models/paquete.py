class Nodo:
    def __init__(self, codigo_seguimiento, origen, destino, estado):
        self.codigo_seguimiento = codigo_seguimiento
        self.origen = origen
        self.destino = destino
        self.estado = estado
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar_paquete(self, codigo_seguimiento, origen, destino, estado):
        nuevo_nodo = Nodo(codigo_seguimiento, origen, destino, estado)
        if self.head is None:
            self.head = self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.tail
            self.tail = nuevo_nodo

    def eliminar_paquete(self, codigo_seguimiento):
        actual = self.head
        while actual:
            if actual.codigo_seguimiento == codigo_seguimiento:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.head:
                    self.head = actual.siguiente
                if actual == self.tail:
                    self.tail = actual.anterior
                del actual
                return True
            actual = actual.siguiente
        return False

    def buscar_paquete(self, codigo_seguimiento):
        actual = self.head
        while actual:
            if actual.codigo_seguimiento == codigo_seguimiento:
                return actual
            actual = actual.siguiente
        return None

    def actualizar_estado(self, codigo_seguimiento, nuevo_estado):
        paquete = self.buscar_paquete(codigo_seguimiento)
        if paquete:
            paquete.estado = nuevo_estado
            return True
        return False

    def obtener_todos_los_paquetes(self):
        paquetes = []
        actual = self.head
        while actual:
            paquetes.append(actual)
            actual = actual.siguiente
        return paquetes
