# Ejercicio 29
# Conversión de tipos

moneda = int(input("Monedas de 2 euros:"))
moneda2 = int(input("Monedas de 1 euro:"))
moneda3 = int(input("Monedas de 50 céntimos:"))
moneda4 = int(input("Monedas de 20 céntimos:"))
moneda5 = int(input("Monedas de 10 céntimos:"))


total_euros = moneda * 2 + moneda2
total_centimos = moneda3 * 50 + moneda4 * 20 + moneda5 * 10
total_euros = total_euros + total_centimos // 100
total_centimos = total_centimos % 100

print(total_euros," euros y",total_centimos," céntimos.")

print("Programa echo por Josue Eduard Guerra Lovato")