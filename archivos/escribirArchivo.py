f = open("demo.txt","a")
f.write("El archivo tiene mas contenido")
f.close()

#Abrir el archivo
f = open("demo.txt","r")
print(f.read())