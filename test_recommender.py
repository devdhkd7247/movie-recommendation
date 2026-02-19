"""
Test file for the Movie Recommendation System
Run with: python test_recommender.py
"""

from recommender import MovieRecommender
import json

# Initialize the recommender
print("Loading recommender system...")
r = MovieRecommender('movies.csv', 'ratings.csv')
print("✓ Recommender loaded successfully!\n")

# Test 1: Get recommendations for different users
print("=" * 60)
print("TEST 1: Get recommendations for users")
print("=" * 60)

for user_id in [1, 5, 10]:
    print(f"\nTop 5 recommendations for User {user_id}:")
    recs = r.recommend_for_user(user_id, 5)
    for i, rec in enumerate(recs, 1):
        print(f"  {i}. {rec['title']} (score: {rec['score']:.4f})")

# Test 2: Get similar movies
print("\n" + "=" * 60)
print("TEST 2: Find similar movies")
print("=" * 60)

movies_to_search = ["Toy Story", "Inception", "Matrix", "Avatar"]
for movie_title in movies_to_search:
    print(f"\nMovies similar to '{movie_title}':")
    similar = r.similar_movies(movie_title, 3)
    if similar:
        for i, sim in enumerate(similar, 1):
            print(f"  {i}. {sim['title']} (score: {sim['score']:.4f})")
    else:
        print(f"  No matches found for '{movie_title}'")

# Test 3: Different recommendation counts
print("\n" + "=" * 60)
print("TEST 3: Different recommendation counts")
print("=" * 60)

user_id = 1
for n in [3, 5, 10]:
    print(f"\nTop {n} recommendations for User {user_id}:")
    recs = r.recommend_for_user(user_id, n)
    print(f"  Returned {len(recs)} recommendations")
    for i, rec in enumerate(recs, 1):
        print(f"    {i}. {rec['title']}")

print("\n" + "=" * 60)
print("All tests completed!")
print("=" * 60)
