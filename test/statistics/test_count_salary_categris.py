from unittest import TestCase

import pandas as pd
from statistics.count_salary_categris import count_salary_categories
from pandas.testing import assert_frame_equal


class Test(TestCase):
    def test_count_salary_categories(self):
        data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
        accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype(
            {'account_id': 'Int64', 'income': 'Int64'})
        df_a = count_salary_categories(accounts)

        df_e = pd.DataFrame([['Low Salary', 1.0],
                              ['Average Salary', 0.0],
                              ['High Salary', 3.0]],
                            columns=['category', 'accounts_count']).astype(
            {'category': 'object', 'accounts_count': 'float64'})
        print('before print df_e')
        print(df_e)

        assert_frame_equal(df_a, df_e)
