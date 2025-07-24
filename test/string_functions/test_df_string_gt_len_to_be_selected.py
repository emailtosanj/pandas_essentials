from unittest import TestCase
from string_functions import df_string_gt_len_to_be_selected

from pandas.testing import assert_frame_equal
import pandas as pd

class Test(TestCase):
    def test_invalid_tweets(self):
        # data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
        data = [[2, 'More than fifteen chars are here!']]
        ts = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
        ts_a = df_string_gt_len_to_be_selected.invalid_tweets(ts)
        self.assertIsNotNone(ts_a)
        ts_e = ts[['tweet_id']]
        assert_frame_equal(ts_e, ts_a, check_index_type=False)

    def test_invalid_tweets(self):
        # data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
        data = [[452, 'kWgN63Xj2TFhYDtH0'], [179, 'QFAxkwVQvLTdThlmt']]
        ts = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
        ts_a = df_string_gt_len_to_be_selected.invalid_tweets(ts)
        self.assertIsNotNone(ts_a)
        ts_e = ts[['tweet_id']]
        print(ts_a)
        print(ts_e)
        assert_frame_equal(ts_e, ts_a, check_index_type=False)

    def test_invalid_tweets_emptyval(self):
        ts = pd.DataFrame(None, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
        ts_a = df_string_gt_len_to_be_selected.invalid_tweets(ts)
        self.assertIsNotNone(ts_a)
        ts_e = ts[['tweet_id']]
        print(ts_a)
        print(ts_e)
        assert_frame_equal(ts_e, ts_a, check_index_type=False)
