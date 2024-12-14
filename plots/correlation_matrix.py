import plotly.express as px

from dataframe import df, columns


columns_cor = columns[0:4]
df_filtered = df[df["chipset"].str.contains("RTX 40", case=False, na=False)].copy()
matrix = df_filtered[columns_cor].corr()

fig = px.imshow(
    matrix,
    text_auto=True,
    title="Mapa de correlaciones entre las variables",
    labels={"color": "Correlation"},
    x=columns_cor,
    y=columns_cor,
    color_continuous_scale="Viridis",
)

fig.show()
