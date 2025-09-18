from unittest import TestCase
from pandas.testing import assert_frame_equal
from data_aggregation.groupby_distinct_count_reset_index import count_unique_subjects
import pandas as pd
class Test(TestCase):
    def test_count_unique_subjects(self):
        data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
        teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype(
            {'teacher_id': 'Int64', 'subject_id': 'Int64', 'dept_id': 'Int64'})

        dfa = count_unique_subjects(teacher)

        # test
        dfe = teacher.groupby(by=['teacher_id'])['subject_id'].nunique().reset_index()
        dfe.rename(columns={'subject_id': 'cnt'}, inplace=True)
        # end test

        # assert test
        assert_frame_equal(dfe, dfa)
