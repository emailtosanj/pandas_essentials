'''
Table: Accounts

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.


Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output:
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
Explanation:
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.

'''

# data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
# accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})


import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    c = pd.DataFrame(['Low Salary', 'Average Salary', 'High Salary'], columns=['category']).astype(
        {'category': 'category'})
    accounts.loc[(accounts['income'] < 20000), 'category'] = 'Low Salary'
    accounts.loc[(accounts['income'] >= 20000) & (accounts['income'] <= 50000), 'category'] = 'Average Salary'
    accounts.loc[(accounts['income'] > 50000), 'category'] = 'High Salary'
    accounts = accounts.groupby(by=['category'], as_index=False).agg(accounts_count=pd.NamedAgg('category', aggfunc='count'))
    df = pd.merge(c, accounts, how='left', left_on='category', right_on='category', left_index=False).fillna(0)
    return df








'''
Oracle
/* Write your PL/SQL query statement below */


--SELECT * FROM v$version;
--COMMON TABLE EXPRESSION
WITH catgry as (
    SELECT 'Low Salary' as category FROM dual
    UNION ALL SELECT 'Average Salary' FROM dual
    UNION ALL SELECT 'High Salary' FROM dual
),
grp_sal_range as (

    SELECT
    CASE
        WHEN income < 20000 THEN 'Low Salary'
        WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
        WHEN income > 50000 THEN 'High Salary'
    END AS category
    FROM Accounts
)
 SELECT c.category, COUNT(gsr.category) as accounts_count
FROM catgry c
LEFT JOIN
grp_sal_range gsr
ON
c.category = gsr.category
GROUP BY c.category




'''