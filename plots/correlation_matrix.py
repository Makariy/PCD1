import pandas as pd
import plotly.express as px


df = pd.read_csv('../data/Asus.csv')

df_filtered = df[df["chipset"].str.contains("RTX 40", case=False, na=False)]

columns = ["price", "memory", "core_clock", "core_boost_clock", "length", "user_score", "user_ratings_count"]
matrix = df_filtered[columns].corr()

fig = px.imshow(
    matrix,
    text_auto=True,
    title="Correlation Heatmap of GPU Attributes",
    labels={"color": "Correlation"},
    x=columns,
    y=columns,
    color_continuous_scale="Viridis",
)

fig.show()
