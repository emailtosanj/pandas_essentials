from unittest import TestCase

import pandas as pd

from string_functions.str_contains import find_patients

class Test(TestCase):
    def test_find_patients(self):
        data = [[3, 'Bob', 'DIAB100 MYOP'],
                [4, 'George', 'ACNE DIAB100']]
        patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype(
            {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})

        dat = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'],
                [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]

        p_act= pd.DataFrame(dat, columns=['patient_id', 'patient_name', 'conditions']).astype(
            {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})
        find_patients(patients)
