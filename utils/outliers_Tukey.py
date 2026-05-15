
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def outliers_Tukey(serie):
    q1, q3 = np.percentile(serie, [25, 75])

    IQR = q3 - q1

    lim_sup = q3 + 1.5*IQR
    lim_inf = q1 - 1.5*IQR

    outliers = serie[(serie.to_numpy() < lim_inf) | (serie.to_numpy() > lim_sup)]
    return outliers

def graficar_outliers(serie, fechas, x_label = 'Tiempo', y_label = None, outliers = None):
    ax = serie.plot(alpha = 0.7)

    serie.loc[fechas].plot(ax = ax, style = 'bo')

    if outliers is not None:
        outliers.plot(ax = ax, style = 'rx')
        plt.legend(['Serie de tiempo', 'Outliers conocidos', 'Outliers desconocidos'])
    else:
        plt.legend(['Serie de tiempo', 'Outliers conocidos'])
    
    plt.xlabel(f'{x_label}')
    plt.ylabel(f'{y_label}')
