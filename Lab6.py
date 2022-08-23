import numpy as np
import matplotlib.pyplot as plt


plt.style.use('seaborn-poster')

x = np.linspace(-3, 3, 200)
y = np.zeros(len(x))


plt.figure('Lab 6', figsize=(10, 8))

z1 = (x - (x**3)/(np.math.factorial(3)) + (x**5)/(np.math.factorial(5)))
z2 = (x - (x**3)/(np.math.factorial(3)) + (x**5)/(np.math.factorial(5)) - (x**7)/(np.math.factorial(7)))

plt.plot(x, np.sin(x), 'k', label = 'Sin(x)')
plt.plot(z1, z2, 'r',  label = 'Y3(x) and Y4(x)')
plt.grid()
plt.title('Лабораторна №6')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()