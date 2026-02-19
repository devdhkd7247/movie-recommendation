# Movie Recommendation — Streamlit Interface

Quick start:

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the Streamlit app:

```powershell
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Features

- **👤 Recommend for User** - Get top-N movie recommendations for any user
- **🎥 Find Similar Movies** - Discover movies similar to your favorite film

## Screenshots

### User Recommendations Tab
![User Recommendations](screenshots/user_recommendations.png)

### Similar Movies Tab
![Similar Movies](screenshots/similar_movies.png)

## Try These Popular Movies
- Toy Story
- The Matrix
- Avatar
- Inception
- Star Wars
- Forrest Gump
- Jurassic Park

## How It Works

This system uses **Item-Based Collaborative Filtering**:
- Analyzes user ratings to find movie similarities
- Recommends movies based on similar users' preferences
- Uses cosine similarity to measure movie-to-movie relationships

## Notes

- In-memory collaborative filtering using scikit-learn
- Dataset: 9,742 movies with 100,838 ratings
- For production use, consider: sparse representations, caching, database persistence, and incremental model updates