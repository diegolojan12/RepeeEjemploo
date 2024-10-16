print("Banco de Loja")

saldo = int(10000)


print("Bienvenid@, seleccione la acción que desea realizar")
print("Tu saldo inicial es de: $", saldo)

while True:
  print("1. Depositar dinero")
  print("2. Retirar dinero")
  print("3. Consultar saldo")
  print("4. Salir")

  opcion = input("Ingrese el proceso a realizar: ")
  if opcion == '1':
    deposito = int(input("Ingrese el monto a depositar: "))
    saldo = saldo + deposito
    print(f"Depósito realizado exitosamente. Su saldo actual es de ${saldo}")

  elif opcion == '2':
    retirar = int(input("Ingrese el monto a retirar: "))
    if saldo < retirar:
      print("No se pudo realizar el proceso debido a que su saldo es insuficiente")
    else:
      saldo = saldo - retirar
      print(f"Retiro realizado exitosamente. Su saldo actual es de ${saldo}")

  elif opcion == '3':
    print(f"Su saldo actual es de $: {saldo}")

  elif opcion == '4':
    print("Gracias por utilizar nuestro servicio")
    break