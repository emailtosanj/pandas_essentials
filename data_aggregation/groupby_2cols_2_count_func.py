'''
Table: DailySales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters.


For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
DailySales table:
+-----------+-----------+---------+------------+
| date_id   | make_name | lead_id | partner_id |
+-----------+-----------+---------+------------+
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |
+-----------+-----------+---------+------------+
Output:
+-----------+-----------+--------------+-----------------+
| date_id   | make_name | unique_leads | unique_partners |
+-----------+-----------+--------------+-----------------+
| 2020-12-8 | toyota    | 2            | 3               |
| 2020-12-7 | toyota    | 1            | 2               |
| 2020-12-8 | honda     | 2            | 2               |
| 2020-12-7 | honda     | 3            | 2               |
+-----------+-----------+--------------+-----------------+
Explanation:
For 2020-12-8, toyota gets leads = [0, 1] and partners = [0, 1, 2] while honda gets leads = [1, 2] and partners = [1, 2].
For 2020-12-7, toyota gets leads = [0] and partners = [1, 2] while honda gets leads = [0, 1, 2] and partners = [1, 2].
'''

import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:

    return daily_sales.groupby(by=['date_id', 'make_name'], as_index=False).agg(
        unique_leads=pd.NamedAgg(column='lead_id', aggfunc='nunique'),
        unique_partners=pd.NamedAgg(column='partner_id', aggfunc='nunique')
    )

    # Learnings

    # references
    # help(pd.DataFrame.groupby)
    # help(pandas.api.typing.DataFrameGroupBy.agg)

    '''
    Having reset_index and having as_index=False gets me the same result, is there any difference in performance with its usage
    That's a great question! While as_index=False in groupby and using reset_index() after groupby().agg() often yield the same resulting DataFrame structure, there can be a performance difference, especially with large datasets.
    
    Here's a breakdown:
    
    groupby(..., as_index=False): This approach prevents the creation of a MultiIndex during the grouping operation. By not creating and then discarding the index, it can be more memory-efficient and potentially faster, as it avoids an intermediate step.
    groupby(...).agg(...).reset_index(): This approach first creates a MultiIndex (or Index) from the grouping columns and then converts it back into regular columns. This involves an extra step of creating and then resetting the index, which can add overhead in terms of both time and memory, particularly for large DataFrames.
    In general, using as_index=False is the recommended and often more performant way to achieve the desired result when you know during the grouping step that you don't want the grouping columns to be part of the index.
    
    For smaller datasets, the performance difference might be negligible, but for larger datasets, using as_index=False can lead to noticeable improvements.
    
    To be certain about the performance difference for your specific use case and data, you can always use timing functions (like %%timeit in Colab) to compare the execution speed of both approaches.
    '''


'''
oracle SQL works
select to_char(date_id, 'yyyy-mm-dd') date_id, make_name, count(distinct(lead_id))
unique_leads, count(distinct(partner_id)) unique_partners from DailySales
group by date_id, make_name
'''