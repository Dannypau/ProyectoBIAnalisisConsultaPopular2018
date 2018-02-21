import matplotlib.pyplot as plt

contPositivo = 0
contNegativo = 0

with open('E:\\pruebaCuenca2.json') as lineas:
    for linea in lineas:
        if '"label": "si"' in linea:
            contPositivo += 1
        elif '"label": "no"' in linea:
            contNegativo += 1


# sample data
print(contNegativo)
print(contPositivo)


plt.figure()

labels = ['SI', 'NO']

sizes = [contPositivo,contNegativo]

colors= ['lightblue','brown']
explode =(0.2,0)

plt.pie(sizes, explode=explode,labels=labels, autopct='%.3f', shadow=False ,startangle=440, colors=colors)

plt.title('Resultado Tendencia de Voto: Cuenca')
plt.show()