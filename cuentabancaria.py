banco = {}
clientes = {}

while True:
    print('   Menu   ')
    print('1. Crear Cuenta')
    print('2. Depositar Dinero')
    print('3. Solicitar Credito')
    print('4. Retirar Dinero')
    print('5. Pago Cuota Credito')
    print('6. Cancelar Cuenta')
    print('7. Ver Información de Cuenta')
    print('8. Agregar Producto al Portafolio')
    print('9. Ver Historial de Transacciones')
    print('10. Salir')
    print()

    opcion = input('Porfavor ingrese una opcion: ')

    if opcion == "1":
        nombre = input('Porfavor ingrese su nombre: ')
        cc = input('Porfavor ingrese su cédula de ciudadanía (CC): ')
        email = input('Porfavor ingrese su email: ')
        edad = int(input('Porfavor ingrese su edad: '))
        contacto = input('Porfavor ingrese su contacto (opcional): ')
        movil = input('Porfavor ingrese su móvil: ')
        telefono_fijo = input('Porfavor ingrese su teléfono fijo: ')
        pais = input('Porfavor ingrese su país: ')
        departamento = input('Porfavor ingrese su departamento: ')
        ciudad = input('Porfavor ingrese su ciudad: ')
        direccion = input('Porfavor ingrese su dirección: ')

        print('Porfavor recuerda que tu clave es igual a tu cédula')

        if cc in clientes:
            print('Esta cédula ya está registrada.')
        else:
            print('Cuenta registrada con éxito.')
            clientes[cc] = {
                "nombre": nombre,
                "cc": cc,
                "email": email,
                "edad": edad,
                "contacto": contacto,
                "movil": movil,
                "telefono_fijo": telefono_fijo,
                "ubicacion": {
                    "pais": pais,
                    "departamento": departamento,
                    "ciudad": ciudad,
                    "direccion": direccion
                },
                "productos": [],
                "saldo": 0,
                "credito_solicitado": 0,
                "historial": []
            }

    elif opcion == "2":
        cc = input('Porfavor ingrese su cédula: ')

        if cc in clientes:
            monto = int(input('Porfavor ingrese el monto para depositar: '))

            if monto >= 0:
                clientes[cc]['saldo'] += monto
                clientes[cc]['historial'].append({
                    "id": len(clientes[cc]['historial']) + 1,
                    "fecha": "2025-08-13",  # Ejemplo de fecha, este campo puede automatizarse si es necesario
                    "valor": monto,
                    "tipo": "Depósito"
                })
                print(f'El saldo fue ingresado exitosamente a su cuenta. Saldo actual: {clientes[cc]["saldo"]}')
            else:
                print("El monto debe ser un valor positivo.")
        else:
            print('La cédula ingresada no tiene cuenta')

    elif opcion == "3":
        cc = input('Porfavor ingrese su cédula: ')

        if cc in clientes:
            monto_credito = int(input('Porfavor ingrese el monto de crédito que desea solicitar: '))

            if monto_credito > 0:
                clientes[cc]['credito_solicitado'] += monto_credito
                clientes[cc]['saldo'] += monto_credito
                clientes[cc]['historial'].append({
                    "id": len(clientes[cc]['historial']) + 1,
                    "fecha": "2025-08-13",
                    "valor": monto_credito,
                    "tipo": "Crédito solicitado"
                })
                print(f'Crédito solicitado por {monto_credito} exitosamente. Nuevo saldo: {clientes[cc]["saldo"]}. Crédito pendiente: {clientes[cc]["credito_solicitado"]}')
            else:
                print("El monto de crédito debe ser positivo.")
        else:
            print('La cédula ingresada no tiene cuenta')

    elif opcion == "4":
        cc = input('Porfavor ingrese su cédula: ')

        if cc in clientes:
            monto_retiro = int(input('Porfavor ingrese el monto que desea retirar: '))

            if monto_retiro > 0 and clientes[cc]['saldo'] >= monto_retiro:
                clientes[cc]['saldo'] -= monto_retiro
                clientes[cc]['historial'].append({
                    "id": len(clientes[cc]['historial']) + 1,
                    "fecha": "2025-08-13",
                    "valor": monto_retiro,
                    "tipo": "Retiro"
                })
                print(f'Has retirado {monto_retiro} exitosamente. Nuevo saldo: {clientes[cc]["saldo"]}')
            else:
                print("Fondos insuficientes o monto no válido.")
        else:
            print('La cédula ingresada no tiene cuenta')

    elif opcion == "5":
        cc = input('Porfavor ingrese su cédula: ')

        if cc in clientes:
            monto_pago = int(input('Porfavor ingrese el monto a pagar por su crédito: '))

            if monto_pago > 0 and clientes[cc]['credito_solicitado'] >= monto_pago:
                clientes[cc]['credito_solicitado'] -= monto_pago
                clientes[cc]['historial'].append({
                    "id": len(clientes[cc]['historial']) + 1,
                    "fecha": "2025-08-13",
                    "valor": monto_pago,
                    "tipo": "Pago de crédito"
                })
                print(f'Has pagado {monto_pago} de tu crédito. Crédito pendiente: {clientes[cc]["credito_solicitado"]}. Saldo actual: {clientes[cc]["saldo"]}')
            else:
                print("Monto de pago no válido o no hay crédito suficiente.")
        else:
            print('La cédula ingresada no tiene cuenta')

    elif opcion == "6":
        cc = input('Porfavor ingrese su cédula: ')

        if cc in clientes:
            del clientes[cc]
            print(f'La cuenta con cédula {cc} ha sido cancelada exitosamente.')
        else:
            print('La cédula ingresada no tiene cuenta')

    elif opcion == "7":
        cc = input('Porfavor ingrese su cédula: ')

        if cc in clientes:
            cliente = clientes[cc]
            print(f"\n--- Información de Cuenta ---")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Cédula: {cliente['cc']}")
            print(f"Email: {cliente['email']}")
            print(f"Edad: {cliente['edad']}")
            print(f"Teléfono móvil: {cliente['movil']}")
            print(f"Teléfono fijo: {cliente['telefono_fijo']}")
            print(f"Ubicación: {cliente['ubicacion']['pais']}, {cliente['ubicacion']['departamento']}, {cliente['ubicacion']['ciudad']}, {cliente['ubicacion']['direccion']}")
            print(f"Saldo disponible: {cliente['saldo']}")
            print(f"Total de crédito solicitado: {cliente['credito_solicitado']}")
            print(f"Crédito pendiente a pagar: {cliente['credito_solicitado']}")
            print(f"--- Fin de la Información ---\n")
        else:
            print('La cédula ingresada no tiene cuenta')

    elif opcion == "8":
        cc = input('Porfavor ingrese su cédula: ')

        if cc in clientes:
            print("Seleccione el tipo de producto que desea agregar al portafolio:")
            print("1. Cuenta Ahorros")
            print("2. Cuenta Corriente")
            print("3. CDT")
            print("4. Crédito Libre Inversión")
            print("5. Crédito Davivienda")
            print("6. Crédito Compra Automóvil")
            tipo_producto = input("Seleccione el número del producto: ")

            if tipo_producto == "1":
                nombre_producto = "Cuenta Ahorros"
            elif tipo_producto == "2":
                nombre_producto = "Cuenta Corriente"
            elif tipo_producto == "3":
                nombre_producto = "CDT"
            elif tipo_producto == "4":
                nombre_producto = "Crédito Libre Inversión"
            elif tipo_producto == "5":
                nombre_producto = "Crédito Davivienda"
            elif tipo_producto == "6":
                nombre_producto = "Crédito Compra Automóvil"
            else:
                print("Opción no válida.")
                continue

            fecha_inicio = input("Ingrese la fecha de inicio del producto: ")
            estado = input("Ingrese el estado del producto (activo, inactivo, cancelado, pagado): ")
            saldo = input("Ingrese el saldo del producto: ")

            producto_detalle = {
                "id_producto": len(clientes[cc]['productos']) + 1,
                "nombre_producto": nombre_producto,
                "fecha_inicio": fecha_inicio,
                "estado": estado,
                "saldo": saldo,
                "historial": []
            }

            clientes[cc]['productos'].append(producto_detalle)
            print(f'Producto {nombre_producto} agregado exitosamente al portafolio.')
        else:
            print('La cédula ingresada no tiene cuenta')

    elif opcion == "9":
        cc = input('Porfavor ingrese su cédula: ')

        if cc in clientes:
            print("\n--- Historial de Transacciones ---")
            for transaccion in clientes[cc]['historial']:
                print(f"ID: {transaccion['id']} | Fecha: {transaccion['fecha']} | Valor: {transaccion['valor']} | Tipo: {transaccion['tipo']}")
            print("--- Fin del Historial ---\n")
        else:
            print('La cédula ingresada no tiene cuenta')

    elif opcion == "10":
        print("Gracias por usar el sistema bancario. ¡Hasta luego!")
        break

    else:
        print('Opción no válida. Por favor ingrese una opción entre 1 y 10.')
