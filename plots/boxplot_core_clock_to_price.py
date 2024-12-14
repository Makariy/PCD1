import plotly.express as px

from dataframe import df


df_filtered = df[df["chipset"].str.contains("RTX 40", case=False, na=False)].copy()

df_filtered.loc[:, "boost_clock_per_dollar"] = df_filtered["core_boost_clock"] / df_filtered["price"]

fig = px.box(
    df_filtered.sort_values("boost_clock_per_dollar", ascending=False),
    x="chipset",
    y="boost_clock_per_dollar",
    title="Boost Clock por dolar de las tarjetas gráficas RTX 40 a través de los diferentes vendedores",
    labels={
        "boost_clock_per_dollar": "Clock Speed por Dollar",
        "chipset": "Chipset"
    },
    hover_data=["price", "core_boost_clock", "brand"],
    height=800,
)

fig.update_layout(
    xaxis_title="Chipset",
    yaxis_title="Boost Clock Per Dollar",
    legend_title="Parent Brand",
)

fig.update_traces(marker=dict(color="rgb(118,185,0)"))

fig.show()
