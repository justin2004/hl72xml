#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import string
import random

def getPort():
    return str(random.randrange(20000,55000))

def getString(size):
   return join(random.choice('1234567890abcde') for x in range(size))
#UDP
#s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Estableciendo a 5 Segundos como máximo para recibir respuesta.
s.settimeout(5)

host = "127.0.0.1"
source = "192.168.1.10"
puerto = 7070

print 'Servidor Destino: (host,puerto) : ',(host,puerto)

# Nos conectamos con el servidor
s.connect((host,puerto))

portSIP=getPort()

# Mensaje que se enviará

mensaje  =  "MSH|^~\&|Xxxxx|SENDING|RECEIVING FACILITY|20101223202939-0400||ADT^A40|102|P|2.3.1||||||||\n"
mensaje +=  "EVN|A40|20101223202939-0400||||\n"
mensaje +=  "PID||P12345^^^ISSUER|P12345^^^ISSUER||PATIENT^TEST^M^^^^||19741018|M|||10808 FOOTHILL BLVD^^Francisco Mucamonga^CA^91730^US||(909)481-5872^^^sales@Xxxx.com|(909)481-5800x1||M||12345|286-50-9510|||\n"
mensaje +=  "MRG|758026^^^ISSUER|||758026^^^ISSUER|\n"

message = "MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\n"
message += "PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|19620320|F|||153 FERNWOOD DR.^\n"
message += "^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\n"
message += "OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730|||||||||\n"
message += "555-55-5555^PRIMARY^PATRICIA P^^^^MD^^|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\n"
message += "OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\n"

mess  = "MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\n"
mess += "PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|19620320|F|||153 FERNWOOD DR.^"
mess += "^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\n"
mess += "OBR|1|845439^GHH OE|1045813^GHH LAB|15545^GLUCOSE|||200202150730|||||||||"
mess += "555-55-5555^PRIMARY^PATRICIA P^^^^MD^^|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\n"
mess += "OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\n"




# Envío la informacióm
#s.send(mensaje)
s.send(mess)

print ':::::>Finalizando la conexión'
s.close()

