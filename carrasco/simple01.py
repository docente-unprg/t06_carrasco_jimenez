# Programa 01
import os
usuario, mensaje="",""

#INPUT VIA OS
usuario=os.sys.argv[1]

# PROCESSING
# Si el usuario es admin, mostrar acceso concedido
if ( usuario == "admin"):
    mensaje="Acceso concedido"

#OUTPUT
print(mensaje)
