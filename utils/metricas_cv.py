import numpy as np
import pandas as pd

def metricas_cv(cv_df, nombre_modelos):
    resultados = []
    for modelo in nombre_modelos:
        #Agrupar por cutoff y calcular métricas
        metricas_ventana = []
        for cutoff in cv_df['cutoff'].unique():
            ventana = cv_df[cv_df['cutoff'] == cutoff]
            y_true = ventana['y'].values
            y_pred = ventana[modelo].values
            errores = y_true - y_pred

            rmse = np.sqrt(np.mean(errores**2))         
            mape = np.mean(np.abs(errores / y_true)) * 100
            mae = np.mean(np.abs(errores))
            mae = np.mean(np.abs(errores))

            metricas_ventana.append({'rmse' : rmse, 'mape' : mape, 'mae' : mae})
        
        metricas_df = pd.DataFrame(metricas_ventana)
        resultados.append({
            'Modelo'   : modelo,
            'RMSE'     : metricas_df['rmse'].mean(),
            'MAPE'     : metricas_df['mape'].mean(),
            'MAE'      : metricas_df['mae'].mean(),
            'RMSE_STD' : metricas_df['rmse'].std(),
            'MAPE_STD' : metricas_df['mape'].std(),     
            'MAE_STD'  : metricas_df['mae'].std()    
        })
    df_resultados = pd.DataFrame(resultados)
    df_resultados.index = df_resultados.index + 1
    return df_resultados