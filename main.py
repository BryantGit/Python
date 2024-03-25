#Calculadora de IMS
#IMC = Peso / (Altura * Altura)
# IMC < 19 -> DElgado
# IMC 20 y 25 -> Normal
# IMC 26 y 30 -> SObrepeso
# IMC > 30 -> Obesidad

peso = int(input('Ingrese su peso en Kilos: '))
altura = float(input('Ingrese su altura en metros: '))

imc = peso / (altura * altura)
print('Su IMC es: ',str(imc))

if imc < 19:
    print('Su estado es: delgado')
if imc >= 20 and imc <26: 
    print('Su estado es: normal')
if imc >= 26 and imc <=30: 
    print('Su estado es: Obesidad')
if imc > 30:
    print('Su estado es: anormal')




