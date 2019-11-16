import numpy as np
import matplotlib.pyplot as plt
import tomograph


def show_phantom(size):
    """
    Hilfsfunktion um sich das Originalbild anzuschauen.
    """
    Im = tomograph.phantom(size)
    plt.imshow(Im, cmap='gist_yarg', extent=[-1.0, 1.0, -1.0, 1.0], interpolation='nearest')
    plt.show()


show_phantom(128)

def pol2cart(rho, phi):
    x = rho * np.cos(np.radians(phi))
    y = rho * np.sin(np.radians(phi))
    return(x, y)

def create_sinogram(nAngles, nSamples, angle_range=(0, np.pi)):

    # Winkelschritt 
    phi = 180 / nAngles

    # anlegen der Bildmatrix
    sinogram = np.zeros((nAngles, nSamples))

    # rp - Strahlstartpunkte: pro Winkelschritt, Anzahl der Strahlen pro Winkel viele x-y-Positionen
    # jeweils Tupel mit Koordinaten
    rp = np.zeros([nAngles, nSamples, 2])
    # rd - Strahlrichtungen: pro Winkelschritt ein x-y-Richtung
    rd = np.zeros([nAngles, 2])

    for n in range(nAngles): 
        #strahl richtung
        direction = 180 + n*phi
        cart_direction = pol2cart(1, direction)
        rd[n] = cart_direction
        # mittlerer Strahlstartpunkt
        middle_start_point = [1, (n*phi)]
        cart_middle_start_point = pol2cart(middle_start_point[0], middle_start_point[1])
        # vector mit startpunkten
        point_vector = [1, direction-90]
        # umwandlung in Einheitsvector
        cart_point_vector = pol2cart(point_vector[0], point_vector[1])
        # nSamples 
        scale_vec = np.linspace(-0.99, 0.99, num=nSamples)

        for m in range(nSamples):
            ray_start_point = cart_middle_start_point + np.multiply(cart_point_vector, scale_vec[m])
            rp[n, m] = ray_start_point
            sinogram[n,m] = tomograph.trace(ray_start_point, cart_direction)


    return sinogram, rp, rd

    """
    Funktion soll Sinogram erzeugen

    :param angle_range: Winkel über die die Strahlen laufen in rad. default=(0-180 Grad)
    :param nAngles: Anzahl der Winkelschritte innerhalb der angle_range (Anzahl der Strahlenfronten)
    :param nSamples: Anzahl der Strahlen pro Winkel (Anzahl der Strahlen pro Strahlenfront)

    :return: Tuple sinogram matrix, Strahlstartpunkte, Strahlrichtungen
    """

    # Anlegen von leeren Matrizen für Strahlstart und -richtung

    # Der mittlere Strahlenstartpunkt der Strahlenfront liegt auf dem Einheitskreis.
    # An jedem mittlere Strahlenstartpunkt der Strahenfront soll entlang der
    # Tangente nach links und rechts geganngen werden um die Strahlstartwerte
    # zu berechnen.

    # Tipp: Mittlere Strahlenstartpunkt in Polarkoordinatendarstellung
    # repräsentieren und dann in x/y Position umwandeln.

    # Tipp: Richtungsvektor der Strahlenfront ergibt sich auch direkt aus dem
    # mittlere Strahlenstartpunkt rd[i] -> np.array([-x, -y])

    # Tipp: Die Strahlstartpositionen der Strahlenfront ergeben sich über
    # rp[i, j] = np.array([x,y]) + s*np.array([-y,x])
    # wobei s Anzahl Strahlen viele Skalierungsfaktoren zwischen -1 und 1 mit
    # gleichmäßigen Abständen (np.linspace)

    # Ein sinogramm ist ein Array mit abgeschwaechten Intensitaeten pro Winkel
    # und Strahl, d.h. die Matrix ist ([Anzahl Strahlen] x [Anzahl der Winkel]),
    # bzw. Anzahl der Strahlen pro Aufnahme und die Anzahl der Aufnahmen.

    # for i in AnzahlWinkel:
    #   for j in AnzahlSamples:
    #       trace-Funktion aufrufen und sinogram-Matrix füllen
    #       sinogram[i,j] = ...

    # return sinogram, rp, rd


