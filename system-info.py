# getting system details with python

import sys
import wmi

s= wmi.WMI()

sys_info = s.Win32_ComputerSystem()[0]

print(f"manufacturer: {sys_info.Manufacturer}")
print(f"Model: {sys_info.Model}")
print(f"Name: {sys_info.Name}")
print(f"Number of Processors: {sys_info.NumberOfProcessors}")
print(f"System Type: {sys_info.SystemType}")
print(f"System Family: {sys_info.SystemFamily}")
