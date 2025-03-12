from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tensorflow.python.feature_column.feature_column import linear_model

preco = np.array([10, 15, 20, 25, 30, 35, 40])
vendas = np.array([100, 90, 80, 60, 50, 30, 20])

preco = preco.reshape(-1, 1)



modelo = LinearRegression()
modelo.fit(preco, vendas)

previsao = modelo.predict(preco)

plt.scatter(preco, vendas, color="blue", label="Dados reais")
plt.plot(preco, previsao, color="red", linewidth="2", label="Modelo linear")
plt.title("relação entre preço e venda")
plt.xlabel("preço do produto")
plt.ylabel("vendas mensais")
plt.legend()
plt.grid(True)
plt.show()