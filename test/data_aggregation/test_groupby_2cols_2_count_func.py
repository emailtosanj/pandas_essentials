import pandas as pd
from unittest import TestCase

from pandas.testing import assert_frame_equal
from data_aggregation.groupby_2cols_2_count_func import daily_leads_and_partners


class Test(TestCase):
    def test_daily_leads_and_partners(self):
        data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2],
                ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2],
                ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2],
                ['2020-12-7', 'honda', 2, 1]]

        daily_sales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype(
            {'date_id': 'datetime64[ns]', 'make_name': 'object', 'lead_id': 'Int64', 'partner_id': 'Int64'})

        df_a = daily_leads_and_partners(daily_sales)

        print('test ***** actual' )

        # df_a = df_a.sort_values(by=['date_id'])
        print(df_a)
        print('info-- actual')
        print(df_a.info())

        data_e = [['2020-12-8', 'toyota', 2, 3],
                  ['2020-12-7', 'toyota', 1, 2],
                  ['2020-12-8', 'honda', 2, 2],
                  ['2020-12-7', 'honda', 3, 2]]

        df_e = pd.DataFrame(data_e, columns=['date_id', 'make_name', 'unique_leads', 'unique_partners']).astype(
            {'date_id': 'datetime64[ns]', 'make_name': 'object', 'unique_leads': 'int64', 'unique_partners':
                'int64'})

        print('test 111111111 expected')

        # df_e = df_e.sort_values(by=['date_id'])

        df_e = df_e.sort_values(by=['date_id', 'make_name']).reset_index(drop=True)
        print('info-- expected')
        print(df_e.info())

        print(df_e)

        assert_frame_equal(df_a, df_e)

        '''
        set_a = set(tuple(row) for row in df_a.values)
        set_e = set(tuple(row) for row in df_e.values)
        
        if set_a == set_e:
            print("DataFrames have the same content (ignoring order).")
        else:
            print("DataFrames have different content.")
        '''


'''
Ran 1 test in 0.021s

FAILED (failures=1)

Failure
Traceback (most recent call last):
  File "/Users/sanjay/PycharmProjects/pandas_essentials/test/data_aggregation/test_groupby_2cols_2_count_func.py", line 36, in test_daily_leads_and_partners
    assert_frame_equal(df_a, df_e)
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pandas/_testing/asserters.py", line 1279, in assert_frame_equal
    assert_series_equal(
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pandas/_testing/asserters.py", line 1059, in assert_series_equal
    assert_extension_array_equal(
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pandas/_testing/asserters.py", line 794, in assert_extension_array_equal
    assert_numpy_array_equal(
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pandas/_testing/asserters.py", line 690, in assert_numpy_array_equal
    _raise(left, right, err_msg)
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pandas/_testing/asserters.py", line 684, in _raise
    raise_assert_detail(obj, msg, left, right, index_values=index_values)
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pandas/_testing/asserters.py", line 614, in raise_assert_detail
    raise AssertionError(msg)
AssertionError: DataFrame.iloc[:, 0] (column name="date_id") are different

DataFrame.iloc[:, 0] (column name="date_id") values are different (50.0 %)
[index]: [0, 1, 2, 3]
[left]:  [1607299200000000000, 1607299200000000000, 1607385600000000000, 1607385600000000000]
[right]: [1607385600000000000, 1607299200000000000, 1607385600000000000, 1607299200000000000]


Process finished with exit code 1

     date_id make_name  unique_leads  unique_partners
0 2020-12-07     honda             3                2
1 2020-12-07    toyota             1                2
2 2020-12-08     honda             2                2
3 2020-12-08    toyota             2                3
test 111111111
     date_id make_name  unique_leads  unique_partners
0 2020-12-08    toyota             2                3
1 2020-12-07    toyota             1                2
2 2020-12-08     honda             2                2
3 2020-12-07     honda             3                2


'''
