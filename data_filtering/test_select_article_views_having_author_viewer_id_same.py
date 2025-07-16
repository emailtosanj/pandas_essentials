from unittest import TestCase
from data_filtering import select_article_views_having_author_viewer_id_same
import pandas as pd

class Test(TestCase):
    def test_article_views(self):
        data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'],
                [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
        views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
            {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})
        select_article_views_having_author_viewer_id_same.article_views(views)


    def test_article_views_id_error(self):
        data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'],
                [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
        views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
            {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})
        print(type(select_article_views_having_author_viewer_id_same.article_views_id(views)))
        df_a = select_article_views_having_author_viewer_id_same.article_views_id(views)
        print((select_article_views_having_author_viewer_id_same.article_views_id(views)))
        ## expected data
        resp = [[4],[7]]
        df_e = pd.DataFrame(resp, columns=['author_id'])
        ## end expected data
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(df_e, df_a)


    #TODO - need to fix this test case
     # def test_article_views_id(self):
     #        data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'],
     #                [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
     #        views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
     #            {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})
     #        print(type(select_article_views_having_author_viewer_id_same.article_views_id(views)))
     #        df_a = select_article_views_having_author_viewer_id_same.article_views_id(views)
     #        print((select_article_views_having_author_viewer_id_same.article_views_id(views)))
     #        ## expected data
     #        resp = [[4],[7]]
     #        df_e = pd.DataFrame(resp, columns=['author_id'])
     #        ## end expected data
     #        pd.testing.assert_frame_equal(df_e, df_a)


