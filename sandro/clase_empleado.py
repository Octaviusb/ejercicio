import pickle
from datetime import datetime
class Empleado:
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__salario = salario
        self.__dni = dni
        self.__fecha_vinculacion = fecha_vinculacion
    
    def obtener_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
    def __str__(self):
        return (f"{self.obtener_nombre_completo()}, DNI: {self.__dni}, "
                f"Edad: {self.__edad}, Salario: {self.__salario}, "
                f"Fecha de Vinculación: {self.__fecha_vinculacion}")
    
    # Métodos de acceso (Getters)
    def get_dni(self):
        return self.__dni
    
    def get_nombre(self):
        return self.__nombre
    # Métodos de modificación (Setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self, apellido):
        self.__apellido = apellido