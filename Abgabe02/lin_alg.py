import numpy as np
import math


# (a) Berechnen Sie den Winkel $\alpha$ in Grad zwischen den folgenden beiden Vektoren $a=[1.,1.77]$ und $b=[1.5,1.5]$
a = np.array([1.,1.77])
b = np.array([1.5,1.5])
print("Punktprodukt der Vektoren: ", np.dot(a,b))

absboth = np.linalg.norm(a) * np.linalg.norm(b)
print("Multiplizierte Beträge: ", absboth)

alpha = np.arccos((np.dot(a,b)) / absboth)
print("Winkel in rad:  ", alpha)
print("Winkel in grad: ", np.degrees(alpha))

# (b) Gegeben ist die quadratische regulaere Matrix A und ein Ergbnisvektor b. Rechnen Sie unter Nutzung der Inversen die Loesung x des Gleichungssystems Ax = b aus.
A = np.matrix('2 3 4;3 -2 -1;5 4 3')
b = np.matrix('1.4; 1.2; 1.4')
print(A, '\n', b)

x = np.linalg.inv(A) * b
print(x)

# (c) Schreiben Sie eine Funktion die das Matrixprodukt berechnet. Nutzen Sie dafür nicht die Numpy Implementierung.
# Hinweis: Fangen Sie bitte mögliche falsche Eingabegroessen in der Funktion ab und werfen einen AssertionError
# assert Expression[, Arguments]

def matmult(M1, M2):
    assert (M1.shape[1] == M2.shape[0]), "ungleiche Dimensionen"

    #Dimensionen
    lines = M1.shape[0]
    columns = M2.shape[1]
    
    result = np.zeros((lines, columns))
    #Matrixmultiplikation
    for i in range(0, lines):
    	for k in range(0, columns):
    		for j in range(0, M1.shape[1]):
    			result[i,k] = result[i,k] + M1[i,j] * M2[j,k]

    return result   

M1 = np.matrix('1 2; 3 4; 5 6')
M2 = np.matrix('2 0; 0 2')

print(M1,'\n', M2)

M_res = matmult(M1, M2)
print(M_res)