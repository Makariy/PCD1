import pandas as pd


dfs = []
for brand in ["Asus", "Gigabyte", "MSI"]:
    df = pd.read_csv(f"../data/{brand}.csv")
    df["brand"] = brand
    dfs.append(df)

columns = ["price", "memory", "core_clock", "core_boost_clock",
           "chipset", "name", "brand", "user_score", "user_ratings_count"]
df = pd.concat(dfs, ignore_index=True).dropna().reset_index(drop=True)
df = df[df["parent_brand"] == "NVIDIA"].reset_index(drop=True)
df = df[columns]

columns = ["price", "memory", "core_clock", "core_boost_clock",
           "chipset", "name", "brand", "user_score", "user_ratings_count"]
