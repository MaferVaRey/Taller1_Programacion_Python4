lado1 = float(input('Ingrese el valor del lado a: '))
lado2 = float(input('Ingrese el valor del lado b: '))
lado3 = float(input('Ingrese el valor del lado c: '))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print('No es un triángulo válido')
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print('EL triángulo es escaleno')
elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
    print('El triángulo es isósceles')
elif lado1 == lado2 == lado3:
    print('El triángulo es equilátero')
