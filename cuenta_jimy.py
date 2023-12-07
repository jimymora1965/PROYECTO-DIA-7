import os
import re  # Importamos el módulo de expresiones regulares para la validación del correo

class Persona:
    def __init__(self, nombre, apellido, correo):
        self.nombre = self.validar_letras("nombre", nombre)
        self.apellido = self.validar_letras("apellido", apellido)
        self.correo = self.validar_correo(correo)

    def validar_letras(self, campo, valor):
        while not valor.isalpha():
            print(f"Error: El {campo} debe contener solo letras.")
            valor = input(f"Ingrese su {campo}: ")
        return valor

    def validar_correo(self, correo):
        while not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            print("Error: El correo debe contener un formato válido.")
            correo = input("Ingrese su correo: ")
        return correo

class Cliente(Persona):
    def __init__(self, nombre, apellido, correo, numero_cuenta, balance=0):
        super().__init__(nombre, apellido, correo)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nCorreo: {self.correo}\nNúmero de cuenta: {self.numero_cuenta}\nBalance de ahorros: ${self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Depósito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    correo_cl = input("Ingrese su correo: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    balance_inicial = float(input("Ingrese el balance inicial de ahorros: "))
    cliente = Cliente(nombre_cl, apellido_cl, correo_cl, numero_cuenta, balance_inicial)
    return cliente

def inicio():
    while True:
        mi_cliente = crear_cliente()
        print(mi_cliente)
        opcion = ''

        while opcion.upper() != 'S':
            print('Elije: Depositar (D), Retirar (R), o Salir (S)')
            opcion = input()

            if opcion == 'D':
                try:
                    monto_dep = float(input("Monto a depositar: "))
                    mi_cliente.depositar(monto_dep)
                except ValueError:
                    print("Error: Ingrese un monto válido.")
            elif opcion == 'R':
                try:
                    monto_ret = float(input("Monto a retirar: "))
                    mi_cliente.retirar(monto_ret)
                except ValueError:
                    print("Error: Ingrese un monto válido.")
            print(mi_cliente)
        
        limpiar_consola()
        reiniciar = input("¿Desea realizar otra transacción? (Sí/No): ")
        if reiniciar.upper() != 'S':
            break

    print("Gracias por operar en Banco Python")

inicio()
