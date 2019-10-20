# coding: utf8
import numpy as np

#task a
#(*) Erzeugen Sie einen Vektor mit Nullen der Länge 10 (10 Elemente) und setzen den Wert des 5.Elementes auf eine 1.
a = np.zeros(10)
a[4] = 1
print(a, '\n')

#task b
#(*) Erzeugen Sie einen Vektor mit Ganzzahl-Werten von 10 bis 49 (geht in einer Zeile).
b = np.arange(10, 50, dtype = int)
print(b, '\n')

#task c
#(*) Erzeugen Sie einen Vektor mit 8 Einträgen zwischen -1 und 1 bei dem alle Werte die gleichen Abstände habe und sowohl -1 als auch 1 enthalten sind (geht in einer Zeile).
c = np.linspace(-1, 1, 10)
print(c, '\n')

#task d
#(*) Geben Sie nur das Stück (slice) von Vektor b) aus, das die Zahlen 21 bis 38 (Stellen 11 bis 28) beinhaltet (geht in einer Zeile).
d = b[11:29]
print(d, '\n')

#task e
#(*) Ändern Sie den Vektor b) indem sie das Stück (slice) von Stelle 15 bis einschließlich Stelle 25 mit den Werten negierten Werten von Stelle 1 bis einschließlich Stelle 11 überschreiben 
b[14:25] = -b[0:11]
print(b, '\n') 

#task f
#(*) Drehen Sie die Werte des Vektors aus a) oder b) um 
f = np.flip(a, 0)
print(f, '\n')

#task g
#(*) Summieren Sie alle Werte in einem Array.
g = np.sum(a)
print(g, '\n')

#task h
#(*) Erzeugen Sie eine 4x4 Matrix mit den Werte 0 (links oben) bis 15 (rechts unten)
h = np.arange(0,16).reshape(4,4)
print(h, '\n')

#task i
#(*) Erzeugen Sie eine 5x3 Matrix mit Zufallswerteintegers zwischen 0-100
i = np.random.randint(100, size=(5,3))
print(i, '\n')

#task j
#(*) Multiplizieren Sie eine 4x3 Matrix mit einer 3x2 Matrix 
mat1 = np.random.randint(100, size=(4,3))
mat2 = np.random.randint(100, size=(3,2))
j = np.matmul(mat1, mat2)
print(j, '\n')

#TODO find better way
#task k
#(*)Erzeugen Sie eine 5x5 Matrix und geben Sie jeweils die geraden und die ungeraden Zeile aus 
k = np.random.randint(100, size=(5,5))
print(k[0:5])
for line in range(5):
	if (line%2 == 0):
		print("gerade Zeile", line, k[line])
	else:
		print("ungerade Zeile", line, k[line])

#task l
# (**) Erzeuge eine 5x5 Matrix mit Zufallsintegers zwischen 0-100 und finde deren Maximum und Minimum und normalisieren Sie die Werte (sodass alle Werte zwischen 0 und 1 liegen - ein Wert wird 1 (max) sein und einer 0 (min)).
# Hinweis: D.h. Sie muessen die Werte normalisieren (R - R_min) / (R_max - R_min)
l = np.random.randint(101, size=(5,5))
#l = np.random.rand(5,5)
print(l, '\n')
#l = l.astype(float)
print((l - np.amin(l)) / (np.amax(l)-np.amin(l)), '\n')


#task m
# (**) Extrahieren Sie den Integer-Anteil eine Arrays von zufälliger Zahlen zwischen 0-10 auf 3 verschiedene Arten.
m = 10 * np.random.rand(10)
print(m, '\n')
print(m.astype(int), '\n')
print(np.trunc(m), '\n')
print(np.fix(m), '\n')
print(np.modf(m)[1], '\n')

#task n
# (**) Erzeugen Sie eine Matrix $M$ der Größe 4x3 und einen Vektor $v$ mit Länge 3. Multiplizieren Sie jeden Spalteneintrag aus $v$ mit der kompletten Spalte aus $M$. Nutzen Sie dafür Broadcasting.
n = np.arange(0,12).reshape(4,3)
v = np.array([1,2,3])
print(n, '\n')
res = n * v
print(res, '\n')

#task o
# (***) Erzeugen Sie einen Zufallsmatrix der Größe 10x2, die Sie als Kartesische Koordinaten interpretieren können ([[x0, y0],[x1, y1],[x2, y2]]).
# Konvertieren Sie diese in Polarkoordinaten \url{https://de.wikipedia.org/wiki/Polarkoordinaten}.
# Hinweis: nutzen Sie fuer die Berechnung des Winkel np.arctan2 und geben Sie jeweils Radius und Winkel als Vektor aus
#Tuple --> [r, phi]
def convtopolar(list):
	r = np.sqrt(list[0]**2 + list[1]**2)
	phi = 0


	if list[0] < 0:
		if list[1] < 0:
			phi = np.arctan2(list[1],list[0]) - np.pi
		else:
			phi = np.arctan2(list[1],list[0]) + np.pi
	elif list[0] == 0:
		if list[1] < 0:
			phi = -np.pi / 2
		elif list[1] > 0:
			phi =  np.pi / 2
	elif list[0] > 0:
		phi = np.arctan2(list[1],list[0])
		
	list = np.array([r, phi])

	return list

o = np.random.randint(10, size =(10,2))
print(o, '\n')

print("Polarcoordinates")
for i in o:
	print(convtopolar(i))

#task z
# (***) Erzeugen Sie einen Matrix der Größe 6x2, die Sie als Kartesische Koordinaten interpretieren können ([[x0, y0],[x1, y1],[x2, y2]]).
# Schreiben Sie eine Funktion, die alle Punkt-Punkt Abstände berechnet.
z = np.random.randint(10, size =(6,2))
print(z, '\n')

def distance(list1, list2):
	dist = np.sqrt((list2[0]-list1[0])**2 + (list2[1]-list1[1])**2) 
	return dist


for i in range(0,z.shape[0]):
	for j in range(i+1, z.shape[0]):
		print("Abstand Punkt ", i+1, "zu Punkt ", j+1, " : ", distance(z[i], z[j]))
