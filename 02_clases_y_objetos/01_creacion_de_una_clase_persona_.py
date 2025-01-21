#definicion de una clase

class Persona:
    
    def inicializar_persona(self, nombre, apellido):
        # creamos los atributos de la clase
        self.nombre = nombre # usando self accedemos al atributo de nuestra clase
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f''' Persona:
              Nombre: {self.nombre}
              Apellido: {self.apellido}''')
        
        
#creacion de objetos

if __name__ == '__main__':
    
    #creacion de un primer objeto
    persona1 = Persona()# se crea un objeto vacio
    persona1.inicializar_persona('Romulo','Felizola')
    persona1.mostrar_persona()
    
    #creamos el segundo objeto
    persona2 = Persona() # creamos un objeto vacio en memoria
    persona2.inicializar_persona('Augusto','Ottaviani')
    persona2.mostrar_persona()