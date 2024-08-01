import os

if os.path.exists("mi_archivo.txt"):
    os.remove("mi_archivo.txt")
else:
    print("El archivo no existe")