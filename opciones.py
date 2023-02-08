from abc import ABC, abstractmethod
import datetime
from time import sleep
import os

class Persona(ABC):
    _idpersona = 0
    def __init__(self,nombre,estado):
        Persona._idpersona += 1
        self.nombre = nombre
        self.estado = estado
    
    @property
    def idpersona(self):
        return self._idpersona

    @abstractmethod
    def mostrarDatos(self):
        pass

class Cliente(Persona):
    clientes = []

    def __init__(self, nombre, cedula, estado):
        super().__init__(nombre, estado)
        self.idcliente = str(len(Cliente.clientes)+1)
        self.nombre = nombre
        self.cedula = cedula
        self.estado = estado
    
    def validar_nombre(self):
        return self.nombre.isalpha()
    
    def validar_cedula(self):
        return self.cedula.isdigit() and len(self.cedula) == 10

    def guardar_en_archivo(self):
        with open("archivos/clientes.txt", "a") as archivo:
            archivo.write(f"{self.idcliente},{self.nombre},{self.cedula},{self.estado}\n")
            
    def mostrarDatos(self):
        with open('archivos/clientes.txt', 'r') as archivo:
            for linea in archivo:
                print(linea)
    
    @classmethod
    def crear_cliente(cls):
        nombre = input("Ingrese el nombre: ")
        cedula = input("Ingrese la cédula: ")
        estado = input("Ingrese el estado (True/False): ")
        cliente = cls(nombre, cedula, estado)
        if cliente.validar_nombre() and cliente.validar_cedula():
            cliente.guardar_en_archivo()
            cls.clientes.append(cliente)
            print("Cliente creado exitosamente.")
        else:
            print("Error al crear cliente.")
        
            
class Factura:
    _idfactura = 0
    def __init__(self):
        Factura._idfactura += 1
        self.cliente = Cliente.crear_cliente()
        self.fecha = datetime.date.today()
        self.total = float(input("Ingrese el total de la factura: $"))
        self.estado = input("Ingrese el estado de la factura (True/False): ")
    
    @property
    def idfactura(self):
        return self._idfactura
    
    def mostrarDatos(self):
        with open('archivos/facturas.txt', 'r') as archivo:
            for linea in archivo:
                print(linea)

    def guardar_factura(self):
        with open('archivos/facturas.txt', 'a') as f:
            f.write(f"{self._idfactura}, {self.cliente.nombre}, {self.fecha}, {self.total}, {self.estado}\n")
        print("Registro ingresado exitosamente")
        sleep(0.8)
        os.system("cls")
        
class Detcredito:
    iddetcredito = 0
    def __init__(self):
        self.iddetcredito = Detcredito.iddetcredito + 1
        self.aamm = input("Ingrese el año y mes (yyyymm): ")
        self.cuota = float(input("Ingrese la cuota: "))
        self.detpago = []
        self.estado = input("Ingrese el estado (True/False): ") == "True"
        
    def mostrarDatos(self):
        pass

    def agregarpago(self):
        pago = Pago()
        pago.realizarpago()
        self.detpago.append(pago)


class CabCredito:
    interes = 0.16
    _idcabcredito = 0
    def __init__(self):
        self._idcabcredito = CabCredito._idcabcredito + 1
        self.factura = Factura()
        self.fecha = input("Ingresar fecha: ")
        self.deuda = float(input("Ingrese la deuda: "))
        self.numerocuota = int(input("Ingrese el numero de cuotas: "))
        self.cuota = float(input("Ingrese el valor de cada cuota: "))
        self.saldoainicial = float(input("Ingrese el saldo inicial: "))
        self.detcredito = []
        self.estado = input("Ingrese el estado del credito (True/False): ")
    
    @staticmethod
    def get_interes():
        return CabCredito.interes
    
    def agregar_detcredito(self, detcredito):
        self.detcredito.append(detcredito)
        
    def mostrarDatos(self):
        with open('archivos/creditos.txt', 'r') as archivo:
            for linea in archivo:
                print(linea)

    def guardar_credito(self):
        with open('archivos/creditos.txt', 'a') as f:
            f.write(f"{self._idcabcredito}, {self.factura.idfactura}, {self.fecha}, {self.deuda}, {self.numerocuota}, {self.cuota}, {self.saldoainicial}, {self.estado}\n")
            for det in self.detcredito:
                f.write(f"{det.iddetcredito}, {det.numero}, {det.fecha}, {det.saldo}\n")
            print("Registro ingresado exitosamente")
            sleep(0.8)
            os.system("cls")
            
class Calculo(ABC):
    def realizar_pago(self):
        pass

class Pago:
    _idpago = 0
    def __init__(self):
        self._idpago = Pago._idpago + 1
        self.fechapago = input("Ingrese la fecha de pago (dd/mm/yyyy): ")
        self.valor = float(input("Ingrese el valor del pago: "))
        
    def mostrarDatos(self):
        with open('archivos/pagos.txt', 'r') as archivo:
            for linea in archivo:
                print(linea)      
        
    def realizar_pago(self):
        with open("archivos/pagos.txt", "a") as file:
            file.write(f"{self._idpago},{self.fechapago},{self.valor}\n")
        print("Registro ingresado exitosamente")
        sleep(0.8)
        os.system("cls")
            
def menu():
    while True:
        print("-"*10,"Menú principal", "-"*10)
        print("1. Clientes")
        print("2. Facturas")
        print("3. Créditos")
        print("4. Pagos")
        print("5. Consulta general")
        print("6. Salir")
        print("-"*36)
        opc = input("Seleccione una opción: ")
        if opc == "1":
            Cliente.crear_cliente()
        elif opc == "2":
            facturas1 = Factura()
            facturas1.guardar_factura()
        elif opc == "3":
            creditos1 = CabCredito()
            creditos1.guardar_credito()
        elif opc == "4":
            pagos1 = Pago()
            pagos1.realizar_pago()
        elif opc == "5":
            os.system("cls")
            consulta_general()
        elif opc == "6":
            break
        else:
            print("Opción inválida.")
            
def consulta_general():
    while True:
        print("="*10, "Consulta General", "="*10)
        print("1. Mostrar Clientes")
        print("2. Mostrar Facturas")
        print("3. Mostrar Credito")
        print("4. Mostrar Pagos")
        print("5. Volver al menu principal")
        print("="*38)
        opc = input("Seleccione una opción: ")
        if opc == "1":
            Cliente.mostrarDatos(Cliente)
        elif opc == "2":
            Factura.mostrarDatos(Factura)
        elif opc == "3":
            CabCredito.mostrarDatos(CabCredito)
        elif opc == "4":
            Pago.mostrarDatos(Pago)
        elif opc == "5":
            os.system("cls")
            break
        else:
            print("Opción inválida.")
        
if __name__ == "__main__":
    menu()