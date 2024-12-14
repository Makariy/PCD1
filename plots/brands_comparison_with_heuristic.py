import plotly.express as px

from utils import apply_chipset_punct, chipset_punct
from dataframe import df


chipset = "GeForce RTX 4070 SUPER"

# Get the best graphics card name for each brand for the given chipset
df_filtered = df[df["chipset"] == chipset]

max_per_brand = df_filtered.groupby("brand") \
    .apply(apply_chipset_punct, include_groups=False) \
    .groupby("brand")["punct"] \
    .idxmax()


max_per_brand = df_filtered.loc[max_per_brand.apply(lambda brand: brand[1])].copy()
max_per_brand.loc[:, "punct"] = chipset_punct(max_per_brand)
max_per_brand = max_per_brand.sort_values("punct", ascending=False)

fig = px.bar(
    max_per_brand,
    x="name",
    y="punct",
    title=f"Mejor tarjeta gráfica para el chipset {chipset} de cada vendedor",
    labels={
        "punct": "Puntuación",
        "name": "Tarjeta Gráfica",
    },
    hover_data=["name", "price", "core_clock", "core_boost_clock", "memory"],
    color="brand",
    width=800,
    height=600,
)

fig.show()
