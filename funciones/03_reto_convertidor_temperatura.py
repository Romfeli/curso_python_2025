print('*** Convertidor de Temperatura ***')

#funcion que convierte de celsius a farenheit

def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32) * 5 / 9


#realizacon las pruebas de conversion

celsius = float(input('proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
#imprimimos el resultado
print(f'{celsius} C a F: {resultado:.2f}')


fahrenheit = float(input('proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
#imprimimos el resultado
print(f'{fahrenheit} F a C: {resultado:.2f}')
