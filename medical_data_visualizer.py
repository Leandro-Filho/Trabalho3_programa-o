import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df["altura_metros"] = df["height"] / 100
df["IMC"] = df["weight"] / ((df["altura_metros"]) ** 2)
def classificar_acima_do_peso(imc):
    if imc > 25:
        return 1
    else:
        return 0

df["overweight"] = df["IMC"].apply(classificar_acima_do_peso)

# 3


# 4
def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
