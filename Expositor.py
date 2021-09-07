from Participante import Participante


class Expositor(Participante):
    def __init__(self, nombre: str, apellido: str, sexo: str,
                 lugar_procedencia: str, doc_identidad: str,
                 telefono: str, email: str, cantida_p: int,
                 titulos: str):
        super().__init__(nombre, apellido, sexo, lugar_procedencia,
                         doc_identidad, telefono, email)
        self.__cantidad_p = cantida_p
        self.__titulos = titulos

    def get_cantidad_p(self):
        return self.__cantidad_p

    def set_cantidad_p(self, cantidad_p: int):
        self.__cantidad_p = cantidad_p

    def get_titulos(self):
        return self.__titulos

    def set_titulos(self, titulos: str):
        self.__titulos = titulos