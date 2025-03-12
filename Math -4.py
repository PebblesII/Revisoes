from cProfile import label
from statistics import linear_regression

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn.linear_model import LinearRegression

area = np.array([50, 60, 80, 100, 120, 150, 180])
quartos = np.array([1, 2, 2, 3, 3, 4, 4])
preco = np.array([200000, 240000, 3100000, 3600000, 4000000, 4500000, 500000])

X = np.column_stack((area, quartos))

modelo = LinearRegression()
modelo.fit(X, preco)

previsao = modelo.predict(X)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(area, quartos, preco, color="blue", label="Dados reais")
ax.plot_trisurf(area, quartos, previsao, color="red", alpha=0.5, label="Plano ajustado")
ax.set_title("Relação entre Área, Número de Quartos e Preço de Venda")
ax.set_xlabel("Área (m²")
ax.set_ylabel("Número de Quartos")
ax.set_zlabel("Preço de Venda (R$)")
plt.legend()
plt.show()
