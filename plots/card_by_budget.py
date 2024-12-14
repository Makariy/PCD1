import plotly.express as px

from dataframe import df
from utils import graphics_card_punct

budget = 600

chipset_filtered = df[df["price"] <= budget].drop(columns=["user_score", "user_ratings_count"]).dropna()
max_chipsets = chipset_filtered.groupby("chipset", as_index=False)["core_boost_clock"].idxmax()
max_chipsets = chipset_filtered.loc[max_chipsets["core_boost_clock"]]

max_chipsets["punct"] = graphics_card_punct(max_chipsets)
max_chipsets = max_chipsets.sort_values("punct", ascending=False).iloc[:3]

fig = px.bar(
    max_chipsets,
    x=max_chipsets.apply(lambda row: f"{row['name']} - {row['chipset']}", axis=1),
    y="punct",
    title=f"Mejores tarjetas gráficas por debajo de ${budget}",
    labels={"punct": "Puntuación", "x": "Name - Chipset"},
    hover_data=["price", "core_clock", "core_boost_clock", "memory"],
    color="brand",
)
fig.update_traces(width=0.2)
fig.show()
