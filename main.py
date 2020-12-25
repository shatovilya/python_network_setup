from netmiko import (
    ConnectHandler,
    NetMikoAuthenticationException,
    NetMikoTimeoutException
)

import json
import re
with open(r'devices.json', 'r') as in_file:
    devices = json.load(in_file)
sw1 =sw2 = sw3 = fw1 = hq1 = br1 = ''
try:
    sw1 = ConnectHandler(**devices['sw1'])
    print('Connect to sw1 successfull')
except:
    print('Connection to sw1 failed!')

try:
    sw2 = ConnectHandler(**devices['sw2'])
    print('Connect to sw2 successfull')
except:
    print('Connection to sw2 failed!')

try:
    sw3 = ConnectHandler(**devices['sw3'])
    print('Connect to sw3 successfull')
except:
    print('Connection to sw3 failed!')


try:
    fw1 = ConnectHandler(**devices['fw1'])
    print('Connect to fw1 successfull')
except:
    print('Connection to fw1 failed!')

try:
    hq1 = ConnectHandler(**devices['hq1'])
    print('Connect to hq1 successfull')
except:
    print('Connection to hq1 failed!')

try:
    br1 = ConnectHandler(**devices['br1'])
    print('Connect to br1 successfull')
except:
    print('Connection to br1 failed!')

# O1
conf_sw1 = sw1.send_command('sh run | s hostname').lower().find('sw1')
conf_fw1 = fw1.send_command('sh run | i hostname').lower().find('fw1')
if conf_fw1 != -1 and conf_fw1 != -1:
    print('O1: passed')
else:
    print('O1: failed')

# O2
conf_sw1 = sw1.send_command('sh run | s domain-name').lower().find('worldskills.ru')
conf_hq1 = hq1.send_command('sh run | s domain name').lower().find('worldskills.ru')
conf_fw1 = fw1.send_command('sh run | i domain-name').lower().find('worldskills.ru')
if conf_fw1 != -1 and conf_fw1 != -1 and conf_hq1 != -1:
    print('O2: passed')
else:
    print('O2: failed')

# O3

conf_sw2 = sw2.send_command('sh run | s username').lower().find('wsruser privilege 15 secret')
conf_sw3 = sw3.send_command('sh run | s username').lower().find('wsruser privilege 15 secret')
conf_fw1 = re.findall(r'wsruser password \S+ \S+ privilege 15', fw1.send_command('sh run | i username').lower())
if conf_fw1 != -1 and conf_sw2 != -1 and conf_sw3 != -1:
    print('O3: passed')
else:
    print('O3: failed')

# O4

conf_br1 = br1.send_command('sh run | s enable').lower().find('secret 5')
conf_sw3 = sw3.send_command('sh run | s enable').lower().find('secret 5')
conf_fw1 = re.findall('password', fw1.send_command('sh run | i enable').lower())
if len(conf_fw1) != 0 and conf_br1 != -1 and conf_sw3 != -1:
    print('O4: passed')
else:
    print('O4: failed')

# O5

conf_hq1 = hq1.send_command('sh run | s service').lower().find('no service password-encryption')
conf_fw1 = fw1.send_command('sh run | i password').lower().find('password encryption aes')
if conf_fw1 != -1 and conf_hq1 == -1:
    print('O5: passed')
else:
    print('O5: failed')

# O6

conf_hq1 = hq1.send_command('sh run | s aaa')
conf_sw2 = sw2.send_command('sh run | s aaa')
print('O6  ################hq1################')
print(conf_hq1)
print('O6  ################sw2################')
print(conf_sw2)

# O7
print('O7  ################hq1################')
print('manual')

# O8

conf_hq1 = hq1.send_command('sh run | s aaa')

print('O8  ################hq1################')
print(conf_hq1)

# O9

conf_hq1 = hq1.send_command('sh run | s aaa')
print('O9  ################hq1################')
print(conf_hq1)

# 10
print('10  ################pc1################')
print('manual')

# 11
print('11  ################sw1################')
conf_sw1 = sw1.send_command('sh vtp status')
print(conf_sw1)
# 12
print('12  ################sw2################')
conf_sw2 = sw2.send_command('sh vtp status')
print(conf_sw2)
print('12  ################sw3################')
conf_sw3 = sw3.send_command('sh vtp status')
print(conf_sw3)

# 13
print('13  ################sw1################')
conf_sw1 = sw1.send_command('sh int trunk')
print(conf_sw1)

# 14-15
print('14-15  ################sw1################')
conf_sw1 = sw1.send_command('sh etherch sum')
print(conf_sw1)

# 16-17
print('16-17  ################sw1################')
conf_sw1 = sw1.send_command('sh span')
print(conf_sw1)
print('16-17  ################sw2################')
conf_sw2 = sw2.send_command('sh span')
print(conf_sw2)
print('16-17  ################sw3################')
conf_sw3 = sw3.send_command('sh span')
print(conf_sw3)

# 18
print('18  ################sw1################')
conf_sw1 = sw1.send_command('sh run int e0/0')
print(conf_sw1)

# 19
print('19  ################sw1################')
conf_sw1 = sw1.send_command('sh vlan bri')
print(conf_sw1)
print('19  ################sw2################')
conf_sw2 = sw2.send_command('sh vlan bri')
print(conf_sw2)
print('19  ################sw3################')
conf_sw3 = sw3.send_command('sh vlan bri')
print(conf_sw3)

# 20
print('20  ################hq1################')
conf_hq1 = hq1.send_command('sh run int e0/0')
print(conf_hq1)

# 21
print('21  ################sw1################')
conf_sw1 = sw1.send_command('sh ip int bri')
print(conf_sw1)

# 22-23
print('22-23  ################sw1################')
conf_sw1 = sw1.send_command('sh vlan bri')
print(conf_sw1)
print('22-23  ################sw2################')
conf_sw2 = sw2.send_command('sh vlan bri')
print(conf_sw2)
print('22-23  ################sw3################')
conf_sw3 = sw3.send_command('sh vlan bri')
print(conf_sw3)

# 24-25
print('24-25  ################fw1################')
conf_fw1 = fw1.send_command('sh ip addr')
print(conf_fw1)

# 26-28
print('26-28  ################br1################')
conf_br1 = br1.send_command('sh ip int bri')
print(conf_br1)



print('29  ################ failed')
print('30  ################ failed')
print('31  ################ failed')
print('32  ################ failed')

# 33
print('33  ################hq1################')
conf_hq1 = hq1.send_command('sh bgp sum')
print(conf_hq1)

# 34
print('34  ################fw1################')
conf_fw1 = fw1.send_command('sh bgp sum')
print(conf_fw1)

# 35
print('35  ################br1################')
conf_br1 = br1.send_command('sh bgp sum')
print(conf_br1)

print('36  ################ failed')
print('37  ################ failed')

# 38
print('38  ################br1################')
conf_br1 = br1.send_command('sh ntp stat')
print(conf_br1)

print('39  ################ failed')
print('40  ################ failed')

# 41
print('41  ################hq1################')
conf_hq1 = hq1.send_command('sh run | s dhcp')
print(conf_hq1)

# 42
print('42  ################br1################')
conf_br1 = br1.send_command('sh pppoe sum')
print(conf_br1)

print('43  ################ failed')
print('44  ################ failed')
print('45  ################ failed')
print('46  ################ failed')
print('47  ################ failed')
print('48  ################ failed')
print('49  ################ failed')
print('50  ################ failed')
print('51  ################ failed')
print('52  ################ failed')