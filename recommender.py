import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self, movies_path, ratings_path, min_movie_ratings=5):
        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)
        self.min_movie_ratings = min_movie_ratings
        self._prepare()

    def _prepare(self):
        ratings = self.ratings
        movie_counts = ratings.groupby('movieId').size()
        popular_movies = movie_counts[movie_counts >= self.min_movie_ratings].index
        ratings_f = ratings[ratings['movieId'].isin(popular_movies)]

        # user x movie pivot
        self.user_item = ratings_f.pivot_table(index='userId', columns='movieId', values='rating')

        # item-user matrix for item-item similarity (rows=movieId, cols=userId)
        item_user = self.user_item.T.fillna(0)

        # compute cosine similarity between items
        self.similarity = cosine_similarity(item_user)

        # mappings
        self.movie_ids = list(item_user.index)
        self.movie_index = {movieId: idx for idx, movieId in enumerate(self.movie_ids)}
        self.index_movie = {idx: movieId for movieId, idx in self.movie_index.items()}
        self.title_map = dict(zip(self.movies['movieId'], self.movies['title']))
        self.item_user_matrix = item_user.values

    def recommend_for_user(self, user_id, n=10):
        if user_id not in self.user_item.index:
            return []
        user_ratings = self.user_item.loc[user_id].fillna(0)
        user_vec = np.array([user_ratings.get(mid, 0) for mid in self.movie_ids])

        scores = self.similarity.dot(user_vec)
        sim_sums = np.abs(self.similarity).sum(axis=1) + 1e-9
        scores = scores / sim_sums

        # exclude already rated
        rated_mask = user_vec > 0
        scores[rated_mask] = -np.inf

        top_idx = np.argsort(scores)[::-1][:n]
        results = []
        for idx in top_idx:
            movieId = self.index_movie[idx]
            results.append({
                'movieId': int(movieId),
                'title': self.title_map.get(movieId, ''),
                'score': float(scores[idx])
            })
        return results

    def similar_movies(self, title, n=10):
        df = self.movies
        matches = df[df['title'].str.contains(title, case=False, na=False)]
        if matches.empty:
            return []
        movieId = matches.iloc[0]['movieId']
        if movieId not in self.movie_index:
            return []
        idx = self.movie_index[movieId]
        sims = self.similarity[idx]
        top_idx = np.argsort(sims)[::-1]
        # exclude self
        top_idx = [i for i in top_idx if i != idx][:n]
        return [
            {'movieId': int(self.index_movie[i]), 'title': self.title_map.get(self.index_movie[i], ''), 'score': float(sims[i])}
            for i in top_idx
        ]


if __name__ == '__main__':
    base = os.path.dirname(__file__)
    movies_path = os.path.join(base, 'movies.csv')
    ratings_path = os.path.join(base, 'ratings.csv')
    print('Loading recommender (this may take a moment)...')
    r = MovieRecommender(movies_path, ratings_path)
    print('Loaded. Example recommendations for user 1:')
    print(r.recommend_for_user(1, 5))