import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import seaborn as sns

def pacf_acf(serie, d, D, m):

    y = serie.dropna().copy()

    if d != 0:
            y = y.diff(d).dropna()
    
    if D != 0 and m !=0:
            for _ in range(D):
                    y = y.diff(m).dropna()

    fig, ax = plt.subplots(3, 1, figsize = (12, 10))

    sns.lineplot(y, ax = ax[0])
    ax[0].set_title(f'Serie diferenciada d = {d}, D = {D}, m = {m}')
    ax[0].set_xlabel('ds')
    ax[0].set_ylabel('y')

    LAGS = 100
    plot_acf(y,
            alpha=0.05,
            lags = LAGS,
            zero=False,
            auto_ylims=True,
            ax = ax[1])
    ax[1].set_title('ACF')
    ax[1].set_xlabel('LAGS')
    ax[1].set_xticks(range(0, LAGS+1, 6))
    ax[1].grid(True)

    plot_pacf(y,
            lags = LAGS,
            zero = False,
            auto_ylims = True,
            ax = ax[2])
    ax[2].set_title('PACF')
    ax[2].set_xlabel('LAGS')
    ax[2].set_xticks(range(0, LAGS+1, 6))
    ax[2].grid(True)

    plt.tight_layout()