print("---CONVERSOR DE TEMPERATURA DE CELSIUS PARA FAHRENHEIT---")
celsius = int(input("Quantos graus celsius esta fazendo? "))
fahrenheit = celsius * 9 / 5 + 32

if celsius == 0:
 print('A conversão de 0º é equivalente a 32º na escala de Fahrenheit.')

else:
 print(f'A conversão de {celsius}º é equivalente a {fahrenheit}º na escala de Fahrenheit.')