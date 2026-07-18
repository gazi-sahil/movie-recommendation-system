# 🎬 Movie Recommendation System

A **content-based movie recommendation engine** built in Python. It suggests
similar movies based on genres, director, cast, and plot overview using
**TF-IDF vectorization** and **cosine similarity** — the same core idea
behind many real-world recommendation systems.

## ✨ Features

- Content-based filtering (no user ratings required — works from movie metadata)
- TF-IDF text vectorization with weighted features (genres & cast weighted higher)
- Cosine similarity to rank the most relevant matches
- Two interfaces:
  - **CLI** (`cli.py`) — quick terminal-based testing
  - **Web app** (`app.py`) — interactive Streamlit UI
- Clean, modular code (`recommender.py` is fully reusable/importable)

## 🛠️ Tech Stack

- Python 3.9+
- pandas — data handling
- scikit-learn — TF-IDF + cosine similarity
- Streamlit — web UI

## 📁 Project Structure

```
movie-recommendation-system/
├── data/
│   └── movies.csv          # Movie dataset (title, genres, cast, overview)
├── recommender.py           # Core recommendation engine
├── cli.py                   # Command-line interface
├── app.py                   # Streamlit web app
├── requirements.txt
└── README.md
```

## 🚀 Setup & Usage

1. Clone the repo and move into the folder:
   ```bash
   git clone <your-repo-url>
   cd movie-recommendation-system
   ```

2. (Recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the CLI version:
   ```bash
   python cli.py
   ```

   Or run the web app:
   ```bash
   streamlit run app.py
   ```

## 🧠 How It Works

1. Each movie's **genres, director, cast, and overview** are combined into a
   single text "soup" (genres and cast are repeated to weight them more heavily).
2. `TfidfVectorizer` converts this text into numerical vectors.
3. `cosine_similarity` computes how close each movie is to every other movie.
4. Given a movie title, the engine returns the top-N most similar movies.

## 📈 Possible Improvements (good talking points for interviews)

- Swap the sample dataset for the real **MovieLens** or **TMDB** dataset
- Add **collaborative filtering** (user-based) alongside content-based filtering
- Add a hybrid recommender that blends both approaches
- Deploy the Streamlit app on **Streamlit Community Cloud** for a live demo link
- Add unit tests with `pytest`

## 📌 Resume Bullet (ready to use)

> Built a content-based movie recommendation system in Python using TF-IDF
> vectorization and cosine similarity on movie metadata (genres, cast,
> overview); implemented both a CLI and an interactive Streamlit web app.

---

Feel free to fork, extend the dataset, or connect it to a real movie API!
