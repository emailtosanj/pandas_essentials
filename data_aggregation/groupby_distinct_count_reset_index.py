import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(by=['teacher_id'])['subject_id'].nunique().reset_index()
    df.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return df


''' Write your PL/SQL query statement below */
-- select  teacher_id, dept_id, count(subject_id) as cnt  from Teacher
-- group by  teacher_id, dept_id

--Equivalent query for the above pandas
select  teacher_id,  count(distinct(subject_id)) as cnt  from Teacher
group by  teacher_id
'''