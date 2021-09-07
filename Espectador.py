from Participante import Participante


class Espectador(Participante):
    def __init__(self, nombre: str, apellido: str, sexo: str,
                 lugar_procedencia: str, doc_identidad: str,
                 telefono: str, email: str, numero_registro: str,
                 grado_academico: str):
        super().__init__(nombre, apellido, sexo, lugar_procedencia,
                         doc_identidad, telefono, email)
        self.__numero_registro = numero_registro
        self.__grado_academico = grado_academico

    def get_numero_registro(self):
        return self.__numero_registro

    def set_numero_registro(self, numero_registro: str):
        self.__numero_registro = numero_registro

    def get_grado_academico(self):
        return self.__grado_academico

    def set_grado_academico(self, grado_academico: str):
        self.__grado_academico = grado_academico

    def imprimir(self):
        print("Hola: " + self.get_nombre())