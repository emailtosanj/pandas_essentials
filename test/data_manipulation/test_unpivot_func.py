from unittest import TestCase
import pandas as pd
from data_manipulation.unpivot_func import rearrange_products_table
from pandas.testing import assert_frame_equal




class Test(TestCase):
    def test_rearrange_products_table(self):
        data = [[0, 95, 100, 105], [1, 70, None, 80]]
        products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype(
            {'product_id': 'Int64', 'store1': 'Int64', 'store2': 'Int64', 'store3': 'Int64'})
        df1 = rearrange_products_table(products)

        res_data = [ [0,	'store1', 	95], [1,	'store1', 70], [0,	'store2',	100], [0,	'store3',	105], [1,	'store3',	80]]
        df2 = pd.DataFrame(res_data, columns = ['product_id', 'store', 'price']).astype(
            {'product_id': 'Int64', 'store' : 'str', 'price' : 'Int64'}
        )
        print(df1)
        print('\n')
        print(df2)
        assert_frame_equal(df1, df2)



