#f = open("mi_archivo2.txt","x")

texto = input("Escriba en el archivo un texto: ")

f = open("mi_archivo2.txt","w")
f.write(texto)
f.close()

"Ver archivo con texto"
f = open("mi_archivo2.txt","r")
print(f.read())