# ---------------------------------------------
# Main Programablauf:
# ---------------------------------------------
gridsizes = [32, 64] #, 128, 256]
# plot mit unterfigures
fig, ax = plt.subplots(nrows=2, ncols=len(gridsizes))
# Für alle Gridsizes:
for i,ng in enumerate(gridsizes):
    print("GRID: ", ng)
    nGrid = ng
    # die Anzahl der Winkelstufen
    nSamples = 2 * nGrid
    nAngles = 2 * nGrid

    mat, rp, rd = create_sinogram(nSamples, nAngles)
    # Erstellen Sie das Sinogram mithilfe Ihrer zuvor geschriebenen Funktion.
    # Plotten Sie das Sinogram mit Hilfe von Matplotlib. Nutzen Sie die 'gist_yarg' color map
    ax[0][i].imshow(mat, cmap="gist_yarg")

    # Die bekannten aufgenommenen Intensitaetswerte im Sinogram speichern wir als ein Vektor (siehe np.ravel)
    # in logarithmierter Form ab
    i_sino = np.ravel(np.log2(mat))
    # Initialisieren Sie eine Matrix A in der gewünschten Größe.
    mat_A = np.zeros([(nAngles*nSamples), nGrid**2])
    # Für jeden Winkel und jeden Strahl fügen wir jetzt eine Zeile in das Gleichungsystem ein.
    # Dafür müssen Sie über alle Winkel die Funktion grid_intersect (Rückgabe -> I, G, dt)
    # nutzen. I[k] beinhaltet den Index des Strahls, der mit der länge dt[k]
    # den Quadrant G[k] schneidet. Die errechneten Strahllängen pro Quadrant
    # (Pixel) sind dann die Einträge in die Matrix A. Gucken Sie notfalls nochmal
    # die Vorlesungsunterlagen an.
    
    for n in range(nAngles):
        I, G, dt = tomograph.grid_intersect(nGrid, rp[n], rd[n])
        mat_A[I+nSamples*n, G] = dt

    # Achtung!: Die Strahlen indices I beziehen sich immer nur lokal auf die Strahlen,
    # die an grid_intersect übergeben wurden um den richtigen Index in der Matrix
    # zu finden muss (i*nSamples+I) berechnet werden, wobei i die Laufvariabel
    # über alle Winkel(nAngles) ist.
    # Hier kann etwas Indexmagic stattfinden: A[i*nSamples+I, G] = dt
    # Das ist das gleiche wie:
    # for k in range(len(I)):
    #   A[i*nSamples+I[k], G[k]] = dt[k]

    # --------------------------------------------------------------------------
    # Bis hier hin kommt ihr mit der ersten Vorlesung!
    # Wer neugierig ist, kann np.linalg.lstsq(A, b) benutzen.i
    # Was dahinter steckt wird nächste Woche erklärt.
    # --------------------------------------------------------------------------
    mat_t_A = mat_A.T @ mat_A
    mat_t_I = mat_A.T @ i_sino.T

    # Lösen des Ausgleichsproblems mit Hilfe von np.linalg.solve
    x = np.linalg.solve(mat_t_A, mat_t_I)
    # Lösungsvektor wieder auf die gewünschte Form bringen - reshape() und
    # wieder exponieren.
    x = 2**x
    x = x.reshape(nGrid, nGrid)
    # Plotten Sie die Rekonstruktion mit Hilfe von Matplotlib. Nutzen Sie die 'gist_yarg' color map
    ax[1][i].imshow(x, cmap="gist_yarg")


# plt.savefig('tg_fig.png', bbox_inches='tight')
plt.show()
