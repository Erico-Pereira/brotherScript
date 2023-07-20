#!/usr/bin/python3
from easysnmp import snmp_get
import sys



res = snmp_get('1.3.6.1.4.1.2435.2.3.9.4.2.1.5.5.8.0', hostname=sys.argv[1],community='public', version=2).value.encode('latin-1').hex()

indice = res.find('81')
hexa = res[indice+12] + res[indice+13]
hexa = int(hexa, 16)

print(hexa)
