f = open("demo.txt","r")
#print(f.read())

#Leer solo partes del archivo
#print(f.read(10))

#leer lineas

for x in f:
    print(x)
    
f.close()

