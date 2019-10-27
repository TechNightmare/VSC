import numpy as np
from math import sqrt, fabs, pi
import matplotlib.pyplot as plt

# Aufgabe 1 (a)
# i ist hier die Anzahl der Iterationen
# In jeder Iteration soll ein epsilon auf 1.0 addiert werden und mit der
# Floating-Point Darstellung von np.float64(1) bzw. np.float(32) verglichen werden.
# Starten Sie dabei mit Epsilon=1.0 und halbieren Sie den Wert in jeder Iteration (wie an der Ausgabe 2^(-i) zu sehen)
# Stoppen Sie die Iterationen, wenn np.float32(1) + epsi == np.float32(1) ist.
# Hinweis: Ja - in diesem Fall dürfen Sie Floating-Point Werte vergleichen ;)

#python float
epsi = float(1)
i = 0

print(type(epsi))

# Print Anweisung vor dem Loop
print('i | 2^(-i) | 1 + 2^(-i) ')
print('----------------------------------------')

while float(1) + epsi != float(1):
	print('{0:4.0f} | {1:16.8e} | ungleich 1'.format(i, epsi))
	epsi /= 2
	i += 1



#numpy float32

epsi = 1.0
i = 0

print(type(epsi))

# Print Anweisung vor dem Loop
print('i | 2^(-i) | 1 + 2^(-i) ')
print('----------------------------------------')

while np.float32(1) + epsi != np.float32(1):
	print('{0:4.0f} | {1:16.8e} | ungleich 1'.format(i, epsi))
	epsi /= 2
	i += 1


#numpy float64
epsi = np.float64(1)
i = 0
print(type(epsi))

# Print Anweisung vor dem Loop
print('i | 2^(-i) | 1 + 2^(-i) ')
print('----------------------------------------')

while np.float64(1) + epsi != np.float64(1):

	print('{0:4.0f} | {1:16.8e} | ungleich 1'.format(i, epsi))
	epsi /= 2
	i += 1

# Aufgabe 1 (b)
# Werten Sie 30 Iterationen aus und speichern Sie den Fehler in einem
# Fehlerarray err
N = 30
err = []
# sqrt(2) kann vorberechnet werden
sn = sqrt(2)			#sn für 2² Eck also Quadrat, Startpunkt für Berechnung von n+1

for n in range(3, N):
    # 1. Umfang u berechnen
    s = sqrt(2 - sqrt(4 - sn**2))
    u = s * (2**n)

    # 2. Fehler en berechnen und in err speichern
    en = abs((2 * pi) - u)
    err.append(en)
    # Fehler ausgeben 
    print('{0:2d}\t{1:1.20f}\t{2:1.20e}'.format(n, u, en))
    sn = s 		#neues sn

# Plotten Sie den Fehler
plt.figure(figsize=(6.0, 4.0))
plt.semilogy(range(3, N), err, 'rx')
plt.xlim(2, N - 1)
plt.ylim(1e-16, 10)


# Aufgabe 1 (c)
# besser Approximation
# Löschen des Arrays und wir fangen mit der Berechnung von vorn an.
# Nur diesmal mit der leicht veranderten Variante
err = []

# sqrt(2) kann vorberechnet werden
sn = sqrt(2)			#sn für 2² Eck also Quadrat

for n in range(3, N):
    # 1. Umfang u berechnen
    s = sn / (sqrt(2 + sqrt(4 - sn**2)))
    u = s * (2**n)

    # 2. Fehler en berechnen und in err speichern
    en = abs((2 * pi) - u)
    err.append(en)
    # Fehler ausgeben 
    print('{0:2d}\t{1:1.20f}\t{2:1.20e}'.format(n, u, en))
    sn = s 		#neues sn

plt.figure(figsize=(6.0, 4.0))
plt.semilogy(range(3, N), err, 'rx')
plt.xlim(2, N - 1)
plt.ylim(1e-16, 10)
plt.show()

#Auswertung Plots
#Figure 1: Zunächst wird der Fehler immer kleiner(bis 10⁻9, beim 2^15-Eck) Dann wächst der Fehler wieder an.
#Bei einigen Approximationen entstehen exakte gleiche Werte(wegen der Ungenauigkeit?)
#Figure 2: Die Genauigkeit ist wesentlich besser als bei der ersten Variante. Der Fehler sinkt auf 10⁻16 beim 2^26-Eck
#Ab diesem Wendepunkt wird der Fehler wieder größer