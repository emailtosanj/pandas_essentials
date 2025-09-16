from unittest import TestCase
from data_aggregation.groupby_post_col_creation import total_time

import pandas as pd
from pandas.testing import assert_frame_equal




class Test(TestCase):
    def test_total_time(self):
        data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
        employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})
        dfa  = total_time(employees)

        dat_e = [
                    ['2020-11-28' , '1'      , 173 ],
                    [ '2020-12-03' , '1'      , 41],
                    [ '2020-11-28' , '2'      , 30],
                    [ '2020-12-09' , '2'      , 27]]

        dfe = pd.DataFrame(dat_e, columns=['day', 'emp_id', 'total_time']).astype({
            'day': 'datetime64[ns]', 'emp_id': 'Int64', 'total_time': 'Int64'})


        print(dfa)
        print('\n')
        print(dfe)

        dfe = dfe.sort_values(by = ['day']).reset_index(drop=True)

        assert_frame_equal(dfa, dfe)

