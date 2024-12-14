
CC = 0.2
CB = 0.4
MM = 0.4


def standardize(column):
    return (column - column.mean()) / column.std()


def chipset_punct(df):
    return standardize(df["core_boost_clock"]) / standardize(df["price"])


def apply_chipset_punct(df):
    df["punct"] = chipset_punct(df)
    return df[["punct"]]


def graphics_card_punct(df):
    return CC * standardize(df["core_clock"]) + CB * standardize(df["core_boost_clock"]) + MM * standardize(df["memory"])
