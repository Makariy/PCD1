import pandas as pd
import plotly.express as px


dfs = []
for brand in ["Asus", "Gigabyte", "MSI", "XFX", "Zotac"]:
    df = pd.read_csv(f"../data/{brand}.csv")
    df["brand"] = brand
    dfs.append(df)


df = pd.concat(dfs, ignore_index=True)


chipset_filtered = df[df["chipset"] == "GeForce RTX 4070"]

# Calculate the heuristic for each GPU
chipset_filtered["performance_heuristic"] = (
        (chipset_filtered["core_boost_clock"] + chipset_filtered["core_clock"] + chipset_filtered["memory"])
        / chipset_filtered["price"]
)

# Group by brand to calculate the average heuristic
brand_performance = chipset_filtered.groupby("brand").agg(
    avg_heuristic=("performance_heuristic", "mean"),
    count=("name", "size")
).reset_index()


fig = px.bar(
    brand_performance.sort_values("avg_heuristic", ascending=False),
    x="avg_heuristic",
    y="brand",
    text="avg_heuristic",
    orientation="h",
    title="Performance-to-Price Heuristic by Brand (RTX 4070)",
    labels={"avg_heuristic": "Performance-to-Price Heuristic", "brand": "Brand"},
    hover_data=["count"],
)

# Update layout for better readability
fig.update_layout(
    xaxis_title="Performance-to-Price Heuristic",
    yaxis_title="Brand",
    uniformtext_minsize=8,
    uniformtext_mode="hide",
)

fig.show()
