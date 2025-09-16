import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    p = products.melt(id_vars='product_id', var_name='store', value_name='price')
    p.dropna(subset=['price'], inplace=True)
    p = p.reset_index(drop=True)
    return p

# SQL - MS SQL
# SELECT product_id, store, price
# FROM products
# UNPIVOT (
#     price FOR store IN (store1, store2, store3)
# ) AS unpivoted_products
# WHERE price IS NOT NULL;

# SQL ORACLE
# SELECT product_id, store, price
# FROM products
# UNPIVOT (
#     price FOR store IN (store1, store2, store3)
# )
# WHERE price IS NOT NULL;
