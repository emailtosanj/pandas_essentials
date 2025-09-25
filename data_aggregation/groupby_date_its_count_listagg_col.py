'''
Table Activities:

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.


Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.

The result format is in the following example.



Example 1:

Input:
Activities table:
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+
Output:
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
Explanation:
For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
For 2020-06-02, the Sold item is (Mask), we just return it.'''

import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates()
    '''
    # Below implementation of groupby (pandas.api.typing.DataFrameGroupBy) is a simple version of agg function having NamedAgg version.
    return activities.groupby(by=['sell_date']).agg(num_sold=('sell_date', 'size'),
                                                    products=('product', lambda x: ','.join(sorted(x.unique())))).reset_index()
                                                    
    # below  is a explicit version of groupby (pandas.api.typing.DataFrameGroupBy)  agg function having NamedAgg 
    version.'''

    return activities.groupby(by=['sell_date'], as_index=False).agg(num_sold=(pd.NamedAgg(column='sell_date',
                                                                                   aggfunc='size')),
                                                     products=(
        pd.NamedAgg('product', aggfunc=lambda x: ','.join(sorted(x.unique())))))


'''
    # Learnings
    
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
select to_char(sell_date, 'YYYY-MM-DD') as sell_date, count(sell_date) as num_sold ,
LISTAGG(product, ',') WITHIN GROUP (ORDER BY product) AS products
from (select distinct sell_date, product from Activities) 
group by sell_date    
'''

