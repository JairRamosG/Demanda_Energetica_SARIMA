import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

def grafico_estacional(df, col, periodo, estacionalidad = 'meses', seasonal=True):
    df_c = df.copy()
    
    # Crear columnas de tiempo
    df_c['año'] = df_c.index.year
    df_c['mes'] = df_c.index.month
    df_c['hora'] = df_c.index.hour  
    
    # Calcular componente estacional si se pide
    if seasonal:
        # Ajustar STL con periodo 
        stl = STL(df_c[col], period = periodo).fit()
        df_c[col + '_seas'] = stl.seasonal
        col = col + '_seas'
    
    if estacionalidad == 'meses':
        # Agrupar por mes y hora para obtener un valor único por combinación
        df_agg = df_c.groupby(['mes', 'hora'])[col].mean().reset_index()
        
        # Pivotear: filas = hora, columnas = mes, valores = col (promedio)
        df_pivot = df_agg.pivot(index='hora', columns='mes', values=col)
    
    if estacionalidad == 'años':
        # Agrupar por año y hora para obtener un valor único por combinación
        df_agg = df_c.groupby(['año', 'hora'])[col].mean().reset_index()
        
        # Pivotear: filas = hora, columnas = año, valores = col (promedio)
        df_pivot = df_agg.pivot(index='hora', columns='año', values=col)

        # Graficar
    ax = df_pivot.plot(figsize=(18, 6))
    plt.title(f'Componente estacional - {col}')  
    plt.xlabel('Hora')
    plt.ylabel('MWh')
    plt.legend(title = estacionalidad, ncol=6, loc='best')  
    plt.show()