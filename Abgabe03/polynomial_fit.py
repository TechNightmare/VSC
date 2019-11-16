import numpy as np
import matplotlib.pyplot as plt

# Laden der gegebenen Daten d0 - d4
x = np.linspace(-2,2,200)
data0 = np.load('data/d0.npy')
data1 = np.load('data/d1.npy')
data2 = np.load('data/d2.npy')
data3 = np.load('data/d3.npy')
data4 = np.load('data/d4.npy')

plt.scatter(x,data0, s=1)
plt.show()
plt.scatter(x,data1, s=1)
plt.show()
plt.scatter(x,data2, s=1)
plt.show()
plt.scatter(x,data3, s=1)
plt.show()
plt.scatter(x,data4, s=1)
plt.show()

# Implementieren Sie ein Funktion, die gegeben den x-Werten und dem Funktiongrad
# die Matrix A aufstellt.

def create_matrix(x, degree):
	matrix = np.zeros((len(x), degree+1), dtype=np.float64)			#(Zeilen, Spalten)	
	matrix[:, -1] = 1

	for j in range(len(x)):
		for i in range(degree):
			matrix[j:, -(i+2)] = x[j] ** (i+1)
	
	return matrix

# Lösen Sie das lineare Ausgleichsproblem
# Hinweis: Nutzen Sie bitte hier nicht np.linalg.lstsq!, sondern implementieren sie A^T A x = A^T b selbst

# Stellen Sie die Funktion mit Hilfe der ermittelten Koeffizienten mit matplotlib
# np.poly1d

def best_function(data, name):
	for i in range(0, 20):
		mat = create_matrix(x, i)
		#print(mat)

		mat_t_mat = np.dot(mat.T, mat)
		mat_t_y = np.dot(mat.T, data)

		koeff = np.linalg.solve(mat_t_mat, mat_t_y)	 
		#print(koeff)

		p = np.poly1d(koeff)
		#print(p)

		#plt.scatter(x,data, s=1)
		#plt.plot(x, p(x))
		#plt.show()

		residual_vect = np.dot(mat, koeff) - data 
		residual = np.linalg.norm(residual_vect) 	# ** 2	entspricht Betrag des Fehlers
		print("Fehler bei Grad ", i, ":", residual)

def safeplot(data, name, degree):
	mat = create_matrix(x, degree)
	
	mat_t_mat = np.dot(mat.T, mat)
	mat_t_y = np.dot(mat.T, data)

	koeff = np.linalg.solve(mat_t_mat, mat_t_y)	 
	
	p = np.poly1d(koeff)
	#print(p)
	plt.scatter(x,data, s=1)
	plt.plot(x, p(x))

	filename = name + "grad" + str(degree) + ".png"
	plt.savefig(filename)
	plt.show()	

#Fehler der Grade ausgeben
best_function(data0, "data0")		#passender Grad: 1
best_function(data1, "data1")		#passender Grad: 2
best_function(data2, "data2")		#passender Grad: 4
best_function(data3, "data3")		#passender Grad: 5
best_function(data4, "data4")		#passender Grad: 7

#Bild der besten Ausgleichfunktion mit Daten
safeplot(data0, "data0", 1)
safeplot(data1, "data1", 2)
safeplot(data2, "data2", 4)
safeplot(data3, "data3", 5)
safeplot(data4, "data4", 7)

"""
Bei den entsprechend gewählten Graden der Funktionen verändert der Fehler sich nicht mehr großartig
Zwar werden die Fehlerwerte immer kleiner, jedoch in der Form nicht mehr ausschlaggebend


Warum ist es sinnvoll möglichst kleine Polynomgrade zu wählen? 
Rechenzeit, Aufwand rechtfertigt Genauigkeit nicht mehr
"""