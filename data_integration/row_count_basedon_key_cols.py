'''

data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})

'''

import pandas as pd

#TODO - write unit tests fro this
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(by=['actor_id', 'director_id'], as_index=False).agg(num_sold=(pd.NamedAgg(
        column='actor_id', aggfunc='size')));
    df = df[df['num_sold'] >= 3]
    return df[['actor_id', 'director_id']]



