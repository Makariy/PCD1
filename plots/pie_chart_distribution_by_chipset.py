import pandas as pd
import plotly.express as px


df = pd.read_csv('../data/Asus.csv')

df_filtered = df[df["chipset"].str.contains("RTX 40", case=False, na=False)]


chipset_data = df_filtered.groupby("chipset").agg(
    count=("chipset", "size"),
    avg_price=("price", "mean")
).reset_index()

fig = px.pie(
    chipset_data,
    names="chipset",
    values="count",
    title="Distribution of GPUs by Chipset",
    hover_data=["avg_price"],
    labels={"avg_price": "Average Price"},
)

fig.update_traces(
    hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Average Price: $%{customdata[0]:.2f}<extra></extra>"
)

fig.show()
