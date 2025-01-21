print('*** Calculadora con funciones ***')

def mostrar_menu():
    print(f'''
          Operaciones que puedes realizar
          1. Suma
          2. Resta
          3.Multiplicacion
          4.Division
          5. Sair
          
          
        ''')
    return int(input('escoge una opcion: '))

def pedir_valores():
    operando1 = float(input('dame el valor 1: '))
    operando2 = float(input('dame el valor 2: '))
    return operando1,operando2

def ejecutar_operacion(opcion, salir):
    #solicityar los valores de los operandos
    if 1 <= opcion <= 4: # solo si estamos en este rango
        operando1,operando2 = pedir_valores()  # hacemos otra variablew para pedir los nuemros
    if opcion == 1:#sumar
        resultado = operando1 + operando2
        print(f'el resultado de sumar es : {resultado}\n')
    elif opcion == 2: #resta
            resultado = operando1 - operando2
            print(f'el resultado de resta es : {resultado}\n')
    elif opcion == 3: #multiplicaicon
                resultado = operando1 * operando2
                print(f'el resultado de multiplicaicon es : {resultado}\n')
    elif opcion == 4: #division
                resultado = operando1 / operando2
                print(f'el resultado de division es : {resultado}\n')            
    elif opcion == 5:
                print('Saliendo del programa de calculadora')
                salir = True
    else:
        print('opcion invalida selecciona otra opcion \n')
    return salir
        

#programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)