#!/usr/bin/python3
from easysnmp import snmp_get
import sys
import textwrap


res = snmp_get('1.3.6.1.4.1.2435.2.3.9.4.2.1.5.5.8.0', hostname=sys.argv[1],community='public', version=2).value.encode('latin-1').hex()



char_List = textwrap.wrap(res,14)
result = ''

for string_ in char_List:
    #print(string_[0])
    #print(string_[1])
    if string_[0] == '8' and string_[1] == '1':
        result = string_

hexa = result[12] + result[13]

valor = int(hexa, 16)

print(valor)
