from dataframe import df

import plotly.express as px


chipset = "GeForce RTX 4070 SUPER"

chipset_filtered = df[df["chipset"] == chipset][["user_score", "user_ratings_count", "brand"]].dropna()
chipset_filtered = chipset_filtered[chipset_filtered["user_ratings_count"] > 2].reset_index(drop=True)

grouped = chipset_filtered.groupby("brand").mean().sort_values("user_score", ascending=False).reset_index()

fig = px.bar(
    grouped,
    x="brand",
    y="user_score",
    title=f"Media de puntuación de usuario de {chipset}",
    labels={"user_score": "User Score", "brand": "Brand"},
    width=800,
    height=600,
    color="brand",
    hover_data=["user_ratings_count"]
)
fig.update_traces(width=0.5)
fig.show()
