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

Features:

- **👤 Recommend for User** - Get top-N movie recommendations for any user
- **🎥 Find Similar Movies** - Discover movies similar to your favorite film

Try these popular movies:
- Toy Story
- The Matrix
- Avatar
- Inception
- Star Wars

Notes:
- This is an in-memory item-based collaborative filtering system using cosine similarity
- It recommends based on user ratings and movie similarity patterns
- For production use, consider using sparse representations, caching, and persistence