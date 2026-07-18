"""
Movie Recommendation Engine
----------------------------
A content-based movie recommender that suggests similar movies based on
genres, director, cast, and plot overview using TF-IDF vectorization and
cosine similarity.

Author: You :)
"""

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    
def __init__(self, data_path: str = None):
    if data_path is None:
        data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "movies.csv")        self.data_path = data_path
        self.df = pd.read_csv(data_path)
        self._prepare_data()

    def _prepare_data(self):
        """Combine relevant text features into a single 'soup' column
        and build the TF-IDF matrix + similarity matrix."""
        for col in ["genres", "director", "cast", "overview"]:
            self.df[col] = self.df[col].fillna("")

        # Weight genres and cast more by repeating them — this nudges
        # recommendations towards similar genre/cast rather than only
        # similar plot wording.
        self.df["soup"] = (
            (self.df["genres"] + " ") * 3
            + (self.df["cast"] + " ") * 2
            + self.df["director"] + " "
            + self.df["overview"]
        )

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["soup"])
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

        self.title_to_index = pd.Series(
            self.df.index, index=self.df["title"].str.lower()
        )

    def get_all_titles(self):
        return self.df["title"].tolist()

    def recommend(self, title: str, top_n: int = 5):
        """Return top_n movies most similar to the given title."""
        key = title.strip().lower()
        if key not in self.title_to_index:
            return None

        idx = self.title_to_index[key]
        scores = list(enumerate(self.similarity_matrix[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        # Skip index 0 result since it will always be the movie itself
        scores = [s for s in scores if s[0] != idx][:top_n]

        results = []
        for i, score in scores:
            row = self.df.iloc[i]
            results.append({
                "title": row["title"],
                "genres": row["genres"],
                "overview": row["overview"],
                "similarity": round(float(score), 3),
            })
        return results


if __name__ == "__main__":
    engine = MovieRecommender()
    movie = "Iron Circuit"
    print(f"Recommendations for '{movie}':\n")
    for rec in engine.recommend(movie, top_n=5):
        print(f"- {rec['title']}  (score: {rec['similarity']})")
        print(f"  Genres: {rec['genres']}")
        print(f"  {rec['overview']}\n")
