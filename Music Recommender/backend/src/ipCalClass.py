import flet as ft
from flet import *
import UIElements as UIE

class ipCalClass(object):

    # Diccionario que almacena las máscaras de red por su valor
    list_masc = {
        0:'0.0.0.0',
        1:'128.0.0.0',
        2:'192.0.0.0',
        3:'224.0.0.0',
        4:'240.0.0.0',
        5:'248.0.0.0',
        6:'252.0.0.0',
        7:'254.0.0.0',
        8:'255.0.0.0',
        9:'255.128.0.0',
        10:'255.192.0.0',
        11:'255.224.0.0',
        12:'255.240.0.0',
        13:'255.248.0.0',
        14:'255.252.0.0',
        15:'255.254.0.0',
        16:'255.255.0.0',
        17:'255.255.128.0',
        18:'255.255.192.0',
        19:'255.255.224.0',
        20:'255.255.240.0',
        21:'255.255.248.0',
        22:'255.255.252.0',
        23:'255.255.254.0',
        24:'255.255.255.0',
        25:'255.255.255.128',
        26:'255.255.255.192',
        27:'255.255.255.224',
        28:'255.255.255.240',
        29:'255.255.255.248',
        30:'255.255.255.252',
        31:'255.255.255.254',
        32:'255.255.255.255',
    }

    def __init__(self, ip_addr = ''):

        # Inicialización de variables principales        
        self.IP_princ = [0, 0, 0, 0]
        self.IP_masc = 0
        self.IP_masc_int = [0, 0, 0, 0]

        # División de la dirección IP y la máscara de red
        self.masc = ip_addr.split('/')
        self.div_masc = self.masc[1]
        self.IP_div = self.masc[0].split('.')
        
        # Validación y asignación de valores para la dirección IP principal
        for i in range(len(self.IP_div)):
            self.IP_princ[i] = int(self.IP_div[i])
            if self.IP_princ[i] > 255: 
                raise ValueError
            if i > 3: 
                raise ValueError

        # Validación y asignación de la máscara de red
        self.IP_masc = int(self.div_masc)
        if self.IP_masc > 32 or self.IP_masc < 0: 
            raise ValueError
        if not self.IP_masc:
            test = self.obtener_clase()
            if test == 'A':
                self.IP_masc = 8
            if test == 'B':
                self.IP_masc = 16
            if test == 'C':
                self.IP_masc = 24
            if test == 'D':
                print('Direccion multicast, usando /24')
                self.IP_masc = 24
            if test == 'E':
                print('Direccion reservada, usando /24')
                self.IP_masc = 24
            del test

        self.IP_masc_div = (self.list_masc.get(self.IP_masc)).split('.')
        self.IP_mascDotted = self.list_masc.get(self.IP_masc)

        for index in range(len(self.IP_masc_div)):
            self.IP_masc_int[index] = int(self.IP_masc_div[index])

    # Método para obtener la clase de la dirección IP
    def obtener_clase(self):
        self.ipClass = ''
        test = self.ip_calc_bin()
        if test[0] == '0':
            self.ipClass = 'A'
        if test[:2] == '10':
            self.ipClass = 'B'
        if test[:3] == '110':
            self.ipClass =  'C'
        if test[:4] == '1110':
            self.ipClass = 'D'
        if test[:4] == '1111':
            self.ipClass = 'E'
        return self.ipClass

    # Método para obtener la designación de la dirección IP
    def obtener_designacion(self):
        self.ipDesignation = ''
        test = self.ip_calc_bin()
        if test[0] == '0' and self.IP_masc == 0:
            self.ipDesignation = 'Bloqueo de Internet'
        elif test[0] == '0' and self.IP_princ[0] == 10 and self.IP_masc >= 8:
            self.ipDesignation = 'Direccion privada'
        elif test[0] == '0' and self.IP_princ[0] == 10 and self.IP_masc <= 8:
            self.ipDesignation = 'Direccion privada - Supernetting'
        elif test[0] == '0' and self.IP_masc <= 8:
            self.ipDesignation = 'Internet Publica - Supernetting'
        elif test[0] == '0' and self.IP_princ[0] == 127:
            self.ipDesignation = 'Direccion para localhost'
        elif test[:2] == '10' and self.IP_princ[0] == 172 and self.IP_princ[1] == 16 and self.IP_masc >= 12:
            self.ipDesignation = 'Direccion privada'
        elif test[:2] == '10' and self.IP_princ[0] == 172 and self.IP_princ[1] == 16 and self.IP_masc <= 12:
            self.ipDesignation = 'Direccion privada - Supernetting'
        elif test[:2] == '10' and self.IP_masc <= 16:
            self.ipDesignation = 'Direccion privada - Supernetting'
        elif test[:3] == '110' and self.IP_princ[0] == 192 and self.IP_princ[2] == 2 and self.IP_masc == 24:
            self.ipDesignation =  'TEST-NET'
        elif test[:3] == '110' and self.IP_princ[0] == 192 and self.IP_princ[1] == 168 and self.IP_masc >= 16:
            self.ipDesignation =  'Direccion privada'
        elif test[:3] == '110' and self.IP_princ[0] == 192 and self.IP_princ[1] == 168 and self.IP_masc <= 16:
            self.ipDesignation =  'Direccion privada - Supernetting'
        elif test[:3] == '110' and self.IP_princ[0] == 169 and self.IP_princ[1] == 254 and self.IP_masc == 16:
            self.ipDesignation =  'Link Local'
        elif test[:3] == '110' and self.IP_masc <= 24:
            self.ipDesignation =  'Direccion publica - Supernetting'
        elif test[:4] == '1110':
            self.ipDesignation = 'Multi-Cast'
        elif test[:4] == '1111':
            self.ipDesignation = 'Reservada'
        else:
            self.ipDesignation = 'Direccion publica'
        return self.ipDesignation


    # Método para calcular la representación de la IP en formato entero
    def ip_calc_int(self):
        self.intIP = '{}.{}.{}.{}'.format(self.IP_princ[0], self.IP_princ[1],self.IP_princ[2], self.IP_princ[3])
        return self.intIP

    # Metodo para convertir la dirección IP en formato binario.
    def ip_calc_bin(self):
        self.binIP = '{:08b}.{:08b}.{:08b}.{:08b}'.format(self.IP_princ[0], self.IP_princ[1],self.IP_princ[2], self.IP_princ[3])
        return self.binIP

    # Metodo para calcular la mascara de red en formato binario
    def calc_masc_bin(self):
        self.binMask = '{:08b}.{:08b}.{:08b}.{:08b}'.format(self.IP_masc_int[0], self.IP_masc_int[1],self.IP_masc_int[2], self.IP_masc_int[3])
        return self.binMask

    # Metodo para calcular la mascara de red de la ip en hexadecimal
    def ip_calc_hex(self):
        self.hexIP = '{:02x}.{:02x}.{:02x}.{:02x}'.format(self.IP_princ[0], self.IP_princ[1],self.IP_princ[2], self.IP_princ[3])
        return  self.hexIP

    # Metodo para calcular mascara de red en hexadecimal
    def calc_masc_hex(self):
        self.hexMask = '{:02x}.{:02x}.{:02x}.{:02x}'.format(self.IP_masc_div[0], self.IP_masc_div[1],self.IP_masc_div[2], self.IP_masc_div[3])
        return self.hexMask

    # Metodo para calcular la marcara de red en entero
    def calc_net_int(self):
        self.netID = [0, 0, 0, 0]
        for index in range(len(self.IP_princ)):
            self.netID[index] = self.IP_princ[index] & self.IP_masc_int[index]
        self.netIDInt = "{}.{}.{}.{}".format(self.netID[0], self.netID[1], self.netID[2], self.netID[3])
        return self.netIDInt
    
    # Metodo para calcular la mascara de red en binario
    def calc_net_bin(self):
        self.netID = [0, 0, 0, 0]
        for index in range(len(self.IP_princ)):
            self.netID[index] = self.IP_princ[index] & self.IP_masc_int[index]
        self.netIDBin = '{:08b}.{:08b}.{:08b}.{:08b}'.format(self.netID[0], self.netID[1],self.netID[2], self.netID[3])
        return self.netIDBin

    # Metodo para calcular el wildcard en enteros
    def calc_wilc_int(self):
        self.wildNet = [0, 0, 0, 0]
        for index in range(len(self.IP_masc_int)):
            self.wildNet[index] = 255 - self.IP_masc_int[index]
        self.wildNetInt = '{}.{}.{}.{}'.format(self.wildNet[0], self.wildNet[1], self.wildNet[2],self.wildNet[3])
        return self.wildNetInt

    # Metodo para calcular el wildcard en binario
    def calc_wilnet_bin(self):
        self.wildNet = [0, 0, 0, 0]
        for index in range(len(self.IP_masc_int)):
            self.wildNet[index] = 255 - self.IP_masc_int[index]
        self.wildNetBin = '{:08b}.{:08b}.{:08b}.{:08b}'.format(self.wildNet[0], self.wildNet[1],self.wildNet[2], self.wildNet[3])
        return self.wildNetBin

    # Metodo para calcular el broadcast en enteros
    def calc_broad_int(self):
        self.broadcast = [0, 0, 0, 0]
        self.calc_wilc_int()
        for index in range(len(self.IP_masc_int)):
            self.broadcast[index] = self.IP_princ[index] | self.wildNet[index]
        self.broadcastInt = '{}.{}.{}.{}'.format(self.broadcast[0], self.broadcast[1],self.broadcast[2], self.broadcast[3])
        return self.broadcastInt

    # Metodo para calcular el broadcast en binarios
    def calc_broad_bin(self):
        self.broadcast = [0, 0, 0, 0]
        self.calc_wilc_int()
        for index in range(len(self.IP_masc_int)):
            self.broadcast[index] = self.IP_princ[index] | self.wildNet[index]
        self.broadcastBin = '{:08b}.{:08b}.{:08b}.{:08b}'.format(self.broadcast[0], self.broadcast[1], self.broadcast[2], self.broadcast[3])
        return self.broadcastBin

    # Metodo para calcular el rango de direcciones IP validas
    def calc_rango(self):
        self.firstIP = self.netID
        self.firstIP[3] += 1
        self.lastIP = self.broadcast
        self.lastIP[3] -= 1
        self.firstIPInt = '{}.{}.{}.{}'.format(self.firstIP[0], self.firstIP[1],self.firstIP[2], self.firstIP[3])
        self.lastIPInt = '{}.{}.{}.{}'.format(self.lastIP[0], self.lastIP[1],self.lastIP[2], self.lastIP[3])
        if self.IP_masc == 32:
            host_route = 'Ruta de host: host único'
            return host_route, self.ip_calc_int(), 'None'
        elif self.IP_masc == 31:
            point_to_point = 'Punto a punto (RFC 3021): dos direcciones IP, solo válidas si la subred cero está habilitada'
            return point_to_point, self.netIDInt, self.broadcastInt
        else:
            return '', self.firstIPInt, self.lastIPInt

    # Metodo para calcular cantidad de host y bits de hosts
    def calc_host(self):
        self.hostsBits = 32 - self.IP_masc
        self.hosts = (2 ** self.hostsBits) - 2
        if self.IP_masc == 32:
            return 1, 0
        elif self.IP_masc == 31:
            return 2, 1
        if self.IP_masc <= 30:
            return self.hosts, self.hostsBits

    # Metodo para imprimir toda la informacion en la tabla
    def imp_infor(self, ip_addr):
        UIE.UIElements.ip_text.value = "IP: "+ip_addr
        tabla = UIE.UIElements.table_info
        tabla.columns=[
            DataColumn(ft.Text("Nombre")),
            DataColumn(ft.Text("Resultado")),
        ]
        ex_tab = (
            DataRow(
                    cells=[
                        DataCell(ft.Text('Direccion IP:')),
                        DataCell(ft.Text('{:15}-   {:35}'.format(self.ip_calc_int(), self.ip_calc_bin()))),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(ft.Text('Mascara de red:')),
                        DataCell(ft.Text('{:15}-   {:35}'.format(self.IP_mascDotted, self.calc_masc_bin()))),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(ft.Text('Mascara Wildcard:')),
                        DataCell(ft.Text('{:15}-   {:35}'.format(self.calc_wilc_int(), self.calc_wilnet_bin()))),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(ft.Text('Direccion subred:')),
                        DataCell(ft.Text('{:15}-   {:35}'.format(self.calc_net_int(), self.calc_net_bin()))),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(ft.Text('Broadcast:')),
                        DataCell(ft.Text('{:15}  -   {:35}'.format(self.calc_broad_int(), self.calc_broad_bin()))),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(ft.Text('# de Hosts:')),
                        DataCell(ft.Text('{}'.format(self.calc_host()[0], self.calc_host()[1]))),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(ft.Text('Red tipo Clase: ')),
                        DataCell(ft.Text('{}'.format(self.obtener_clase()))),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(ft.Text('Designacion de red :')),
                        DataCell(ft.Text('{}'.format(self.obtener_designacion()))),
                    ],
                ),
        )
        temp = self.calc_rango()
        new_rows=(
            DataRow(
                cells=[
                    DataCell(ft.Text('Primera ip valida:')),
                    DataCell(ft.Text(''+temp[1])),
                ],
            ),
            DataRow(
                cells=[
                    DataCell(ft.Text('Utima ip valida:')),
                    DataCell(ft.Text(''+temp[2])),
                ],
            ),
        )
        tabla.rows=ex_tab+new_rows