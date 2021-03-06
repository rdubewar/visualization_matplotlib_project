import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    df = ipl_df.groupby(['batting_team'])['match_code'].count()
    x_series = np.arange(df.count())
    y_series = df.values
    plt.bar(x_series,y_series)
    plt.xticks(x_series, df.index,  rotation=90)
    plt.show()
    return


#plot_deliveries_by_team()
