from statsmodels.tsa.stattools import adfuller
from pmdarima.arima import nsdiffs
import matplotlib.pyplot as plt

def prueba_diferenciacion(serie, d, D, m):
    serie = serie.dropna()

    if d != 0:
        for _ in range(d):
            serie = serie.diff()
    
    if D != 0:
        for _ in range(D):
            serie = serie.diff(m)
    
    resultado_estacionario = adfuller(serie.dropna())
    pvaladfuller = resultado_estacionario[1]

    print('>Prueba Estacionariedad con Dickey-Fuller')
    if pvaladfuller < 0.05:
        print('Rechazar H0: Serie Estacionaria')
        print(f'pval: {pvaladfuller:.4f} < 0.05')
        print('Ya no es necesario diferenciar más')
    else:
        print('Aceptar H0: Serie No Estacionaria')
        print(f'pval: {pvaladfuller:.4f} > 0.05')
        print('Diferenciar nuevamente')

    D_necesaria = nsdiffs(serie.dropna(), m=m, test='ch') 

    print('\n>Prueba Estacionalidad con Canova‑Hansen')
    if D_necesaria > 0:
        print("La serie presenta un patrón estacional")
    else:
        print("Puede no haber un patrón estacional")

    fig, ax = plt.subplots(1, 1, figsize = (15, 5))
    plt.plot(range(1, len(serie)+1), serie)
    plt.hlines(serie.mean(), xmin = 1, xmax = len(serie)+1, color = 'red', label = 'Media', linestyle = '--')
    plt.title(f'Serie d = {d}, D = {D}, m = {m}')
    plt.xlabel('Tiempo')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()