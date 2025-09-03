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
# cholesterol e gluc
def transformar_valores(valores):
    if valores == 1:
        return 0
    else:
        if valores > 1:
            return 1
        
df['cholesterol'] = df['cholesterol'].apply(transformar_valores)
df['gluc'] = df['gluc'].apply(transformar_valores)

# 4
def draw_cat_plot(df):
    #5
    df_cat = pd.melt(df,
                     value_vars=['gluc', 'cholesterol', 'smoke', 'alco', 'active', 'cardio'])
    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # 7
         # 8
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar',
        height=5,
        aspect=1
    )
    fig.set_axis_labels("Categoria", "Contagem")
    fig.set_titles("Cardio = {col_name}")

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    cond_ap = df['ap_lo'] <= df['ap_hi']
    cond_height = (df['height'] >= df['height'].quantile(0.025)) & \
                (df['height'] <= df['height'].quantile(0.975))
    cond_weight = (df['weight'] >= df['weight'].quantile(0.025)) & \
                (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df[cond_ap & cond_height & cond_weight]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(10,8))

    # 15
    sns.heatmap(
        corr,            
        mask=mask,        
        annot=True,        
        square=True,     
        cbar_kws={"shrink": 0.75}, 
        ax = ax
    )


    # 16
    fig.savefig('heatmap.png')
    return fig
