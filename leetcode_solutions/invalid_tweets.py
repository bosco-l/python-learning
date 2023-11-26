"""
1683. Invalid Tweets

Easy

https://leetcode.com/problems/invalid-tweets/description/
"""

# SQL Solution
# Write your MySQL query statement below
"""
SELECT tweet_id 
FROM Tweets 
WHERE LENGTH(content) > 15;
"""

# Pandas Solution
import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets = tweets[tweets['content'].str.len() > 15]
    return tweets[['tweet_id']]


if __name__ == '__main__':
    df = pd.DataFrame({'tweet_id': [1, 2],
                       'content': ['Vote for Biden', 'Let us make America great again!']
                       })
    df = invalid_tweets(df)
