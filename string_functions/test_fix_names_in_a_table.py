from unittest import TestCase

import pandas as pd
from string_functions.fix_names_in_a_table import fix_names

class Test(TestCase):
    def test_fix_names(self):
        data = [[1, 'aLice'], [2, 'bOB'], [3, 'MaRRy aNN']]
        users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
        usr = fix_names(users)
        print(usr)
