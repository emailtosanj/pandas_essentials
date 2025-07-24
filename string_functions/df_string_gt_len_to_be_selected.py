# Table: Tweets
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | tweet_id       | int     |
# | content        | varchar |
# +----------------+---------+
# tweet_id is the primary key (column with unique values) for this table.
# content consists of alphanumeric characters, '!', or ' ' and no other special characters.
# This table contains all the tweets in a social media app.
#
#
# Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
#
# Return the result table in any order.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Tweets table:
# +----------+-----------------------------------+
# | tweet_id | content                           |
# +----------+-----------------------------------+
# | 1        | Let us Code                       |
# | 2        | More than fifteen chars are here! |
# +----------+-----------------------------------+
# Output:
# +----------+
# | tweet_id |
# +----------+
# | 2        |
# +----------+
# Explanation:
# Tweet 1 has length = 11. It is a valid tweet.
# Tweet 2 has length = 33. It is an invalid tweet.

# data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
# tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

import pandas as pd


# 1. identify content column val having len > 15
# 2. map and get the identified tweet_id from point 1.
# 3. return corresponding data frame of point 2.

    #DO NOT DO this
    # below code will overwrite the dataframe the
    # moment there is match thus assigning a new data frame
    # -created - this in repetitive iteration overwrites the dataframe
def invalid_tweets_DO_NOT_DO_THIS(tweets: pd.DataFrame) -> pd.DataFrame:
    va = [c[1] for c in tweets.values if (len(c[1]) > 15)]
    for v in va:
        tweets = tweets[tweets['content'] == v]
    return tweets[['tweet_id']]

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tw_fil = tweets[tweets['content'].str.len() > 15]
    return tw_fil[['tweet_id']]

