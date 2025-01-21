print('*** Calculadora de impuestos ***')

#funcion que calcla el total de un apgo incluyendo el impuesto

def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

#ejecutar la funcion

pago_sin_impuesto = float(input('Proporcione el pago sin impuestos: '))

impuesto = float(input('Proporcione el monto del impuesto: '))

pago_con_impuesto = calcular_total_pago(pago_sin_impuesto,impuesto)

print(f'pago con impuesto {pago_con_impuesto}')