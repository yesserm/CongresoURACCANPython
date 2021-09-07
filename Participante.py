class Participante:
    def __init__(self, nombre: str, apellido: str, sexo: str,
                 lugar_procedencia: str, doc_identidad: str,
                 telefono: str, email: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sexo = sexo
        self.__lugar_procedencia = lugar_procedencia
        self.__doc_identidad = doc_identidad
        self.__telefono = telefono
        self.__email = email

        # métodos para nombres
    def get_nombre(self)->str:
        return self.__nombre

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

        # métodos para apellidos
    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido: str):
        self.__apellido = apellido

        # métodos para sexo
    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo: str):
        self.__sexo = sexo

        # métodos para lugar_procedencia
    def get_lugar_procedencia(self):
        return self.__lugar_procedencia

    def set_lugar_procedencia(self, lugar_procedencia: str):
        self.__lugar_procedencia = lugar_procedencia

        # métodos para doc_identidad
    def get_doc_identidad(self):
        return self.__doc_identidad

    def set_doc_identidad(self, doc_identidad: str):
        self.__doc_identidad = doc_identidad

        # métodos para telefono
    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono: str):
        self.__telefono = telefono

        # métodos para email
    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email
