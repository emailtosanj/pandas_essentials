from unittest import TestCase
from pandas.testing import assert_frame_equal

from data_aggregation.groupby_count_limited import find_classes

import pandas as pd

class Test(TestCase):
    def test_find_classes(self):
        data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
        courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})
        df = courses.groupby(by=['class'])['student'].count().reset_index()
        df = df[ df['student'] >= 5 ]
        dfe = df[['class']]
        dfa = find_classes(courses)
        assert_frame_equal(dfa, dfe)

