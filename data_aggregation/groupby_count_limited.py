# data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
# courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by=['class'])['student'].count().reset_index()
    df = df[df['student'] >= 5]
    return df[['class']]



'''
 Oracle Query
 /* Write your PL/SQL query statement below */
# select class from Courses group by class having count(class) >= 5;

'''