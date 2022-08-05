import numpy as np
import matplotlib.pyplot as plt



'''
como transformar lista em array numpy
l1 = [5,7,8]
arr = np.array(l1)
print(arr, arr.shape)

l2 = [[1,5,8],[18,9,2]]
arr_d = np.array(l2)
print(arr_d, arr_d.shape)

'''

'''
como tirar a media de uma array numpy


arr = [10, 20, 30]
print("1-D array :", arr)
print("Mean of arr is ", np.mean(arr))
'''

'''
como calcular o desvio padrao amostral numpy

arr = [10, 20, 30]
print("1-D array :", arr)
print("Standard Deviation of arr is ", np.std(arr, ddof = 1))

'''
'''
# Exemplo de geração dos vetores de entrada(x, x_err, y, y_err)
x = np.arange(1, 130, 5)
x_err = 0.1*x

y = np.random.uniform(1, 30, len(x))
y = np.sort(y)
y_err = 0.2*y
'''

#desenhando e salvando o grafico

plt.figure(figsize=(10,10))#altera o tamanho do gráfico
plt.rcParams.update({'font.size': 14})#altera o tamanho da font dos eixos

plt.errorbar(x,y,xerr=None,yerr=y_err, fmt='',ecolor='black', mfc='red', mec='black', mew=2, ms=5, capsize=5)# se quiser o marcador bolinha é so no atributo fmt usar assim -> fmt='o'
plt.title('Grafico Y x X com erro', fontsize=20) #adicionando o título do gráfico
plt.xlabel('X', fontsize=20) #adicionandoo nome do eixo x
plt.ylabel('Y', fontsize=20) #adicionandoo nome do eixo y
plt.xlim([0,140])#define o range, de onde ate onde vai, os valores do eixo x
plt.ylim([0,60])#define o range, de onde ate onde vai, os valores do eixo y

plt.savefig('grafico_de_erro.png',dpi=200)
plt.show()