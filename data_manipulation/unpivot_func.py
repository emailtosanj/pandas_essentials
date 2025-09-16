import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    p = products.melt(id_vars='product_id', var_name='store', value_name='price')
    p.dropna(subset=['price'], inplace=True)
    p = p.reset_index(drop=True)
    return p
