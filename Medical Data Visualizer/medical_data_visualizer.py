import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load the dataset
df = pd.read_csv('Medical Data Visualizer/medical_examination.csv')

# Add 'overweight' column
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# Normalize 'cholesterol' and 'gluc' columns
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    """
    Creates a categorical plot showing the counts of different features split by 'cardio' status.
    """
    # Melt the dataframe for categorical plotting
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group by 'cardio', 'variable', and 'value', then count occurrences
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Create the categorical plot
    plot = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
    figure = plot.fig

    # Save the figure
    figure.savefig('catplot.png')
    return figure

def draw_heat_map():
    """
    Creates a heatmap showing the correlation matrix of features after data cleaning.
    """
    # Data cleaning based on quantiles
    df_clean = df[(df['ap_lo'] <= df['ap_hi']) &
                  (df['height'] >= df['height'].quantile(0.025)) &
                  (df['height'] <= df['height'].quantile(0.975)) &
                  (df['weight'] >= df['weight'].quantile(0.025)) &
                  (df['weight'] <= df['weight'].quantile(0.975))]

    # Compute correlation matrix
    correlation = df_clean.corr()

    # Create a mask for the upper triangle
    upper_triangle_mask = np.triu(np.ones_like(correlation, dtype=bool))

    # Initialize the figure
    fig, ax = plt.subplots(figsize=(16, 9))

    # Generate the heatmap
    sns.heatmap(correlation, mask=upper_triangle_mask, annot=True, fmt=".1f", linewidths=0.5, square=True)

    # Save the figure
    fig.savefig('heatmap.png')
    return fig
