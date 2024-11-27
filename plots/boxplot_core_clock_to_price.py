import pandas as pd
import plotly.express as px


df = pd.read_csv('../data/Asus.csv')

df_filtered = df[df["chipset"].str.contains("RTX 40", case=False, na=False)]

df_filtered["boost_clock_per_dollar"] = df_filtered["core_boost_clock"] / df_filtered["price"]

fig = px.box(
    df_filtered.sort_values("boost_clock_per_dollar", ascending=False),
    x="chipset",
    y="boost_clock_per_dollar",
    color="parent_brand",
    title="Boost Clock Per Dollar Across Chipsets and Brands",
    labels={
        "boost_clock_per_dollar": "Clock Speed Per Dollar",
        "chipset": "Chipset"
    },
    hover_data=["price", "core_boost_clock"]
)

fig.update_layout(
    xaxis_title="Chipset",
    yaxis_title="Boost Clock Per Dollar",
    legend_title="Parent Brand",
)

fig.show()
