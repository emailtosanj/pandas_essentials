from unittest import TestCase
from pandas.testing import assert_frame_equal
from data_aggregation.groupby_samecol_samecol_cnt import largest_orders
import pandas as pd

class Test(TestCase):
    def test_largest_orders(self):
        data = [[1, 1], [2, 2], [3, 3], [4, 3]]
        orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype(
            {'order_number': 'Int64', 'customer_number': 'Int64'})

        dfa = (largest_orders(orders))

        dt = [3]
        dfe = pd.DataFrame(dt, columns=['customer_number']).astype(
            {'customer_number':'Int64'})
        assert_frame_equal(dfa, dfe)