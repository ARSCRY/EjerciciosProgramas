f = open("demo.txt","w")
f.write("Perdon, he sobreescrito en el archivo")
f.close()

#abrir de nuevo:
f = open("demo.txt","r")
print(f.read())