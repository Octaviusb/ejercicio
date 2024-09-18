
class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        super().__init__(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        self.__empleados_a_cargo = []
    
    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.__empleados_a_cargo.append(empleado)
    
    def obtener_empleados_a_cargo(self):
        return [emp.obtener_nombre_completo() for emp in self.__empleados_a_cargo]
    
    def __str__(self):
        empleados = ', '.join(self.obtener_empleados_a_cargo())
        return (f"{super().__str__()}, Empleados a Cargo: [{empleados}]")
    
    # Métodos de acceso
    def get_empleados_a_cargo(self):
        return self.__empleados_a_cargo