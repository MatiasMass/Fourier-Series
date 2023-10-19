import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

def fourier(a0, an, bn, n, frec, x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = a0 / 2
        for j in range(n):
            y[i] += an[j] * np.cos((j + 1) * frec * x[i]) + bn[j] * np.sin((j + 1) * frec * x[i])

    return y

n = 1000 # Cambiar n según el ejercicio
frec = 1 # Cambiar frec según el ejercicio
a0 = 2 * PI # Cambiar a0 según el ejercicio

# Calcula los coeficientes an y bn
an = [0] * n # Inicializa an con ceros
bn = [0] * n # Inicializa bn con ceros

for i in range(1, n + 1):
    an_i = 0 # Cambiar an_i según el ejercicio
    bn_i = (-2 * (-1)**i)/i # Cambiar bn_i según el ejercicio
    an[i - 1] = an_i
    bn[i - 1] = bn_i

x = np.linspace(-3 * PI , 3 * PI , 500, endpoint=False)
y = fourier(a0, an, bn, n, frec, x)

plt.plot(x, y, label='Fourier')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de la función f(t)')
plt.legend()
plt.grid()
plt.show()
