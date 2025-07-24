from unittest import TestCase
import pandas as pd

from df_col_int_val_check_criteria import calculate_special_bonus
from pandas.testing import assert_frame_equal
class Test(TestCase):
    def test_calculate_special_bonus(self):
        dat = [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]]
        df_e = pd.DataFrame(dat, columns=['employee_id', 'bonus']).astype({'employee_id':'int64', 'bonus':'int64'})
        data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
        emp = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})
        print(df_e)
        df_a = calculate_special_bonus(emp)
        print(df_a)
        assert_frame_equal(df_e, df_a)

    def test_calculate_special_bonus_empty(self):
        dat = [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]]
        df_e = pd.DataFrame(None, columns=['employee_id', 'bonus']).astype({'employee_id':'int64', 'bonus':'int64'})
        data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
        emp = pd.DataFrame(None, columns=['employee_id', 'name', 'salary']).astype({'employee_id': 'int64',
                                                                                 'name': 'object', 'salary': 'int64'})
        print(df_e)
        df_a = calculate_special_bonus(emp)
        print(df_a)
        assert_frame_equal(df_e, df_a)

    #
    def test_calculate_special_ordered(self):
        dat = [[2, 0], [3, 0], [7, 7700], [8, 6100], [9, 7400]]
        df_e = pd.DataFrame(None, columns=['employee_id', 'bonus']).astype({'employee_id':'int64', 'bonus':'int64'})
        data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [9, 'Addilyn', 7400], [8, 'Juan', 6100], [7, 'Kannon', 7700]]
        emp = pd.DataFrame(None, columns=['employee_id', 'name', 'salary']).astype({'employee_id': 'int64',
                                                                                 'name': 'object', 'salary': 'int64'})
        df_a = calculate_special_bonus(emp)
        assert_frame_equal(df_e, df_a)

    def test_calculate_special_unordered_lowercase(self):

        dat = [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700], [11, 0]]
        df_e = pd.DataFrame(dat, columns=['employee_id', 'bonus']).astype(
            {'employee_id': 'int64', 'bonus': 'int64'})

        data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700],
                [11, 'master', 9000]]
        emp = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
            {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})
        df_a = calculate_special_bonus(emp)
        assert_frame_equal(df_e, df_a)





